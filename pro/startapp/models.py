from django.db import models

from django.utils import timezone

# Create your models here.
class Post(models.Model):
  #.ForeignKey('auth.User', on_delete = models.CASCADE) #on_delete->삭제 방법 (전부 삭제or부분 삭제 등등)cascade는 참조된 모든 키 삭제
     author = models.CharField(max_length=200)
     title = models.CharField(max_length=200)
     content= models.TextField()
     create_date=models.DateTimeField(
         default = timezone.now()
    )
