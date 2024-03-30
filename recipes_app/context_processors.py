from django.contrib.auth.models import User

def user(request):
    return {
        'current_user': request.user
    }
