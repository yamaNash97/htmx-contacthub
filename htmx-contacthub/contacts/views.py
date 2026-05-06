from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import contactForm


@login_required
def index(request):
    contacts = request.user.contacts.all().order_by('-date')
    context = {
        'contacts': contacts,
        'form': contactForm()       
               }
    return render(request, 'contacts.html', context)

@login_required
def search_contacts(request):
    import time
    time.sleep(1)
    query = request.GET.get('search', '')
    
    contacts = request.user.contacts.filter(
        Q(name__icontains= query) | Q(email__icontains=query)
    )
    return render(request, 'partials/contact-list.html', {'contacts': contacts} )