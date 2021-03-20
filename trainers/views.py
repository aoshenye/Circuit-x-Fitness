from django.shortcuts import render, get_object_or_404
from .models import Trainer

# Create your views here.

def all_trainers(request):
    """ show all trainers """

    trainers = Trainer.objects.all()

    context = {
        'trainers': trainers,
    }

    return render(request, 'trainers/trainers.html', context)


def trainer_detail(request, trainer_id):
    """ A view to show individual product details """

    trainer = get_object_or_404(Trainer, pk=trainer_id)

    context = {
        'trainer': trainer,
    }

    return render(request, 'trainers/trainer_detail.html', context)