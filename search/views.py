from django.shortcuts import render
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET"])
def search(request):
    params = request.GET.copy()
    return render(request, 'search/index.html', {})



# Create your views here.
