from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# 1. Главная страница
class IndexView(TemplateView):
    template_name = 'index.html'

# 2. Регистрация
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# 3. Защищенная страница 
@method_decorator(login_required, name='dispatch') 
class ProtectedView(TemplateView):
    template_name = 'protected.html'








