from django.shortcuts import render
from django.views.generic import FormView
from django.http import FileResponse

from mainapp.forms import DocumentForm


class DocumentView(FormView):
    form_class = DocumentForm
    template_name = 'mainapp/home.html'
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def success(request):
    return render(request, 'mainapp/success_page.html')


def download(request):
    return FileResponse(open('media/documents/2022/09/20/01999980_Договір__4109-E922-P000.pdf', 'rb'),
                        as_attachment=True)