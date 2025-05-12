
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

#urlpatterns = [ path('admin/', admin.site.urls),]
urlpatterns = [
    path ("", views.MoviesView.as_view()),
]