from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connections
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

@login_required
def index(request):
    query = "select * from public.gen_pessoa where fl_ativo='S' and "
    # if request.GET.get('nome'):
    #     with connections['vwcontrol'].cursor() as cursor:
    #         cursor.execute(query+"lower(nm_pessoa) like '%"+request.GET['nome']+"%' order by nm_pessoa")
    #         trows = namedtuplefetchall(cursor)
    #     rows = request.GET['nome']
    #     return render(request, 'TGCMain/index.html', {"rows" : rows})
    # else:    
    #     return render(request, 'TGCMain/index.html', {})
    if request.method == 'GET':
        Nome = request.GET.get('nome')
        Cracha = request.GET.get('cracha')
        Matricula = request.GET.get('matricula')
        Identificador = request.GET.get('identificador')
        if Nome is None:
            Nome = ""
        if Cracha is None:
            Cracha = ""
        if Matricula is None:
            Matricula = ""
        if Identificador is None:
            Identificador = ""
        with connections['vwcontrol'].cursor() as cursor:
            cursor.execute(query+"lower(ds_Identificador_aux) like '%"+Identificador+"%' and lower(nm_pessoa) like '%"+Nome+"%' and cast(nr_cracha as text) like '%"+Cracha+"%' and cast(nr_matricula as text) like '%"+Matricula+"%'  order by nm_pessoa")
            rows = namedtuplefetchall(cursor)
        return render(request, 'TGCMain/index.html', {"rows" : rows})
    else:
        return render(request, 'TGCMain/index.html', {})