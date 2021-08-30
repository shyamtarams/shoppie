from django.contrib.auth.models import User

def status(request):
    status=User.objects.get(username=request.user)
    print(status.last_name)
    if status.last_name=='dis':
        return 'dis'
    else:
        return 'true'
    
