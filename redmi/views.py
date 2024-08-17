from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Redmi


def details_view(request, id):
    if request.method == 'GET':
        redmi_id = get_object_or_404(Redmi, id=id)
        return render(request, 'redmi/redmi_details.html', {'redmi': redmi_id})



def list_view(request):
    if request.method == 'GET':
        redmis = Redmi.objects.all()
        return render(request, 'redmi/redmi_list.html', {'redmis': redmis})


def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")



