from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, help_text="Enter username")

    def validate_username(self):
        data = self.username