from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from history.serialize.donor import CreateDonorPersonSerializer
from history.serialize.inventory import *
from history.serialize.inventory_status import *
from history.serialize.inventory_location import *
def main(request):
    return HttpResponse('main responses')

class DonorPersonView(APIView):
    # TODO: the other rest operations
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = CreateDonorPersonSerializer(data=request.data)
        if serializer.is_valid():
            # donorPerson = DonorPerson(serializer);
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('could not create DonorPerson from information submitted', status=status.HTTP_400_BAD_REQUEST)

class InventoryItemView(generics.CreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    def post(self, request):
        created = InventoryItemSerializer(data=request.data)
        if created.is_valid():
            created.save()
            return Response(created.data, status=status.HTTP_200_OK)
        else:
            print(created.errors)
            return Response('could not create DonorPerson from information submitted', status=status.HTTP_400_BAD_REQUEST)


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

