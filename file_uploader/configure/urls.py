from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('aws', views.aws_uploader),
    path('drive', views.googledrive_upload),
    path('dropbox', views.dropbox_uploader)

]