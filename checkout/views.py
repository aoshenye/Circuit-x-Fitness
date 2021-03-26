from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IZ32hDrwFUAuTpufeaUSGj2R18yzRCpX0Lij5CxnPnKnnBhHTtrtlQDd87xk9wnwk7aTCyPbrqnTXNVXKPlo6C300vUNcgAik',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)