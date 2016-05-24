from django.conf.urls import url
from views import GroupView, SpecialityView

urlpatterns = [
    url(r'^group/(?P<pk>\d+)/$', GroupView.as_view(), name='group'),
    # url(r'^bachelor/$', GroupView.as_view(), name='speciality', {'level': 'bachelor',})
    # url(r'^magister/$', GroupView.as_view(), name='speciality', {'level': 'magister',})
    url(r'^(?P<level>bachelor|magister)/$', SpecialityView.as_view(), name='speciality')
]
