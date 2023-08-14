import os

#Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 
# settings.py파일 경로를 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dummy_drf.settings")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

import django
django.setup()

from post.models import Post

def parser():
    driver = webdriver.Chrome()
    url = 'https://www.inflearn.com/courses?s='
    li = ['django','spring','react','c언어','python','java']

    all_data = []

    for i in range(len(li)):
        newdic ={
            "lecture_name": "",
            #"lecture_img": "",
            "teacher": "",
        # "lecture_url": "",
            "price": "",
            #"platform": "",
            "field": "" #어떤 분야의 강의를 가져올 것인지 매핑 ex) django=1 , spring=2 ...
        }
        newurl = url + li[i]
        driver.get(newurl) # 접속

        #lecture_name
        name = driver.find_element(By.XPATH, '//*[@id="courses_section"]/div/div/div/main/div[4]/div/div[1]/div/a/div[2]/div[1]')
        newdic["lecture_name"] = name.text

        #price
        p = driver.find_element(By.XPATH,'//*[@id="courses_section"]/div/div/div/main/div[4]/div/div[1]/div/a/div[2]/div[4]')
        p = p.text
        pp = re.sub(r"[^0-9]",'', p) # 문자열에서 숫자만 골라내기
        newdic["price"]=pp
        
        #teacher
        teach =  driver.find_element(By.XPATH,'//*[@id="courses_section"]/div/div/div/main/div[4]/div/div[1]/div/a/div[2]/div[2]')
        newdic["teacher"] = teach.text

        newdic["field"]= i+1

        all_data.append(newdic)

    return all_data


if __name__=='__main__':
    data_dict = parser()
    
    for i in range(len(data_dict)):
        dic = data_dict[i]

        n = dic['lecture_name']
        t = dic['teacher']
        p = dic['price']
        f = dic['field']
        
        Post(lecture_name=n, teacher=t, price=p, field=f).save()
        # for n, t, p, f in dic.items():
        #     Post(lecture_name=n, teacher=t, price=p, field = f).save()
    
