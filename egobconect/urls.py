from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
    path('reportessolicitudes/', include("reportessolicitudes.urls"), name='reportessolicitudes'),
    path('iniciarsesionciudadano/', views.custom_login ,name='iniciarsesionciudadano' ),
    path('cerrarsesion/', views.custom_logout, name='cerrarsesion'),
    path('reseteo-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register , name='register'),
    path('iniciarsesionfuncionario/',  views.login_funcionario_view , name='iniciarsesionfuncionario'),
    path('iniciarsesionadmin/', views.admin_login , name='iniciarsesionadmin'),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)