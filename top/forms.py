from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import ClassData
class SignUpForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.exclude(name__in=["統括管理", "Superuser"]),
        required=True
    )
    class Meta:
        model = User
        fields = ('username', 'group', 'password1', 'password2')

class ClassDataForm(forms.ModelForm):
    class Meta:
        model = ClassData
        fields = ['classname', 'data']
