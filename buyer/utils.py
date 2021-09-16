# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def status(request):
    User = get_user_model()
    status=User.objects.get(username=request.user)
    print(status.status)
    if status.status=='Disabled':
        return 'Disabled'
    else:
        return 'true'
    
