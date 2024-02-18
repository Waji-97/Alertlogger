from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not path.startswith('login/') and not path.startswith('admin/'):
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        response = self.get_response(request)
        return response