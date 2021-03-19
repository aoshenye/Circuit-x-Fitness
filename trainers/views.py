from django.shortcuts import render
from .models import Trainer

# Create your views here.
def all_trainers(request):
    """ show all trainers """

    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'trainers/trainers.html', context)

