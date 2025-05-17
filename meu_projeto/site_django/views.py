from django.shortcuts import render, redirect
from .models import Usuario, Produto
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import User

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

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                usuario = Usuario.objects.get(email=email)
                if usuario.senha == senha:
                    # Login bem-sucedido! Aqui você pode salvar na sessão:
                    request.session['usuario_id'] = usuario.id
                    request.session['usuario_nome'] = usuario.nome
                    return redirect('/projeto/')
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
    return render(request, 'site_django/index.html')  # A página principal do seu site, quando o usuário estiver logado
