from django.shortcuts import render, redirect
from .models import Usuario, Produto
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'site_django/product.html', {'produtos': produtos})


def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Aqui você poderia validar ou criptografar a senha
        Usuario.objects.create(nome=nome, email=email, senha=senha)
        return redirect('sucesso')
    
    return render(request, 'site_django/registrar.html')

def sucesso(request):
    return render(request, 'site_django/sucesso.html')

def login_view(request):
    erro = None
    sucesso = False  # Novo

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                usuario = Usuario.objects.get(email=email)
                if usuario.senha == senha:
                    request.session['usuario_id'] = usuario.id
                    request.session['usuario_nome'] = usuario.nome
                    sucesso = True
                    return render(request, 'site_django/index.html', {'form': form, 'sucesso': sucesso})
                else:
                    erro = "Senha incorreta"
            except Usuario.DoesNotExist:
                erro = "Usuário não encontrado"
    else:
        form = LoginForm()

    return render(request, 'site_django/login.html', {'form': form, 'erro': erro})


from django.contrib.auth.decorators import login_required

@login_required
def projeto(request):
    try:
        # Busca o usuário pelo email (assumindo que seja igual no auth_user e Usuario)
        usuario_logado = Usuario.objects.get(email=request.user.email)
        nome = usuario_logado.nome
    except Usuario.DoesNotExist:
        nome = request.user.username  # fallback

    return render(request, 'site_django/index.html', {'usuario_nome': nome})