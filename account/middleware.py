from django.http import HttpResponseForbidden
from django.urls import reverse

class ApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Exclude Django admin URLs
        admin_url = reverse('admin:index')
        if request.path == admin_url:
            return self.get_response(request)

        # Check if user is authenticated and if they are not approved
        if request.user.is_authenticated:
            if not getattr(request.user, 'is_approved', False):
                restricted_urls = ['/admin/', '/employee/']  # Add URLs to restrict
                if request.path in restricted_urls:
                    return HttpResponseForbidden("Your account is not approved yet.")
        
        return self.get_response(request)