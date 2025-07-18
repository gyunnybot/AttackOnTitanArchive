from django.http.response import HttpResponseForbidden


def user_is_owner(function):
    def wrap(request, *args, **kwargs):
        if kwargs.get('pk') != request.user.pk:
            return HttpResponseForbidden("권한이 없습니다.")
        return function(request, *args, **kwargs)
    return wrap