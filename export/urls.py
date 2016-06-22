from django.conf.urls import url
from views import AttendanceExport

urlpatterns = [
    url(r'^group/(?P<pk>\d+)/export/$', AttendanceExport.as_view(), name='group'),
]
