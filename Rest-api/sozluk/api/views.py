from ..models import Word, Comment
from .serializers import WordSerializer, CommentSerializer
from .pagination import SmallPagination
from rest_framework import viewsets
from rest_framework import mixins
from .permissions import IsAdminOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
# todo test yap


class WordViewSet(viewsets.ReadOnlyModelViewSet):
    throttle_scope = 'hasan'
    queryset = Word.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = WordSerializer
    pagination_class = SmallPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "name"

    def get_queryset(self):
        word_instance = Word.objects.all()
        if self.kwargs.get("name"):
            self.kwargs["name"] = self.kwargs.get("name").lower()
            word_name: str = str(self.kwargs.get("name")).lower()

            try:
                word_instance = Word.objects.filter(name=word_name)
                if word_instance.count() < 1:
                    raise Word.DoesNotExist
            except Word.DoesNotExist:

                if word_name == word_name.lstrip().rstrip():

                    from scripts.cambridge import kelimeTara
                    try:
                        sonuc = kelimeTara(word_name)
                        instancemiz = Word.objects.create(name=sonuc.get("kelime"), description=sonuc.get("description"),
                                                          voice=sonuc.get("usSoundLink"), partOfSpeech=sonuc.get("nitelik"),
                                                          example=sonuc.get("example"))
                        instancemiz.save()
                    except:
                        print("cambridge problems")

            return word_instance

        return word_instance


class CommentDetailCreateViewSet(mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    throttle_scope = 'hasan'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = SmallPagination
    #authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == "destroy":
            permission_classes = [IsYorumSahibiOrReadOnly]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
