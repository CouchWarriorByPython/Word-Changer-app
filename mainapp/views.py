from django.shortcuts import render
from django.views.generic import FormView
from django.http import FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp.forms import DocumentForm
from django.contrib.auth.models import User
from account.models import CustomUser


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
    return FileResponse(open('media/documents/2022/09/20/01999980_Договір__4109-E922-P000.pdf', 'rb'),
                        as_attachment=True)