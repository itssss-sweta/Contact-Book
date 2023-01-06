from django.urls import path
from . import views

urlpatterns = [
    path('',views.saveinfo,name='saveinfo'),
    path('saveinfo',views.saveinfo,name='saveinfo'),
    path('index',views.index,name='index'),
    path('<int:id>/formupdate',views.formupdate,name='formupdate'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search')
]
