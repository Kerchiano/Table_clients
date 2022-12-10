from rest_framework.viewsets import GenericViewSet
from .models import Customer
from rest_framework import mixins
from .serializers import CustomerSerializer


class ClientsList(GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
