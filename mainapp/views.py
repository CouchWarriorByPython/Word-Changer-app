from django.shortcuts import render
from django.views.generic import FormView
from django.http import FileResponse, HttpResponseServerError, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp.forms import DocumentForm
from .tools import check
from account.models import CustomUser
from .models import DocxModel


class DocumentView(LoginRequiredMixin, FormView):
    form_class = DocumentForm
    template_name = 'mainapp/home.html'
    success_url = 'success'

    def form_valid(self, form):
        custom_user = CustomUser.objects.get(user=self.request.user)
        form.instance.owner = custom_user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(user=self.request.user)
        context['user_uuid'] = user_id
        return context


def success(request):
    return render(request, 'mainapp/success_page.html')


def download(request):
    resp = check(request.user.username)
    answer = {'response': resp}
    if resp is None:
        query = DocxModel.objects.last()
        return FileResponse(open(query.document.path, 'rb'), as_attachment=True)
    else:
        return render(request, 'mainapp/errors/list_out.html', answer)