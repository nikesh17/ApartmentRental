from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from django.views import View
from django.urls import reverse_lazy
from tenant.models import Apartment, UserPreferences
from .models import Support, UserApartment, Book, Rent
from . forms import  SupportForm
from . models import User, Rent, User,UserApartment,Book
from django.urls import reverse
from django.db.models import Q
from django.db import IntegrityError
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# Create your views here.




    
# class ListingView(ListView):
#     model = Apartment
#     template_name = 'dashboard/listing.html'
#     context_object_name = "apartment"



# class ListingView(ListView):
#     model = Apartment
#     template_name = 'dashboard/listing.html'
#     context_object_name = "apartment"

#     def get_queryset(self):
#         # Get all apartments
#         queryset = super().get_queryset()

#         # Get the search query from the request parameters
#         search_query = self.request.GET.get('search')

#         # If a search query is provided, filter the apartments based on the search query
#         if search_query:
#             queryset = queryset.filter(
#                 Q(location__icontains=search_query) | 
#                 Q(apartment_id__icontains=search_query)
#             )

#         # Get the list of apartment IDs from the UserApartment model
#         excluded_apartment_ids = UserApartment.objects.values_list('apartment_id', flat=True)

#         # Exclude the apartments that have corresponding entries in UserApartment model
#         queryset = queryset.exclude(id__in=excluded_apartment_ids)

#         return queryset




class ListingView(ListView):
    model = Apartment
    template_name = 'dashboard/listing.html'
    context_object_name = "apartment"

    def get_queryset(self):
        # # Get all apartments
        queryset = super().get_queryset()

        # Get the list of apartment IDs from the UserApartment model
        excluded_apartment_ids = UserApartment.objects.values_list('apartment_id', flat=True)

#         # Filter the queryset to include only apartments not in UserApartment model
        queryset = queryset.exclude(id__in=excluded_apartment_ids)
        
        # Get the search query from the request parameters
        search_query = self.request.GET.get('search')
        location = self.request.GET.get('location')
        floor = self.request.GET.get('floor')
        bhk = self.request.GET.get('bhk')
        max_price = self.request.GET.get('price')

        # If a search query is provided, filter the apartments based on the search query
        if search_query:
            queryset = queryset.filter(
                Q(location__icontains=search_query) |
                Q(floor__icontains=search_query)|
                Q(bhk__icontains=search_query)|
                Q(apartment_id__icontains=search_query)
            )

        # Filter by location
        if location:
            queryset = queryset.filter(location=location)

        # Filter by maximum price
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        if floor:
            queryset = queryset.filter(floor=floor)
            
        if bhk:
            queryset = queryset.filter(bhk=bhk)

        return queryset
    
    


def apartment_details(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    booked_apartments = get_object_or_404(Apartment, id=apartment_id)

    # apartment = recommend_apartments(request,apartment_id)
    # print(apartment)
    return render(request, 'dashboard/apartment_details.html', {'apartment': apartment,'booked_apartments':booked_apartments})


# class ComplaintView(CreateView):
#     form_class = ComplaintForm
#     template_name= 'dashboard/complaint.html'
#     success_url = reverse_lazy('dashboard:dashboard-dashboard-listing')
    
class SupportView(CreateView):
    form_class = SupportForm
    template_name= 'dashboard/complaint.html'
    success_url = reverse_lazy('dashboard:dashboard-dashboard-listing')

def removeComplaint(request,pk):
    complaint = get_object_or_404(Support, pk=pk)
    complaint.delete()
    return redirect('tenant:tenant-complaint-list')

class BookView(View):
    def get(self, request, apartment_id=None, username=None):
        if apartment_id and username:
            try:
                apartment = get_object_or_404(Apartment, id=apartment_id)
                user = get_object_or_404(User, username=username)
                book = Book(username=user, apartment_id=apartment)
                book.save()
                return redirect(reverse('user:book-success'))
            except IntegrityError:
                return redirect(reverse('user:book-fail'))

def removeBooked(request,pk):
    booked = get_object_or_404(Book, pk=pk)
    booked.delete()
    return redirect('tenant:tenant-book')




class RentView(View):
    def get(self, request, apartment_id=None, username=None):
        if apartment_id and username:
            try:
                apartment = get_object_or_404(Apartment, id=apartment_id)
                user = get_object_or_404(User, username=username)
                rent = Rent(username=user, apartment_id=apartment)
                rent.save()
                return redirect(reverse('user:rent-success'))
            except IntegrityError:
                return redirect(reverse('user:rent-fail'))


def removeRented(request,pk):
    rented = get_object_or_404(Rent, pk=pk)
    rented.delete()
    return redirect('tenant:tenant-rent')




# def recommend_apartments(request, apartment_id):
#     user = request.user
#     apartment = get_object_or_404(Apartment ,pk=apartment_id)
#     print(apartment)
#     price = apartment.price
#     print(price)
#     location = apartment.location
#     bhk = apartment.bhk
#     floor = apartment.floor
    
#     return apartment
    price = apartment.price
    location = apartment.location
    bhk = apartment.bhk
    floor = apartment.floor
    description = apartment.description
    

    # context = {
    #     'id': id,
    #     'location': location,
    #     'price': price,
        
    #     'bhk': bhk,
    #     'floor': floor,
    #     'description': description,
        
    #     # Add other variables to the context as needed
    # }

    # # Get the user's preferences
    # user_location = location
    # user_price = price
    # user_bhk = bhk
    # user_floor = floor
    # # user_description = description


    # # Retrieve the selected apartment
    # selected_apartment = get_object_or_404(Apartment, apartment_id=apartment_id)

    # # Calculate the similarity between the selected apartment and all other apartments
    # apartment_scores = []
    # for apartment in Apartment.objects.exclude(apartment_id=apartment_id):
    #     apartment_attributes = ' '.join([
    #         apartment.location,
    #         str(apartment.price),
    #         apartment.bhk,
    #         apartment.floor,
    #         str(apartment.parking),

    #     ])
    #     user_attributes = ' '.join([
    #         user_location,
    #         str(user_price),
    #         user_bhk,
    #         user_floor,
    #         str(parking),

    #     ])
    #     attribute_list = [apartment_attributes, user_attributes]

    #     vectorizer = CountVectorizer().fit_transform(attribute_list)
    #     similarity_matrix = cosine_similarity(vectorizer)

    #     apartment_scores.append((apartment, similarity_matrix[0, 1]))

    # # Sort the apartments based on their similarity scores
    # sorted_apartments = sorted(apartment_scores, key=lambda x: x[1], reverse=True)

    # context = {
    #     'selected_apartment': selected_apartment,
    #     'recommended_apartments': [apartment for apartment, score in sorted_apartments],
    # }

    # return render(request, 'apartment_details.html', context)