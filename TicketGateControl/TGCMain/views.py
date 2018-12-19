from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.db import connections
from collections import namedtuple
from django.contrib import messages
from django.http import HttpResponseRedirect

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()] 

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
    query = ("select * "
            "from public.gen_pessoa "
            "where fl_ativo='"+Ativo+"' "
            "and lower(ds_Identificador_aux) like '%"+Identificador.lower()+"%' "
            "and lower(nm_pessoa) like '%"+Nome.lower()+"%' "
            "and cast(nr_cracha as text) like '%"+Cracha+"%' "
            "and cast(nr_matricula as text) like '%"+Matricula+"%' "
            "order by nm_pessoa")
    with connections['vwcontrol'].cursor() as cursor:
            cursor.execute(query)
            rows = namedtuplefetchall(cursor)
    return render(request, 'TGCMain/index.html', {"rows" : rows})

def tipos():
    with connections['vwcontrol'].cursor() as cursor:
        cursor.execute("SELECT ds_Identificador_aux from public.gen_pessoa where fl_ativo='S' group by ds_Identificador_aux order by ds_Identificador_aux ")
        return namedtuplefetchall(cursor)

@login_required
def edit(request):
    if request.method == "GET":
        if request.GET.get('cracha') != '' and request.GET.get('ativo') != '' and request.GET.get('matricula') != '':
            crachaG = request.GET.get('cracha')
            ativoG = request.GET.get('ativo')
            matriculaG = request.GET.get('matricula')
        else:
            messages.error(request, 'Falha na atualização, refaça a pesquisa na tela inicial')
            return render(request, 'TGCMain/edit.html')
        queryGet = ("select * "
                "from public.gen_pessoa "
                "where fl_ativo='"+ativoG+"' "
                "and nr_cracha="+crachaG+" "
                "and nr_matricula="+matriculaG)
        with connections['vwcontrol'].cursor() as cursor:
            cursor.execute(queryGet)
            row = namedtuplefetchall(cursor)
        tipo = tipos()
        return render(request, 'TGCMain/edit.html', {"row":row,"tipo":tipo}) 
            
    if request.method == "POST":
        identificadorP=request.POST.get('identificador')
        nomeP=request.POST.get('nome')
        crachaP=request.POST.get('cracha')
        matriculaP=request.POST.get('matricula')
        ativoP=request.POST.get('ativo')
        crachaG=request.GET.get('cracha')
        matriculaG=request.GET.get('matricula')
        if identificadorP == '' or nomeP == '' or crachaP == '' or matriculaP == '' or ativoP == '':
            messages.error(request, 'Falha na atualização, está faltando informações')
        else:
            queryPostCracha = ("select * "
                "from public.gen_pessoa "
                "where nr_cracha="+crachaP)
            queryPostMatricula =("select * "
                "from public.gen_pessoa "
                "where nr_matricula="+matriculaP)    
            with connections['vwcontrol'].cursor() as cursor:
                try:
                    cursor.execute(queryPostCracha)
                    rowCracha = namedtuplefetchall(cursor)
                    cursor.execute(queryPostMatricula)
                    rowMatricula = namedtuplefetchall(cursor)
                    #atualiza todos os dados
                    if not rowCracha:
                        if not rowMatricula:
                            cursor.execute("update public.gen_pessoa "
                                            "set ds_Identificador_aux='"+identificadorP.upper()+"', "
                                            "nm_pessoa='"+nomeP.upper()+"', "
                                            "nr_cracha='"+crachaP+"', "
                                            "nr_matricula='"+matriculaP+"', "
                                            "fl_ativo='"+ativoP+"' "
                                            "where nr_cracha='"+crachaG+"'")
                            messages.success(request, 'Cadastro atualizado')
                            return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaP+'&matricula='+matriculaP+'&ativo='+ativoP)
                        #Atualiza Cracha    
                        else:
                            cursor.execute("update public.gen_pessoa "
                                            "set ds_Identificador_aux='"+identificadorP.upper()+"', "
                                            "nm_pessoa='"+nomeP.upper()+"', "
                                            "nr_cracha='"+crachaP+"', "
                                            "fl_ativo='"+ativoP+"' "
                                            "where nr_cracha='"+crachaG+"'")
                            messages.success(request, 'Cadastro atualizado')
                            return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaP+'&matricula='+matriculaG+'&ativo='+ativoP)
                    #Atualiza Matricula
                    else:
                        if not rowMatricula:
                            cursor.execute("update public.gen_pessoa "
                                            "set ds_Identificador_aux='"+identificadorP.upper()+"', "
                                            "nm_pessoa='"+nomeP.upper()+"', "
                                            "nr_matricula='"+matriculaP+"', "
                                            "fl_ativo='"+ativoP+"' "
                                            "where nr_cracha='"+crachaG+"'")
                            messages.success(request, 'Cadastro atualizado')
                            return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaG+'&matricula='+matriculaP+'&ativo='+ativoP)
                        #Atualiza outros dados
                        else:
                            if crachaP == crachaG and matriculaP == matriculaG:
                                cursor.execute("update public.gen_pessoa "
                                            "set ds_Identificador_aux='"+identificadorP.upper()+"', "
                                            "nm_pessoa='"+nomeP.upper()+"', "
                                            "fl_ativo='"+ativoP+"' "
                                            "where nr_cracha='"+crachaG+"'")
                                messages.success(request, 'Cadastro atualizado')
                                return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaG+'&matricula='+matriculaG+'&ativo='+ativoP)
                            else:
                                messages.error(request, 'Cracha ou Matricula já existem não é possível alterar')
                                return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaG+'&matricula='+matriculaG+'&ativo='+ativoP)
                except:
                    messages.error(request, 'Houve problema na alteração do cadastro')
                    return HttpResponseRedirect(reverse('edit') + '?cracha='+crachaG+'&matricula='+matriculaG+'&ativo='+ativoP)
        messages.error(request, 'Algo deu errado, tente novamente')
        return render(request, 'TGCMain/edit.html')
    return render(request, 'TGCMain/index.html') 

@login_required
def insert(request):
    tipo = tipos()
    if request.method == "POST":
        identificadorP=request.POST.get('identificador')
        nomeP=request.POST.get('nome')
        crachaP=request.POST.get('cracha')
        matriculaP=request.POST.get('matricula')
        ativoP=request.POST.get('ativo')

        if identificadorP == '' or nomeP == '' or crachaP == '' or matriculaP == '' or ativoP == '':
            messages.error(request, 'Falha no cadastro, está faltando informações')
        else:
            queryPostCracha = ("select * "
                "from public.gen_pessoa "
                "where nr_cracha="+crachaP)
            queryPostMatricula =("select * "
                "from public.gen_pessoa "
                "where nr_matricula="+matriculaP)    
            with connections['vwcontrol'].cursor() as cursor:
                try:
                    cursor.execute(queryPostCracha)
                    rowCracha = namedtuplefetchall(cursor)
                    cursor.execute(queryPostMatricula)
                    rowMatricula = namedtuplefetchall(cursor)
                    if not rowCracha and not rowMatricula:
                        cursor.execute("insert into public.gen_pessoa "
                                        "(id_pessoa,dt_atualizacao,tp_pessoa,"
                                        "ds_Identificador_aux,fl_ativo,fl_calcular,"
                                        "fl_comissionado,fl_funcionario,fl_lista_negra,"
                                        "fl_master,fl_verifica_digital,fl_visitante,"
                                        "nm_pessoa,nr_cracha,nr_matricula,"
                                        "tp_origem_cadastro,fl_aluno,fl_cadastra_digital,"
                                        "fl_refeicao,fl_responsavel,id_empresa) "
                                        "values ((select max(id_pessoa) from public.gen_pessoa)+1,(select current_timestamp),"
                                        "'0','"+identificadorP.upper()+"','"+ativoP+"',"
                                        "'S','N','S','N','N','S','N',"
                                        "'"+nomeP.upper()+"','"+crachaP+"','"+matriculaP+"',"
                                        "'SISTEMA','N','N','S','N','1')")
                        messages.success(request, 'Cadastro inserido com sucesso')
                    else:
                        messages.error(request, 'Cracha ou matricula já existem')
                except:
                    messages.error(request, 'Ocorreu um erro no cadastro, tente novemente')
    return render(request, 'TGCMain/insert.html', {"tipo":tipo})