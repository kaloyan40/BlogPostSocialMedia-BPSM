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
    tags_to_remove = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'v-model': 'tagsToRemove'}
        ))

    tags_to_add = forms.CharField(
        required=False,
        widget=forms.HiddenInput(
            attrs={'v-model': 'tagsToAdd'}
        ))

    class Meta(CreatePostForm.Meta):
        fields = ['name', 'content']

    def save(self, commit=True):
        instance = super(EditPostForm, self).save(commit=False)

        tags_to_remove = self.cleaned_data.get('tags_to_remove', '')
        if tags_to_remove:
            try:
                tags_to_remove_list = tags_to_remove.split(",")
                tags_to_remove_objects = Tag.objects.filter(id__in=tags_to_remove_list)
                instance.tag_set.remove(*tags_to_remove_objects)
            except Exception as e:
                raise ValidationError(f'Невалидни тагове за премахване: {e}')

        tags_to_add = self.cleaned_data.get('tags_to_add', '')
        if tags_to_add:
            try:
                tags_to_add_list = tags_to_add.split(",")
                tags_to_add_objects = Tag.objects.filter(id__in=tags_to_add_list)
                instance.tag_set.add(*tags_to_add_objects)
            except Exception as e:
                raise ValidationError(f'Невалидни тагове за добавяне: {e}')

        if commit:
            instance.save()
        return instance
