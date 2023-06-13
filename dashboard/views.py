from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.views import View
from django.urls import reverse_lazy
from tenant.models import Apartment
from tenant.views import ComplaintListView
from .models import Support, UserApartment, Book, Rent

from . forms import  SupportForm
from . models import User, Rent, User,UserApartment,Book
from django.urls import reverse
from django.views.generic import DetailView,DeleteView
# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')



    
# class ListingView(ListView):
#     model = Apartment
#     template_name = 'dashboard/listing.html'
#     context_object_name = "apartment"
class ListingView(ListView):
    model = Apartment
    template_name = 'dashboard/listing.html'
    context_object_name = "apartment"

    def get_queryset(self):
        # Get all apartments
        queryset = super().get_queryset()

        # Get the list of apartment IDs from the UserApartment model
        excluded_apartment_ids = UserApartment.objects.values_list('apartment_id', flat=True)

        # Exclude the apartments that have corresponding entries in UserApartment model
        queryset = queryset.exclude(id__in=excluded_apartment_ids)

        return queryset

def apartment_details(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    return render(request, 'dashboard/apartment_details.html', {'apartment': apartment})

# class ComplaintView(CreateView):
#     form_class = ComplaintForm
#     template_name= 'dashboard/complaint.html'
#     success_url = reverse_lazy('dashboard:dashboard-index')
    
class SupportView(CreateView):
    form_class = SupportForm
    template_name= 'dashboard/complaint.html'
    success_url = reverse_lazy('dashboard:dashboard-index')

def removeComplaint(request,pk):
    complaint = get_object_or_404(Support, pk=pk)
    complaint.delete()
    return redirect('tenant:tenant-complaint-list')

class BookView(View):
    def get(self, request, apartment_id=None, username=None):
        if apartment_id and username:
            apartment = get_object_or_404(Apartment, id=apartment_id)
            user = get_object_or_404(User, username=username)
            book = Book(username=user, apartment_id=apartment)
            book.save()
            return redirect(reverse('dashboard:dashboard-listing'))


def removeBooked(request,pk):
    booked = get_object_or_404(Book, pk=pk)
    booked.delete()
    return redirect('tenant:tenant-book')



class RentView(View):
    def get(self, request, apartment_id=None, username=None):
        if apartment_id and username:
            apartment = get_object_or_404(Apartment, id=apartment_id)
            user = get_object_or_404(User, username=username)
            rent = Rent(username=user, apartment_id=apartment)
            rent.save()
            return redirect(reverse('dashboard:dashboard-listing'))

def removeRented(request,pk):
    rented = get_object_or_404(Rent, pk=pk)
    rented.delete()
    return redirect('tenant:tenant-rent')
