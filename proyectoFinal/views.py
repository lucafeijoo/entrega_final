from django.http import HttpResponse


def inicio(request):

        return HttpResponse("vista inicio")

def nosotros(request):

        return HttpResponse("vista nosotros")

def blogs(request):

        return HttpResponse("vista blogs")