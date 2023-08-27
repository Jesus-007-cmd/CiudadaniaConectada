from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroCiudadanoForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Los passwords no coinciden. Por favor, intenta nuevamente."
            )
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        if password1:
            username = cleaned_data.get("username")
            if username and password1.lower() == username.lower():
                self.add_error(
                    "password1",
                    "La contraseña no puede ser igual al nombre de usuario. "
                    "Asegúrate de que la contraseña sea lo suficientemente diferente."
                )
            elif password1.isdigit():
                self.add_error(
                    "password1",
                    "La contraseña no puede consistir en números solamente. "
                    "Asegúrate de incluir caracteres diferentes en tu contraseña."
                )
