"""citasmedicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from citasmedicas import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from citas.views import Viendocitas, Insertarcita, Editcita, Elicita
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('vercita/', Viendocitas.as_view()),
    path('insertarcita/', Insertarcita.as_view()),
    path('editcita/<int:pk>/', Editcita.as_view()),
    path('elicita/<int:pk>/', Elicita.as_view()),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view()),
]   +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
