# app_cadastro/views.py
from django.shortcuts import render, redirect
from .models import Cliente

def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')

        # Validação simples (pode ser mais complexa se necessário)
        if nome and email:  # Apenas 'nome' e 'email' são obrigatórios
            # Salva no banco de dados
            cliente = Cliente(nome=nome, email=email, telefone=telefone, endereco=endereco)
            cliente.save()

            # Redireciona para a página de sucesso ou outra página
            return redirect('sucesso')
        else:
            # Caso algum campo obrigatório esteja faltando
            return render(request, 'app_cadastro/forms.html', {'error': 'Nome e email são obrigatórios.'})
    
    return render(request, 'app_cadastro/forms.html')

def sucesso(request):
    return render(request, 'app_cadastro/sucesso.html')
