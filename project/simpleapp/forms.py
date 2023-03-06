from django import forms
from django.core.exceptions import ValidationError
from .models import News, Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'name',
            'description',
            'category',
        ]

    categoryType = forms.ChoiceField(
        label='ТИП',
        choices=Post.CATEGORIES
    )

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'description',
            'categoryType',
        ]
