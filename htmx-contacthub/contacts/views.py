from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods #only going to allow POST request
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

@login_required
@require_http_methods(['POST'])
def create_contact(request):
    form = contactForm(request.POST)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user 
        contact.save()
        #return partial containing a new row for our user
        #that we can add to the table
        context= {'contact' : contact}
        response = render(request, 'partials/contact-row.html', context)
        response['HX-Trigger']= 'Contact_added_successfuly'
        return response