from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",include("Home.urls")),
    path("courses/",include("Courses.urls")),
    path('admin/', admin.site.urls),
]
