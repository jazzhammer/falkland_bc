from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


def main(request):
    return HttpResponse('main responses')

class DonorPersonView(APIView):
    serializer_class = CreateDonorPersonSerializer
    # TODO: the other rest operations
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            donorPerson = DonorPerson(serializer.data);
            # donorPerson = DonorPerson(
            #     last_name=serializer.data.last_name,
            #     first_name=serializer.data.first_name,
            #     street=serializer.data.street,
            #     city=serializer.data.city,
            #     province_state=serializer.data.province_state,
            #     country=serializer.data.country,
            #     phone_area_code=serializer.data.phone_area_code,
            #     phone_number=serializer.data.phone_number
            # )
            donorPerson.save()
            return Response(DonorPersonSerializer(donorPerson).data, status=status.HTTP_201_CREATED)

class InventoryItemView(generics.CreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


class InventoryImageView(generics.CreateAPIView):
    queryset = InventoryImage.objects.all()
    serializer_class = InventoryImageSerializer

class InventoryStatusView(generics.CreateAPIView):
    queryset = InventoryStatus.objects.all()
    serializer_class = InventoryStatusSerializer

class InventoryStatusAssignView(generics.CreateAPIView):
    queryset = InventoryStatusAssign.objects.all()
    serializer_class = InventoryStatusAssignSerializer

class InventoryLocationAssignView(generics.CreateAPIView):
    queryset = InventoryLocationAssign.objects.all()
    serializer_class = InventoryLocationAssignSerializer

class InventoryLocationView(generics.CreateAPIView):
    queryset = InventoryLocation.objects.all()
    serializer_class = InventoryLocationSerializer

