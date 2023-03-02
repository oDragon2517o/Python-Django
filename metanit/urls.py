"""metanit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from hello import views
 

product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]
 
#urlpatterns = [
#    path("", views.index1),
#    path("products/", include(product_patterns)),
#]


urlpatterns = [

    path("", views.index),
    #path('', views.index),
    path("", views.index),
    path("products/<int:id>/", include(product_patterns)),


    path("index", views.index),
    path("error", views.error),
    path("txt", views.txt),
    #path('about', views.about, kwargs={"name":"Tom", "age": 38}),
    #re_path(r'^contact', views.contact),
    #path("user", views.user),
    #path("user/<name>", views.user),
    #path("user/<name>/<int:age>", views.user),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    #re_path(r"^user", views.user),

    ###########
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),



    path("user/", views.user3),

    path('Hello', views.Hello),


    ################################
    path("index20", views.index20),
]
