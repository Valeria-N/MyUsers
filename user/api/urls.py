from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'users'

router = routers.SimpleRouter()

router.register(r'users', UserListView)
#router.register(r'login', get_login_my, basename='MyLogin')


urlpatterns = [
    path('', include(router.urls)),
    path('current_user/',
         CurrentUserView.as_view(),
         name='Current_user'),
    path('login/',
         my_view,
         name='my_view'),
]