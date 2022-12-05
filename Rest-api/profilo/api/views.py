from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from profilo.models import Profil
from .serializers import ProfilSerializer
from .pagination import LargePagination,SmallPagination

class ListUsersAPiView(ListAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    pagination_class =LargePagination
    permission_classes = [IsAuthenticated]