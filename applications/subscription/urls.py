from django.conf.urls import url
from applications.subscription import views


app_name = 'subscription'
urlpatterns = [
    url(r'^newsletter', views.SubscriberView.as_view(), name='newsletter'),
]
