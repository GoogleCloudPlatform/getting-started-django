from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, managed VMs.")

def healthcheck(request):
    return HttpResponse("ok")
