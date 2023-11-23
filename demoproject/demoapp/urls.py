from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.login_page,name='login'),
        path('login-check',views.login_check,name='login-check'),
        path('register',views.register,name='register'),
        path('register-data',views.register_data,name='register-data'),
        path('dashboard',views.dashboard,name='dashboard'),

        path('create-employee',views.create_employee,name='create-employee'),
        path('edit-employee',views.edit_employee,name='edit-employee'),
        path('edit-employee-action',views.edit_employee_action,name='edit-employee-action'),
        path('delete-employee/<int:id>',views.delete_employee,name='delete-employee'),

        path('logout', auth_views.LogoutView.as_view(), name="logout"),
    ]