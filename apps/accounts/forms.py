from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,PasswordInput
from apps.accounts.models import Profile
class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exist!")
        except User.DoesNotExist as e:
            pass

        except Exception as e:
            raise forms.ValidationError("Email already Exist!")

class UserRegisterForm(ModelForm):
    # email = EmailValidation(required=True)
    class Meta:
        model = User
        fields =['email','username','password']
        widgets ={
            'username':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'password':PasswordInput(attrs={'class':'form-control'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()



    class Meta:
        model = User
        fields = ['username', 'email' ,'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_image']