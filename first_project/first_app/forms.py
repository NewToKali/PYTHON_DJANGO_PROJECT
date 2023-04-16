from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("value needs to start with certian z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(validators=[validators.validate_email])
    vemail = forms.EmailField(validators=[validators.validate_email])
    text= forms.CharField(widget=forms.Textarea, validators=[check_for_z])
    botcatcher = forms.ChoiceField(required=False , widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data= super().clean()
        if all_clean_data["email"].lower() != all_clean_data["vemail"].lower():
            raise forms.ValidationError("emails don't match")
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
