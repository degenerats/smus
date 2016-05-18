from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

class AuthRequiredMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated() and request.path != reverse('account:login') and not request.path.startswith('/admin/'):
            return HttpResponseRedirect(reverse('account:login')) # or http response
        return None
