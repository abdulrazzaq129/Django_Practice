from django.urls import path, re_path
from . import views

urlpatterns = [
    path('product_detail/<str:product_name>/', views.product_detail, name='product_detail'),
    path('reverse_words/', views.reverse_words, name='reverse_words '),
    path('article_detail/<int:year>/<int:month>/<int:day>/', views.article_detail, name='article_detail'),
    path('', views.home, name='home'),
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article, name='article'),
    path('student/', views.student_list, name='student_list '),
    path('student_edit/<int:id>/', views.student_edit, name='student_edit '),


]
