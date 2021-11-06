"""massage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import (IndexView,StoreView,ProductsView,AboutView)

app_name = "massage_app"

urlpatterns = [
    path('index/', IndexView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('products/', ProductsView.as_view(), name="products"),
    path('store/', StoreView.as_view(), name="store"),
]
