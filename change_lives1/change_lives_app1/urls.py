from django.contrib import admin
from django.urls import path
from change_lives_app1 import views
from change_lives1 import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='index'),
    path('about',views.aboutt,name='about'),
    path('contact',views.contactt,name='contact'),
    path('login',views.loginn,name='login'),
    path('logout',views.logoutt,name='logout'),
    path('signup',views.signupp,name='signup'),
    path('contact',views.contactt,name='contact'),
    path('payment',views.payment,name='p'),
    path('registration',views.registrationn,name='registration'),
    path('success',views.success,name='success'),
    path('fundraiser',views.fundraiser,name='fundraiser'),
    path('patient',views.patien,name='patient'),
    path('404',views.error404,name='404'),
    path('login_of_ngo',views.ngo_login,name='login_of_ngo')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)