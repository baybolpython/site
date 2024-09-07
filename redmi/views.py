from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import generic
from .models import Redmi
from .forms import RedmiForm
#
#
# def update_phone_view(request, id):
#     phone = get_object_or_404(Redmi, id=id)
#     if request.method == 'POST':
#         form = RedmiForm(request.POST, instance=phone)
#         if form.is_valid():
#             form.save()
#             return redirect('list_view')
#     else:
#         form = RedmiForm(instance=phone)
#     return render(request, 'redmi/update_phone.html', {'form': form})
#
#
#
#
# def delete_phone_view(request, id):
#     phone = get_object_or_404(Redmi, id=id)
#     phone.delete()
#     return redirect('list_view')
#
#
#
# def create_phone_view(request):
#     if request.method == 'POST':
#         form = RedmiForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list_view')
#     else:
#         form = RedmiForm()
#     return render(request, 'redmi/create_phone.html', {'form': form})
#
#
# def details_view(request, id):
#     if request.method == 'GET':
#         redmi_id = get_object_or_404(Redmi, id=id)
#         return render(request, 'redmi/redmi_details.html', {'redmi_id': redmi_id})

class Redmi_list_view(generic.ListView):
    template_name = 'redmi/redmi_list.html'
    context_object_name = 'redmis'
    model = Redmi

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class Redmi_details_view(generic.DetailView):
    template_name = 'redmi/redmi_details.html'
    context_object_name = 'redmi_id'

    def get_object(self, **kwargs):
        redmi_id = self.kwargs.get('id')
        return get_object_or_404(Redmi, id=redmi_id)



class Redmi_create_view(generic.CreateView):
    template_name = 'redmi/create_phone.html'
    form_class = RedmiForm
    success_url = '/list_view/'

    def form_valid(self, form):
        form.save()
        return super(Redmi_create_view, self).form_valid(form=form)

class Redmi_delete_view(generic.DeleteView):
    template_name = 'redmi/delete_redmi.html'
    success_url = '/list_view/'

    def get_object(self, **kwargs):
        redmi_id = self.kwargs.get('id')
        return get_object_or_404(Redmi, id=redmi_id)


class Redmi_update_view(generic.UpdateView):
    template_name = 'redmi/update_phone.html'
    form_class = RedmiForm
    success_url = '/list_view/'
    def get_object(self, **kwags):
        redmi_id = self.kwargs.get('id')
        return get_object_or_404(Redmi, id=redmi_id)
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Redmi_update_view, self).form_valid(form=form)




# def list_view(request):
#     if request.method == 'GET':
#         redmis = Redmi.objects.all()
#         return render(request, 'redmi/redmi_list.html', {'redmis': redmis})


def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")



