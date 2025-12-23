from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register_view(request):
    user_form = UserCreationForm()#criando o form
    return render(
        request,
        'register.html',
        {'user_form': user_form}#envando para o template
    )
    