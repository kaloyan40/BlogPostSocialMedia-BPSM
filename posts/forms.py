from Tekst.utils import sanitize_and_escape
from django.core.exceptions import ValidationError
from django import forms
from .models import Post
from spaces.models import Space, Tag


class CreatePostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'id': 'tags-input', 'v-model': 'tags'}
        ),
        required=False
    )

    space = forms.ModelChoiceField(
        queryset=Space.objects.all(),
        widget=forms.HiddenInput(
            attrs={'id': 'space-select', 'v-model': 'spaceInput'}
        ),
        required=False
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Name', 'class': 'form-control', 'v-model': 'name'}
        ),
        required=False
    )

    content = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'v-model': 'content'}
        ))

    visibility = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input', 'id': 'flexSwitchCheckDefault'}
        ),
        required=False,
        initial=True
    )

    class Meta:
        model = Post
        fields = ['name', 'content', 'visibility', 'space']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        return sanitize_and_escape(content)

    def save(self, commit=True):
        instance = super(CreatePostForm, self).save(commit=False)
        tags = self.cleaned_data.get('tags', '')

        if commit:
            instance.save()

        if tags:
            try:
                list_tags = tags.split(",")
                tags_to_add = Tag.objects.filter(id__in=list_tags)
                instance.tag_set.add(*tags_to_add)
            except Exception as e:
                raise ValidationError(f'Невалидни тагове: {e}')

        if commit:
            instance.save()
        return instance


class EditPostForm(CreatePostForm):
    class Meta(CreatePostForm.Meta):
        fields = ['name', 'content']
