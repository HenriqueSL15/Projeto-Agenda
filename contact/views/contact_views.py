from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q
from django.http import Http404

# Create your views here.
def index(request):
    contact = Contact.objects.filter(show=True).order_by('id')

    paginator = Paginator(contact, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }    

    return render(
        request,
        'contact/index.html',
        context,
        )

def search(request):
    search_value = request.GET.get('q', '').strip()
    contact = Contact.objects.filter(show=True) \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)

        )\
        .order_by('id')
    
    paginator = Paginator(contact, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if search_value == "":
        return redirect('contact:index')

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }    

    return render(
        request,
        'contact/index.html',
        context,
        )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    single_contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    if single_contact is None:
        raise Http404()

    context = {
        'contact': single_contact,
        'site_title': single_contact_name
    }    

    return render(
        request,
        'contact/contact.html',
        context,
        )