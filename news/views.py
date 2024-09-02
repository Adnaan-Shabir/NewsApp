from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.conf import settings


def home(request):
    api_key = settings.NEWS_API_KEY  
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q=apple&from=2024-09-01&to=2024-09-01&sortBy=popularity&apiKey={api_key}")
        response.raise_for_status()  # Raises an error for bad responses 
        api = response.json()  # Directly using .json() instead of loading from content
    except requests.exceptions.RequestException as e:
        api = {"error": "Failed to retrieve news", "details": str(e)}

    return render(request, 'index.html', {'api': api})
