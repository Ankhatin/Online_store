from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter

from online_store.models import Dealer, Contacts
from online_store.serializers import DealerSerializer, DealerUpdateSerializer
from users.permissions import IsActiveStaff


class DealerListView(generics.ListAPIView):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [IsActiveStaff]


class DealerCreateView(generics.CreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsActiveStaff]


class DealerRetrieveView(generics.RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsActiveStaff]


class DealerUpdateView(generics.UpdateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerUpdateSerializer
    permission_classes = [IsActiveStaff]


class DealerDestroyView(generics.DestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsActiveStaff]
