from django.db import models

class Post(models.Model):
    lecture_name = models.TextField(max_length=100) # 강의 이름
    #lecture_img = models.ImageField()
    teacher = models.CharField(max_length=100) # 강사 
    #lecture_url = models.TextField(max_length=300) # 강의 사이트 주소
    price = models.IntegerField()  # 가격
    #platform = models.CharField(max_length=100) # 제공 플랫폼
    field = models.CharField(max_length=100) # 매핑 1~6 까지 


    
    
