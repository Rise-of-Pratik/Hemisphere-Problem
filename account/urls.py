from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.Login.as_view(), name='account-login'),
    url(r'^logout/', views.Logout.as_view(), name='account-logout'),
]