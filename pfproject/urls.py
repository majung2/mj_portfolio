from django.contrib import admin
from django.urls import path
import portfolio.views # portfolio에 있는 views.py파일을 불러온다.

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',portfolio.views.home,name="home"),
    path('firstpage/',portfolio.views.firstpage,name="firstpage"),
    path('secondpg/',portfolio.views.secondpg,name="secondpg"),
    path('new/',portfolio.views.new,name="new"),
    path('youtube/',portfolio.views.youtube, name="youtube"),
]
