from django.views import generic 
from .models import Post 
from rest_framework import viewsets 
from .serializers import PostSerializer 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib import messages

class PostList(generic.ListView): 
    queryset = Post.objects.filter(status=1).order_by('-created_on') 
    template_name = 'index.html' 
 
class PostDetail(generic.DetailView): 
    model = Post 
    template_name = 'post_detail.html' 
    
class PostViewSet(viewsets.ModelViewSet): 
    serializer_class = PostSerializer 
    queryset = Post.objects.all()     
    
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )    