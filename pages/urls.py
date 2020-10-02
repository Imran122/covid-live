from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('index_save/', views.index_save, name='index_save'),
	path('result/', views.result, name='result'),
	path('test_list/', views.test_list, name='test_list')


]
