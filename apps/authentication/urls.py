from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns  = [
    url(r'^$', views.index, name = "index"),
    url(r'^home$', views.home, name = "home"),
    url(r'^users$', views.users, name = "users"),
    url(r'^login$', views.login_view, name = "login"),
    url(r'^logout$', views.logout_view, name = "logout"),
    url(r'^register$', views.register, name = "register"),
]
