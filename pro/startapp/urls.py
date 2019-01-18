"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create_view),
    re_path(r'^createBoard$',views.post_create),
    re_path(r'^startapp/update/(?P<post_id>\d+)$',views.post_update_view,name="post_update_view"), 
    re_path(r'^startapp/show/(?P<post_id>\d+)$',views.post_view), 
    re_path(r'^updateBoard$',views.post_update),
    re_path(r'^startapp/delete/(?P<post_id>\d+)$',views.post_delete), 
]
