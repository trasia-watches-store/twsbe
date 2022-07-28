from django.urls import re_path, path, include
from . import views

urlpatterns = [
    # path('auth/', include('rest_auth.urls')),
    # url(r'^auth/register/', include('rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]