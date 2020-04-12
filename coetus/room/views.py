from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import room

@login_required
def demo(request):
    return render(request=request , template_name='pages/demo.html' )

def landing(request):
    qs = room.objects.all()
    return render(request=request , template_name='pages/landing.html' , context={qs:'rooms'} )


# Create your views here.
