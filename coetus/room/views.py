from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin

from .models import room , file


@login_required
def demo(request):
    qs_f = file.objects.all()
    return render(request=request , template_name='pages/demo.html', context={'files':qs_f}  )

def landing(request):

    return render(request=request , template_name='pages/landing.html' )


# Create your views here.
