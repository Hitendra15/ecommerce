from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=3,max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter username'}),error_messages={'required':'please enter username','min_length':'please enter atleast 3 character','max_length':'please enter charcter less than 20'})
    email = forms.EmailField(min_length=5,max_length=30,widget=forms.EmailInput(attrs={'placeholder':'Enter email'}),error_messages={'required':'please enter email','min_length':'please enter atleast 5 character','max_length':'please enter character less than 30'})
    password1 = forms.CharField(label='Password',min_length=5,widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}),error_messages={'required':'please enter password','min_length':'please enter strong password'})
    password2 = forms.CharField(label='Confirm Password',min_length=5,widget=forms.PasswordInput(attrs={'placeholder':'Enter confirm password'}),error_messages={'required':'please enter confirm password'})
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password1')
        cpassword = self.cleaned_data.get('password2')
        if password and cpassword and cpassword != password:
            raise forms.ValidationError('Password does not match')
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username'}),error_messages={'required':'please enter username'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}),error_messages={'required':'please enter password'})

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username',error_messages={'required':'please enter username'})
    email = forms.EmailField(label='Email',error_messages={'required':'please enter email'})
    class Meta:
        model = User
        fields = ('username','email')
