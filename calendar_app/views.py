from django.http import JsonResponse
from .models import Calendar

def calendar_view(request):
    calendar_entry = Calendar.objects.last() or Calendar.objects.create(date='2025-02-27')
    data = {
        'year': calendar_entry.date.year,
        'month': calendar_entry.date.month,
        'day': calendar_entry.date.day,
    }
    return JsonResponse(data)