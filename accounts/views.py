from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == "POST":#se o usuário enviar um formulário com os dados.
        user_form = UserCreationForm(request.POST)#criamos um formuláro com os dados que o usuário enviou
        if user_form.is_valid():#vaidamos pra ver se estar dentro dos requisitos de validação
            user_form.save()#usuário cadastrado no banco de dados
            return redirect('login')#redirecionado pra tela de login
    else:
        user_form = UserCreationForm()#criando um formulaŕio  vazio
    return render(request,'register.html',{'user_form': user_form})#envando para o template
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]#dados de usuário enviado
        password = request.POST["password"]#dados de senha enviado
        user = authenticate(request, username=username, password=password)#autenticando os dados enviados pelo o usuário
        if user is not None:#verificando se os dados não são nulos
            login(request, user)    #fazendo login
            return redirect('pipoca_list')#os dados sendo validos entra no site
        else:
            login_form = AuthenticationForm()#os dados não sendo validos retorna para o formulário em branco
    else:
        login_form = AuthenticationForm()#os dados não sendo validos retorna para o formulário em branco

    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('pipoca_list')