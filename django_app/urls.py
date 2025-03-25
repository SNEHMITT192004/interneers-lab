# django_app/urls.py

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_name(request):
    """
    A simple view that returns 'Hello, {name}' in JSON format.
    Uses a query parameter named 'name'.
    """
    # Get 'name' from the query string, default to 'World' if missing
    name = request.GET.get("name", "World")
    return JsonResponse({"message": f"Hello, {name}!"})

from datetime import datetime

def get_datetime(request):
    """
    Returns the current date and time in JSON format.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({"current_datetime": current_time})

def get_user_info(request):
    """
    Accepts 'name' and 'age' as query parameters and returns them in JSON format.
    """
    name = request.GET.get("name", "Guest")
    age = request.GET.get("age", "Unknown")
    return JsonResponse({"name": name, "age": age})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_name), 
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
     path('datetime/', get_datetime),  # Now both APIs work!
     path('user/', get_user_info),
]
