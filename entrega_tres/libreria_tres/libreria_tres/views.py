from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    saludo = "Bienvenida/o a la libreria virtual"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_html(request):
    http_response = render(
        request=request,
        template_name="base.html",
        context={},
    )
    return http_response
     
