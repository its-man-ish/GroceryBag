from django.urls import path

from .views import*
urlpatterns = [
  path('bag/',MyBag,name='bag'),
  path('',index,name='index'),
  path('home',HomeView.as_view(), name='home'),
  path('items/',SavedList.as_view(), name='list'),
  path('item/add/',AddItemView.as_view(), name='add-item'),
  path('item/update/<int:pk>',UpdateItem.as_view(),name='update-item'),
  path('item/delete/<int:pk>',DeleteItem.as_view(),name='delete-item'),
  path('item/export/',ExportList.as_view(),name='export')
  

]