from django import forms
from .models import SellerProfileModel
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)

class SellerProfileCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = SellerProfileModel
        exclude = ('is_active',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = super(SellerProfileCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class SellerLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SellerLoginForm, self).__init__(*args, **kwargs)

        self.utils = FormHelper()
        self.utils.layout = Layout(
            'username',
            'password',
            Submit('login', 'Login', css_class='btn-primary')
        )
