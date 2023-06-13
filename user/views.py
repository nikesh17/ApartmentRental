from  django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView,UpdateView
from . forms import UserForm, LoginForm,EditProfileForm
from dashboard.models import UserApartment
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User
from tenant.models import Apartment
# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user:user-login')
#     else:
#         form = UserForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'user/register.html', context)

# def login(request):
#     form =AuthenticationForm()
#     context ={
#         'form' : form
#     }
#     return render(request,'user/login.html',context)

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserForm
    success_url = reverse_lazy('user:user-login')
    
class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    
class MyLogoutView(LogoutView):
    next_page = reverse_lazy("user:user-login")
    
def ProfileView(request):
    try:
        user_apartment = UserApartment.objects.get(username=request.user)
    except UserApartment.DoesNotExist:
        user_apartment = None
    
    context = {
        'user': request.user,
        'apartment': user_apartment.apartment_id if user_apartment else None,
    }
    return render(request, 'user/profile.html', context)
    
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = EditProfileForm
    template_name = "user/editprofile.html"
    success_url = reverse_lazy("user:user-profile")

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)

def user_apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    return render(request, 'user/user_apartment_detail.html', {'apartment': apartment})