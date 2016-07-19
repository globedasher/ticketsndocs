"""tickets app urls.py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

# The following app_name provides a name to reference in the namespace...
# or something. I'm still learning Django.
app_name = "tickets"
urlpatterns = [
    url(r'^$', views.TicketIndex.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
    url(r'^create/$', views.CreateTicket.as_view(), name='create'),
    #url(r'^admin/', admin.site.urls),
    ]
