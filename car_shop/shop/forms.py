from django import forms

from .models import Car, Comment


class CarForm(forms.ModelForm):
    '''Form for cars.'''

    class Meta:
        model = Car
        exclude = ('owner', 'created_at', 'updated_at',)


class CommentForm(forms.ModelForm):
    '''Form for comments.'''

    class Meta:
        model = Comment
        fields = ('content',)
