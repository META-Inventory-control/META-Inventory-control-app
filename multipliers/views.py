from django.shortcuts import render
from rest_framework import generics
from .models import Multipliers
from .serializers import MultipliersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse
from rest_framework.decorators import authentication_classes, permission_classes
from .permissions import RecalculatePermission
from django.shortcuts import get_object_or_404
from products.models import Product

# Create your views here.


class MultipliersView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch"]

    queryset = Multipliers.objects.all()
    serializer_class = MultipliersSerializer
    lookup_url_kwarg = "multipliers_id"


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, RecalculatePermission])
def recalculate_costs(request):
    multipliers = get_object_or_404(Multipliers, pk=1)
    products = Product.objects.all()

    for product in products:
        if product.final_cost_altered:
            pass
        else:
            entry_cost = product.entry_cost
            if entry_cost <= 50:
                product.final_cost = (
                    entry_cost * multipliers.multi_0_50 / 100 + entry_cost
                )
            elif entry_cost > 50 and entry_cost <= 150:
                product.final_cost = (
                    entry_cost * multipliers.multi_51_150 / 100 + entry_cost
                )
            elif entry_cost > 151 and entry_cost <= 700:
                product.final_cost = (
                    entry_cost * multipliers.multi_151_700 / 100 + entry_cost
                )
            elif entry_cost > 701 and entry_cost <= 1500:
                product.final_cost = (
                    entry_cost * multipliers.multi_701_1500 / 100 + entry_cost
                )
            elif entry_cost > 1501 and entry_cost <= 3000:
                product.final_cost = (
                    entry_cost * multipliers.multi_1501_3000 / 100 + entry_cost
                )
            elif entry_cost > 3001 and entry_cost <= 6000:
                product.final_cost = (
                    entry_cost * multipliers.multi_3001_6000 / 100 + entry_cost
                )
            elif entry_cost > 6000:
                product.final_cost = (
                    entry_cost * multipliers.multi_6001_8 / 100 + entry_cost
                )

        product.save()

    return HttpResponse("Costs have been recalculated for all products.")
