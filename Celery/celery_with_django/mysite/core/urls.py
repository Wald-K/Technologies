from django.urls import path

from . import views

urlpatterns = [
    # path('', views.get_all_users, name='users_list'),
    path('', views.UserListView.as_view(), name='users_list'),
    path('generate_users', views.GenerateRandomUserView.as_view(), name='generate_users'),

]