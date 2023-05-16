from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),

]