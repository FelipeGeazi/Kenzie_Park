from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import ipdb

from .serializers import FloorSerializer
from .models import Floor
from parking_lots.models import ParkingLot
from parking_lots.permissions import IsAdminOrParkingLotOwner


class FloorView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    # queryset = Floor.objects.all().all()
    serializer_class = FloorSerializer

    def get_queryset(self):
        parking_lot_id = self.kwargs["parking_lot_id"]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)

        floors = Floor.objects.filter(parking_lot=parking_lot_obj)

        return floors

    def perform_create(self, serializer):
        # 1. Verificar se o estacionamento existe
        parking_lot_id = self.kwargs["parking_lot_id"]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)

        # 2. Verificar se o usuario é dono ou admin
        self.check_object_permissions(self.request, parking_lot_obj)

        serializer.save(parking_lot=parking_lot_obj)
