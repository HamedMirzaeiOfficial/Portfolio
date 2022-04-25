from django import forms
from django.core.exceptions import ValidationError
from .models import Comment, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        labels = {
            'body': 'Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your message...'})
        }

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'hamed mirzaei':
            raise ValidationError("Sorry, you cannot use this name.")
        return data


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your message...'})
        }
        labels = {
            'body': 'Message',
        }


