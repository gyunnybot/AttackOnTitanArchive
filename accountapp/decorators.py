from django.http.response import HttpResponseForbidden


def account_ownership_required(function):
    def decorated(request, *args, **kwargs):
        if kwargs.get('pk') != request.user.pk:
            return HttpResponseForbidden()

        return function(request, *args, **kwargs)

    return decorated