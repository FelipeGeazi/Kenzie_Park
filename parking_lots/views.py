from .models import ParkingLot
from .serializers import ParkingLotSerializer, DetailedParkingLotSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrParkingLotOwner
import ipdb


class ParkingLotView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        GET -> ParkingLotSerializer
        POST -> DetailedParkingLotSerializer
        """
        if self.request.method == "POST":
            return DetailedParkingLotSerializer

        return ParkingLotSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ParkingLot.objects.all()

        return ParkingLot.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

    lookup_url_kwarg = "parking_lot_id"
