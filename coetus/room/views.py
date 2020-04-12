from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def demo(request):
    return render(request=request , template_name='pages/demo.html' )

def landing(request):
    return render(request=request , template_name='pages/landing.html' )


# Create your views here.
