from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def health_view(request):
    return JsonResponse({"ok": True })