from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import room , file

@login_required
def demo(request):
    return render(request=request , template_name='pages/demo.html' )

def landing(request):

    qs_f=  file.objects.all()
    return render(request=request , template_name='pages/landing.html' , context={'files':qs_f} )


# Create your views here.
