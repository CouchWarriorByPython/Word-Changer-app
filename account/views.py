from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/registration/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    template_name = 'account/registration/login.html'
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Авторизация'
        return context


class LogoutUser(LogoutView):
    template_name = 'account/registration/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Выход'
        return context


class UserProfileView(DetailView):
    template_name = 'account/registration/profile.html'
    context_object_name = 'profile'
    slug_field = 'user_uuid'
    slug_url_kwarg = 'user_id'
    queryset = CustomUser.objects.all()

