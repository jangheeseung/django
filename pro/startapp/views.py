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
   url = "/createBoard"
   context = {'url': url}                
   return render(request,'startapp/form.html',context)    #/form.html,/create

def post_create(request):
   title= request.POST.get("title")
   content= request.POST.get("content")
   author=request.POST.get("author")
   post=Post(title=title,content=content,author=author)
   post.save()
   return HttpResponseRedirect("/")

def post_update_view(request, post_id):
   post = Post.objects.get(pk = post_id)
   url = "/updateBoard"
   context = {'post': post, 'url': url}
   return render(request, 'startapp/form.html', context)

def post_view(request,post_id):
   post = Post.objects.get(pk = post_id)  
   context = {'post': post} 
   return render(request, 'startapp/show.html', context)

def post_update(request):
   post_id = request.POST.get("post_id")
   title = request.POST.get("title")
   content = request.POST.get("content")
   post = Post.objects.get(pk = post_id)
   post.title = title
   post.content = content
   post.save()
   return HttpResponseRedirect("/")

def post_delete(request,post_id):
   post = Post.objects.get(pk = post_id)
   post.delete()
   return HttpResponseRedirect("/")
    

