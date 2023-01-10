from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAnonymous, IsOwner
from .serializers import UserDetailSerializer, UserChangePassword, UserRegister, UserEditSerializer
from .throttles import RegisterThrottle
from ..models import CustomUser
from rest_framework.permissions import IsAuthenticated


class UserDetailApiView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    throttle_scope = 'hasan'


class UserPasswordChangeApiView(APIView):
    serializer_class = UserChangePassword
    permission_classes = [IsAuthenticated]
    throttle_scope = 'hasan'

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        serializer = UserChangePassword(data=data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")

            if not user.check_password(old_password):
                return Response({"old_password": "Wrong Password"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"Status": "Accept"}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterApiView(CreateAPIView):
    serializer_class = UserRegister
    permission_classes = [IsAnonymous]
    throttle_classes = [RegisterThrottle]
    throttle_scope = 'hasan'


class UserEditApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserEditSerializer
    permission_classes = [IsOwner]
    lookup_field = "id"
    throttle_scope = 'hasan'

    def get_queryset(self):
        user_id = self.kwargs.get("id")
        return CustomUser.objects.filter(id=user_id)
