from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response


def index(request):
    """
    View of the main page
    """
    return render(request, 'Index.html')


def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response
