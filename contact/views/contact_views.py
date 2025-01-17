from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def index(request):
    contact = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contact,
    }    

    return render(
        request,
        'contact/index.html',
        context,
        )