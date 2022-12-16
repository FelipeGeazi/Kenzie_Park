from rest_framework import serializers
from .models import ParkingLot
import ipdb
from accounts.serializers import AccountSerializer


class DetailedParkingLotSerializer(serializers.ModelSerializer):
    """
    Informações detalhadas sobre owner (OwnerSerializer)
    """

    owner = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "owner"]


class ParkingLotSerializer(serializers.ModelSerializer):
    """
    Somente a FK de owner
    """

    owner_username = serializers.SerializerMethodField()

    def get_owner_username(self, obj: ParkingLot) -> str:
        return f"{obj.owner.id} - {obj.owner.username}"
        # return "batata"

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "owner", "owner_username"]
