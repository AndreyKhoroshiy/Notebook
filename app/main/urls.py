from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_list, name='list'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ContactsDetailView.as_view(), name='details'),
    path('<int:pk>/update', views.ContactsUpdateView.as_view(), name='update')
]
