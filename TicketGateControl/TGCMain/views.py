from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connections


@login_required
def index(request):
    with connections['vwcontrol'].cursor() as cursor:
        cursor.execute("select * from public.gen_pessoa where fl_ativo='S'")
        rows = cursor.fetchall()
    return render(request, 'TGCMain/index.html', {"rows" : rows})
