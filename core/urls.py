from django.conf.urls import url
from views import GroupView, SpecialityView, StaffView, StudentView

urlpatterns = [
    url(r'^group/(?P<pk>\d+)/$', GroupView.as_view(), name='group'),
    url(r'^staff/(?P<pk>\d+)/$', StaffView.as_view(), name='staff'),
    url(r'^student/(?P<pk>\d+)/$', StudentView.as_view(), name='student'),
    # url(r'^search/$', GroupView.as_view(), name='search'),
    # url(r'^bachelor/$', GroupView.as_view(), name='speciality', {'level': 'bachelor',})
    # url(r'^magister/$', GroupView.as_view(), name='speciality', {'level': 'magister',})
    url(r'^(?P<level>bachelor|magister)/$', SpecialityView.as_view(), name='speciality')
]
