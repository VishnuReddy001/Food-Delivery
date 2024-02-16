# delivery/urls.py

from django.urls import path
from .views import OrganizationListView, PricingView

urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),
    path('pricing/', PricingView.as_view(), name='pricing'),
]
