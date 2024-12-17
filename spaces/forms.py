from Tekst.utils import sanitize_and_escape
from django import forms
from .models import Space, Tag
from django.core.exceptions import ValidationError


class CreateSpaceForm(forms.ModelForm):
    tags = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'id': 'tags-input'}
        ))

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Name', ':class': "['form-control', {'is-invalid': !nameInputValid && showInvalidMessage}]", 'v-model': 'nameInput'}
        ))

    description = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'v-model': 'descriptionInput'}
        ))

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control', 'id': 'image-field'}
        ))

    class Meta:
        model = Space
        fields = ['name', 'description', 'image']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return sanitize_and_escape(description)

    def clean(self):
        cleaned_data = super().clean()
        tags = cleaned_data.get('tags', '')

        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]

        if len(tag_list) < 3:
            raise ValidationError("Трябват ти поне 3 тага.")

        cleaned_data['tags'] = ','.join(tag_list)
        return cleaned_data

    def save(self, commit=True):
        space = super().save(commit=False)
        if commit:
            space.save()
            tags = self.cleaned_data['tags']
            if tags:
                tag_list = [tag.strip() for tag in tags.split(',')]
                new_tags = [Tag(name=tag_name, space=space) for tag_name in tag_list]
                Tag.objects.bulk_create(new_tags)
        return space


class EditSpaceForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Name', 'class': "form-control", 'v-model': 'nameInput'}
        ))

    description = forms.CharField(
        widget=forms.HiddenInput(
            attrs={'v-model': 'descriptionInput'}
        ))

    class Meta:
        model = Space
        fields = ['name', 'description']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return sanitize_and_escape(description)
