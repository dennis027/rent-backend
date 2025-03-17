from django.urls import path
from .views import ClientListCreateView, ClientDetailView, HouseListCreateView, HouseDetailView,ReceiptListCreateView,ReceiptDetailView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('houses/', HouseListCreateView.as_view(), name='house-list-create'),
    path('houses/<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
    path('receipts/', ReceiptListCreateView.as_view(), name='receipt-list-create'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
]
