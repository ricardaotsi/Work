from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connections
from collections import namedtuple
from django.contrib import messages
from django.shortcuts import reverse, redirect
from django.http import HttpResponseRedirect

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def sql(Nome, Identificador, Cracha, Matricula, Ativo):
    query = "select * from public.gen_pessoa where fl_ativo='"+Ativo+"' and "
    with connections['vwcontrol'].cursor() as cursor:
            cursor.execute(query+"lower(ds_Identificador_aux) like '%"+Identificador.lower()+"%' and lower(nm_pessoa) like '%"+Nome.lower()+"%' and cast(nr_cracha as text) like '%"+Cracha+"%' and cast(nr_matricula as text) like '%"+Matricula+"%'  order by nm_pessoa")
            rows = namedtuplefetchall(cursor)
    return rows

def sql2(Cracha, Ativo):
    query = "select * from public.gen_pessoa where fl_ativo='"+Ativo+"' and "
    with connections['vwcontrol'].cursor() as cursor:
            cursor.execute(query+"nr_cracha="+Cracha)
            rows = namedtuplefetchall(cursor)
    return rows

@login_required
def index(request):
    if request.GET.get('nome') is None:
        Nome = ""
    else:
        Nome = request.GET.get('nome')
    if request.GET.get('cracha') is None or request.GET.get('cracha').isdigit() == False:
        Cracha = ""
    else:
        Cracha = request.GET.get('cracha')
    if request.GET.get('matricula') is None or request.GET.get('matricula').isdigit() == False:
        Matricula = ""
    else:
        Matricula = request.GET.get('matricula')
    if request.GET.get('identificador') is None:
        Identificador = ""
    else:
        Identificador = request.GET.get('identificador')
    if request.GET.get('ativo') is None:
        Ativo = "S"
    else:
        Ativo = request.GET.get('ativo')
    rows = sql(Nome, Identificador, Cracha, Matricula, Ativo )
    return render(request, 'TGCMain/index.html', {"rows" : rows})

@login_required
def edit(request):
    if request.method == "GET":
        if request.GET.get('cracha') != '' or request.GET.get('ativo') != '':
            row = sql2(request.GET.get('cracha'), request.GET.get('ativo'))   
    if request.method == "POST":
        ide=request.POST.get('identificador')
        n=request.POST.get('nome')
        c=request.POST.get('cracha')
        m=request.POST.get('matricula')
        a=request.POST.get('ativo')
        with connections['vwcontrol'].cursor() as cursor:
            try:
                cursor.execute("update public.gen_pessoa set ds_Identificador_aux='"+ide.upper()+"', nm_pessoa='"+n.upper()+"', nr_cracha='"+c+"', nr_matricula='"+m+"', fl_ativo='"+a+"' where nr_cracha='"+request.GET.get('cracha')+"'")
                messages.success(request, 'O cadastro foi atualizado')
                return HttpResponseRedirect(reverse('edit') + '?cracha='+c+'&ativo='+a)
            except:
                messages.error(request, 'Ocorreu um erro na atualização')
                row = sql2(request.GET.get('cracha'), request.GET.get('ativo'))
    return render(request, 'TGCMain/edit.html', {"row":row}) 