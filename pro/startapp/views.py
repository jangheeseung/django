from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import Post #모델에 있는 post객체 가져오기 
# Create your views here.

def post_list(request):
   # return HttpResponse("Hello world!!")                                                  #하나를 불러 오려면 .get   
   posts = Post.objects.filter(create_date__lte = timezone.now()).order_by('create_date') #여러개는 .fillter .all()해도 전부 가져옴  
   context = {'posts': posts} 
   return render(request,'startapp/list.html',context)   

def post_create_view(request):                
   return render(request,'startapp/form.html')    #/form.html,/create

def post_create(request):
   title= request.POST.get("title")
   content= request.POST.get("content")
   author=request.POST.get("author")
   post=Post(title=title,content=content,author=author)
   post.save()
   return redirect('http://127.0.0.1:8000/')