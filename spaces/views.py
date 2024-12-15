from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views import View
from .forms import CreateSpaceForm, EditSpaceForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Count
from .models import Space, UserSpaceFollow, Tag


class SpaceCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'spaces/create-space.html'
    form_class = CreateSpaceForm
    success_message = 'Темата беше създадена успешно'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class SpaceEditView(View):
    form_class = EditSpaceForm
    template_name = "spaces/edit-space.html"

    @staticmethod
    def _handle_form_errors(request, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"Грешка в полето {field}: {error}")

    def _validate_ownership(self, space, user):
        if space.user != user:
            messages.error(self.request, "Нямате право да редактирате тази тема.")
            raise PermissionError()

    def get(self, request, *args, **kwargs):
        # Find space
        space = get_object_or_404(Space, slug=self.kwargs['slug'])

        # Validate if space belongs to the user
        try:
            self._validate_ownership(space, request.user)
        except PermissionError:
            return redirect('home')

        form = self.form_class(instance=space)

        context = {
            "form": form,
            "space": space
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        space = get_object_or_404(Space, slug=self.kwargs['slug'])
        form = self.form_class(request.POST, instance=space)

        if form.is_valid():
            form.save()
            messages.success(request, "Темата се поднови успешно!")
            return redirect('space_details', slug=space.slug)
        else:
            self._handle_form_errors(request, form)

        context = {
            "form": form,
            "space": space
        }

        return render(request, self.template_name, context)


class SpaceListView(ListView, LoginRequiredMixin):
    template_name = 'spaces/list-spaces.html'
    model = Space
    paginate_by = 12

    def get_queryset(self):
        queryset = Space.objects.all()

        order = self.request.GET.get('order')
        verified = self.request.GET.get('verified')

        if order == 'newest':
            queryset = queryset.order_by('-created_at')
        elif order == 'oldest':
            queryset = queryset.order_by('created_at')
        elif order == 'top':
            queryset = queryset.annotate(num_followers=Count('followers')).order_by('-num_followers')
        else:
            queryset = queryset.order_by('name')

        if verified:
            queryset = queryset.filter(verified=True)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SpaceListView, self).get_context_data(*args, **kwargs)
        context['name'] = self.request.GET.get('name')
        context['content'] = self.request.GET.get('content')

        if self.request.user.is_authenticated:
            followed_spaces = UserSpaceFollow.objects.filter(user=self.request.user).values_list('space_id', flat=True)
            context['followed_spaces'] = followed_spaces

        return context


class SpaceDetailView(DetailView):
    template_name = 'spaces/space-details.html'
    model = Space

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Space, slug=slug)

    def get_context_data(self, *args, **kwargs):
        context = super(SpaceDetailView, self).get_context_data()
        space = self.get_object()
        context['in_space_details'] = True
        context['tags'] = Tag.objects.filter(space=space)

        if self.request.user.is_authenticated:
            context['is_following'] = UserSpaceFollow.objects.filter(user=self.request.user, space=space).exists()
        else:
            context['is_following'] = False

        return context
