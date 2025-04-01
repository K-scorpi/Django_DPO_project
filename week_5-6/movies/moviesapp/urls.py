from django.urls import path, include
from . import views

#urlpatterns = [ path('admin/', admin.site.urls),]
urlpatterns = [
    path ("", views.MoviesView.as_view()),
]