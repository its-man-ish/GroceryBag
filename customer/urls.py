from django.urls import path

from .views import*
urlpatterns = [
  path('myprofile/',MyProfile,name='myprofile'),
  path('signup/',UserSignupView.as_view(),name='signup'),

]