from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, RegisterView, ProtectedView

urlpatterns = [
    # Главная страница с формой входа и регистрации
    path('', IndexView.as_view(), name='home'),
    
    # Вход (LoginView)
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Выход (LogoutView)
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
    # Регистрация (RegisterView)
    path('register/', RegisterView.as_view(), name='register'),
    
    # Защищенная страница
    path('protected/', ProtectedView.as_view(), name='protected'),
    ]