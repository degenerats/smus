from django.conf.urls import url
from views import GroupView

urlpatterns = [
    url(r'^group/(?P<pk>\d+)/$', GroupView.as_view(), name='group'),
]
