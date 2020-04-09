from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),
    path('create/',views.PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name='post_delete'),
    path('update/<int:pk>',views.PostUpdateView.as_view(),name='post_update')


]