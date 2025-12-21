from django.shortcuts import render, redirect

# Create your views here.
from pipoca.models import Pipoca
from pipoca.forms import PipocaModelForm

def pipoca_view(request):
    pipoca = Pipoca.objects.all()
    return render(
        request,
        'pipoca.html',
        {'pipoca': pipoca}
    )

def new_pipoca_view(request):
    if request.method == 'POST':
        new_pipoca_form = PipocaModelForm(request.POST, request.FILES)
        if new_pipoca_form.is_valid():
            new_pipoca_form.save()
            return redirect('pipoca_list')
    else:
        new_pipoca_form = PipocaModelForm()
    return render(request, 'new_pipoca.html', {'new_pipoca_form': new_pipoca_form})