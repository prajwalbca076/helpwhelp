from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login),
    path('', include('schoolproject.url')),
    path('admin/', admin.site.urls),
]
