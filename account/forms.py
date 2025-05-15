from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ["username", "email"]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if MyUser.objects.filter(username=username).exists():
            raise ValidationError("username number already exists.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ["username", "email", "password", "is_active", "is_admin"]

#def start_value_0(value):
 #   if value[0]!= '0':
  #      raise ValidationError("should be 0")
   # return value
#def len_value(value):
 #   if len(value) != 11:
  #      raise ValidationError("should be 11")
   # return value
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username ","class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password","class":"form-control"}))

    #def clean(self):
     #   cd = super().clean()
      #  username = cd['username']
     #and check for username
    #in html for x in form.non_field_errors

