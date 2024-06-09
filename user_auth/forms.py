from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email address is already in use."))
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
