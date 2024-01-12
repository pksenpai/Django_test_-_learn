from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    # email = forms.CharField(label="email", max_length=150)
    class Meta:
        model = User
        fields = ['email']
    
    def clean(self):...
        
    