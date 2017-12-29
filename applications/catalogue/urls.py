from django.conf.urls import url
from applications.catalogue import views


app_name = 'catalogue'
urlpatterns = [
    url(r'^', views.RelatedproductView.as_view(), name='related'),
]
