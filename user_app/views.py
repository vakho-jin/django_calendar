from django.http import JsonResponse
from .models import User

def user_view(request):
    user = User.objects.last() or User.objects.create(
        first_name='Djibril',
        last_name='Cisse',
        birth_date='1981-08-12'
    )
    data = {
        'First Name': user.first_name,
        'Last Name': user.last_name,
        'Age': user.age(),
    }
    return JsonResponse(data)