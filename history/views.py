import io
import time

from django.db import Error
from django.http import JsonResponse
from rest_framework import status
import json

from rest_framework.parsers import JSONParser

from history.entity.donor import DonorPerson
from history.util.model_utils import randomId
from django.core import serializers
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from history.serialize.donor import CreateDonorPersonSerializer, DonorPersonSerializer, \
    CreateDonorOrganizationSerializer
from history.serialize.inventory import *
from history.serialize.inventory_status import *
from history.serialize.inventory_location import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist



@api_view(["GET", "POST"])
def main(request, *args, **kwargs):
    pass

def test(request, *args, **kwargs):
    print(request.content_type)
    body = request.body
    print("body:----------------------------------------")
    print(body)
    print("headers:----------------------------------------")
    print(dict(request.headers))
    body_data = {}
    try:
        body_data = json.loads(body)
    except:
        pass
    print("body data json: ----------------------------------------")
    print(f"{body_data}")
    print("body data json keys: ----------------------------------------")
    print(f"{body_data.keys()}")
    print("request.GET: ----------------------------------------")
    print(f"{request.GET}")
    return JsonResponse({"message": 'main responses'})


class DonorPersonView(APIView):
    def post(self, request, format=None):
        print(f"DonorPersonView(APIView):post(self, request, format=None):----------------------------------------")
        print(f"@ {time.time()}")
        print(f"--------------------------------------------------------------------------------------------------")
        body = request.body
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        new_donor = JSONParser().parse(io.BytesIO(body))
        new_donor["donor_person_id"] = randomId()

        donor_type = new_donor['type']

        if donor_type == 1:
            serializer = CreateDonorPersonSerializer(data=new_donor)
            if serializer.is_valid():
                print(f"saving DonorPerson with {serializer.validated_data}")
                # serializer.save()
                DonorPerson.objects.create(**serializer.validated_data)
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            else:
                return Response('could not create DonorPerson from information submitted',
                                status=status.HTTP_400_BAD_REQUEST
                )
        # else:
        #     # is an organization
        #     serializer = CreateDonorOrganizationSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     else:
        #         return Response('could not create DonorOrganization from information submitted',
        #                         status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        searchTerm = request.query_params['searchTerm']
        if searchTerm != None:
            try:
                founds = DonorPerson.objects.filter(last_name__contains=searchTerm).filter(
                    first_name__contains=searchTerm)
                return JsonResponse(serializers.serialize("json", founds), safe=False, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                print(f"DonorPerson.get: search {searchTerm} {ObjectDoesNotExist}")
                return JsonResponse({}, status.HTTP_404_NOT_FOUND)
        print(f"DonorPerson.get: search failed for None searchTerm")
        return JsonResponse({}, status.HTTP_404_NOT_FOUND)


class InventoryItemView(generics.CreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def post(self, request):

        nextId = randomId()
        already = None
        try:
            already = InventoryItem.objects.get(inventory_item_id=nextId)
        except:
            while already is not None:
                nextId = randomId()
                already = InventoryItem.objects.get(inventory_item_id=nextId)
                print(f"prevent dupe. using nextId {nextId}")
        request.data['inventory_item_id'] = nextId
        created = InventoryItemSerializer(data=request.data)
        if created.is_valid():
            created.save()
            return Response(created.data, status=status.HTTP_200_OK)
        else:
            print(created.errors)
            return Response('could not create DonorPerson from information submitted',
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        all = InventoryItem.objects.get()
        return JsonResponse(all, status=status.HTTP_200_OK)


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
