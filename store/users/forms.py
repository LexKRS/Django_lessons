from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta():
        model = User
        #Также можно вносить списком.
        #Указываем с какими полями будем работать в форме.
        fields = ('username', 'password')