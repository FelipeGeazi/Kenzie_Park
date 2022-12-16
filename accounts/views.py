from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    APIView
    has_object_permission -> self.check_object_permission
    """

    authentication_classes = [JWTAuthentication]
    # AND
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    lookup_url_kwarg = "account_id"
