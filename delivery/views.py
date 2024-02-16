# delivery/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Organization, Pricing
from .serializers import OrganizationSerializer, PricingSerializer

class OrganizationListView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class PricingView(generics.RetrieveAPIView):
    serializer_class = PricingSerializer

    def get_object(self):
        zone = self.request.query_params.get('zone')
        organization_id = self.request.query_params.get('organization_id')
        total_distance = float(self.request.query_params.get('total_distance'))
        item_type = self.request.query_params.get('item_type')

        # Implement your pricing logic here based on the provided requirements
        # Example pricing logic (modify as per your requirements)
        base_distance = 5  # Example base distance in kilometers
        base_price = 10  # Example base price in euros

        if total_distance <= base_distance:
            total_price = base_price
        else:
            per_km_price = 1.5 if item_type == 'perishable' else 1.0
            additional_distance = total_distance - base_distance
            total_price = base_price + (additional_distance * per_km_price)

        # Create a Pricing object and return it
        pricing_object = Pricing(
            organization_id=organization_id,
            zone=zone,
            base_distance_in_km=base_distance,
            km_price=per_km_price,
            fix_price=base_price
        )

        return pricing_object
