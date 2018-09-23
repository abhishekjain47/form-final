from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect:
            return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
            return render(request, 'form1.html', {'form': form})
    else:
        return render(
            request,
            'form1.html',
            #context
        )
