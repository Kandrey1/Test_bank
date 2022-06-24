from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .serializers import *
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    db_clients = Client.objects.all()
    db_organizations = Organization.objects.all()
    db_bills = Bills.objects.all()
    qq = get_data_two_endpoint()
    return render(request, "bills/index.html",
                  {"db_clients": db_clients, "db_organizations": db_organizations,
                   "db_bills": db_bills, "qq": qq})


class GetOneEndPointView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer_for_queryset = OneEndPointSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)


class GetTwoEndPointView(APIView):
    def get(self, request):
        queryset = get_data_two_endpoint()
        serializer_for_queryset = TwoEndPointSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)


def get_data_two_endpoint():
    list_dict = []
    db_clientss = Client.objects.all()
    for client in db_clientss:
        dict_data = {}
        number = Organization.objects.filter(client_name=client).count()

        orgs = Organization.objects.filter(client_name=client).values()

        organizat = []
        for org in orgs:
            organizat.append(org['organization'])

        summa = Bills.objects.all().filter(
            organization_client__in=organizat).aggregate(
            total=Sum('balance'))["total"]
        if summa == None:
            summa = 0

        LC = ListClients(client=client, number=number, summa=summa)
        serializer = TwoEndPointSerializer(LC)
        list_dict.append(serializer.data)

    return list_dict


class ListClients:
    def __init__(self, client, number, summa):
        self.client = client
        self.number = number
        self.summa = summa


class GetThreeEndPointView(generics.ListAPIView):
    queryset = Bills.objects.all()
    serializer_class = ThreeEndPointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['organization_client', 'account_number']
