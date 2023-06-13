from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    # path('register/',views.register,name='user-register'),
    path('register/', views.RegisterView.as_view(), name='user-register'),

    path('login/',views.MyLoginView.as_view(),name="user-login"),
    path('logout/',views.MyLogoutView.as_view(),name="user-logout"),
    path('profile/',views.ProfileView,name="user-profile"),
    path('editprofile/',views.EditProfileView.as_view(),name="user-editprofile"),
    
    path('user-apartment/<int:apartment_id>/', views.user_apartment_detail, name='user-apartment-detail'),
]
