from django.shortcuts import render, redirect
from .models import Usuario, Produto
from django.contrib import messages
from .forms import LoginForm

# Create your views here.

def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'site_django/product.html', {'produtos': produtos})


def registrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se o email já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'site_django/registrar.html', {
                'erro_email': 'Email já existente',
                'nome': nome,
                'email': email
            })

        # Criação do usuário
        Usuario.objects.create(nome=nome, email=email, senha=senha)
        return redirect('sucesso')

    return render(request, 'site_django/registrar.html')

def sucesso(request):
    return render(request, 'site_django/sucesso.html')


def login_view(request):
    erro = None
    sucesso = False

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
                    return render(request, 'site_django/login.html', {
                        'form': form,
                        'sucesso': True
                    })
                else:
                    erro = "Senha incorreta"
            except Usuario.DoesNotExist:
                erro = "Usuário não encontrado"
    else:
        form = LoginForm()

    return render(request, 'site_django/login.html', {'form': form, 'erro': erro})


def projeto(request):
    nome = request.session.get('usuario_nome')
    return render(request, 'site_django/index.html', {'usuario_nome': nome})

def logout_view(request):
    request.session.flush()  # limpa a sessão
    return redirect('/login/')