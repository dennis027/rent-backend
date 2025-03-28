from django.urls import path
from .views import ClientListCreateView, ClientDetailView, HouseListCreateView, HouseDetailView,ReceiptListCreateView,ReceiptDetailView,register_view, login_view, logout_view,SystemVariableDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('houses/', HouseListCreateView.as_view(), name='house-list-create'),
    path('houses/<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
    path('receipts/', ReceiptListCreateView.as_view(), name='receipt-list-create'),
    path('receipts/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('system-variables/', SystemVariableDetailView.as_view(), name='system-variable-detail'),
]
