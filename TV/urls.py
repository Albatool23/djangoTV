
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index),
    path('createShow',views.create),
    path('<_id>',views.delete),
     path('edit/<_id>',views.edit,name="edit_tvshow"),
     path('disply/<_id>', views.disply)
]