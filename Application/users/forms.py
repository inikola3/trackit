from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control_users', 'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control_users', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control_users', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control_users', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control_users', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control_users', 'placeholder': 'Email'}),
        }

    error_messages = {
        'username':{
            'required' : "Please enter your username"
        }
    }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control_users'})
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'
    

#Custom user auhthentication form
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control_users', 'placeholder': 'Username'}),
        error_messages={'required': 'Please enter your username'}
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control_users', 'placeholder': 'Password'}),
        error_messages={'required': 'Please enter your password'}
    )

    class Meta:
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control_users'})
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'