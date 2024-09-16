from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views import generic
from .models import Redmi
from .models import Comment
from .forms import RedmiForm
from .forms import CommentForm
# from django.contrib.auth import login
# from .forms import SignUpForm
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def some_view(request):
#     # Этот код будет доступен только для авторизованных пользователей
#     ...


#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Войти после регистрации
#             return redirect('list_view')  # Перенаправление на главную страницу
#     else:
#         form = SignUpForm()
#     return render(request, 'redmi/signup.html', {'form': form})
#




def post_detail(request, pk):
    post = get_object_or_404(Redmi, pk=pk)
    comments = post.comments.filter(approved=True)  # Получаем только одобренные комментарии
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post  # Привязываем комментарий к посту
            new_comment.author = request.user  # Указываем автора
            new_comment.save()
            return redirect('redmi_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'redmi_detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    })







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





def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")
