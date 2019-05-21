from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
#return HttpResponse('Bem-vindo ao Connectedin')

@login_required
def index(request):
    # OBRIGATORIAMENTE DEVE POSSUIR PAGINA TEMPLATES
    # CHAMA PAGINA WEB NA PASTA TEMPLATES
    return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir(request, perfil_id):    
    # OBRIGATORIAMENTE DEVE POSSUIR PAGINA TEMPLATES
    # CHAMA PAGINA WEB NA PASTA TEMPLATES
    
    # Printa valor recebido
    # print ('ID recebido: ', perfil_id)

    # CHAMA CLASSE
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {"perfil" : perfil, "ja_eh_contato" : ja_eh_contato})

@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

@login_required
def get_perfil_logado(request):
    return request.user.perfil




"""
BUSCA DUAS INFORMACOES
perfis = Perfil.objects.get(nome='Steve', email='steve@minecraft.com')

BUSCA TUDO QUE CONTEM NO EMAIL
perfis = Perfil.objects.filter(email__contains='s')

Se quisermos buscar independente do letra maiúscula e minúscula usamos icontains:
perfis = Perfil.objects.filter(email__icontains='s')

E se quisermos que o email comece com um s:
perfis = Perfil.objects.filter(email__startswith='s')

if perfil_id == '1':
    perfil = Perfil('Joao', 'Joao@gmail.com', '77777', 'Top')
elif perfil_id == '2':
    perfil = Perfil('Maria', 'Maria@gmail.com', '8888', 'Top')
"""