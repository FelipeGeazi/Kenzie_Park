from rest_framework import permissions
from rest_framework.views import Request, View
from parking_lots.models import ParkingLot
import ipdb


class IsAdminOrParkingLotOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: ParkingLot):
        """
        Somente o dono ou admin pode obter/atualizar/deletar parking lot
        """

        return request.user == obj.owner or request.user.is_superuser
