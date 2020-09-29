from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^api/crud_app$', views.alllist),
    url(r'^api/crud_app/(?P<pk>[0-9]+)$', views.details_list),
]