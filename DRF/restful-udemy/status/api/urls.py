
"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    # StatusListSearchAPIView,
    StatusAPIView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
    StatusAPIDetailView)

urlpatterns = [

    # not generic views
    # path('', StatusListSearchAPIView.as_view()),


    # generic views
    # path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:pk>/', StatusDetailAPIView.as_view()),
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete/', StatusDeleteAPIView.as_view()),


    # two endpoints - generic views and mixins
    path('', StatusAPIView.as_view()),
    path('<int:pk>/', StatusAPIDetailView.as_view()),






]

# Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/1/ -> Detail
# /api/status/1/update -> Update
# /api/status/1/delete -> Delete

# End with
# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Final
# /api/status/ -> CRUD & LS
