from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('user/<int:pk>/todo_update/', views.TodoUpdate.as_view(), name='todo_update'), #user_updateをパクった
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
=======
>>>>>>> d891c40e96f881be5f33d49dd208f6eb01df42fb
]
