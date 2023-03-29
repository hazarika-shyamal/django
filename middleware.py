from django.shortcuts import redirect


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = '/'  # Make sure this is set correctly

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path == '/home/':
            return redirect(self.login_url)

        # Continue with the request/response cycle
        response = self.get_response(request)
        return response
