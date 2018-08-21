from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path(
        "", 
        view = views.Image.as_view() , 
        name="list"
    ),
    path(
        "create/", 
        view = views.CreateImage.as_view() ,
        name = "Create_Image"
    )
]

