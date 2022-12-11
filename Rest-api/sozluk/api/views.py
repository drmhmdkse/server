#from rest_framework import status
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Word
from .serializers import WordSerializer


# concrete Viewslar
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,CreateAPIView,get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsYorumSahibiOrReadOnly
from .pagination import SmallPagination,LargePagination


class WordListCreateApiView(ListCreateAPIView):
    throttle_scope='hasan'
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = SmallPagination


class WordDetailUpdateApiView(RetrieveUpdateAPIView):
    throttle_scope = 'hasan'  # settingslerde throttle rate altında kullanılabilir
    lookup_field = "name"
    #queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        self.kwargs["name"]=self.kwargs.get("name").lower()
        word_name: str = str(self.kwargs.get("name")).lower()
        word_instance = Word.objects.all()
        try:
            word_instance = Word.objects.filter(name=word_name)
            if word_instance.count()<1:
                raise Word.DoesNotExist
        except Word.DoesNotExist:

            if word_name == word_name.lstrip().rstrip():

                from scripts.cambridge import kelimeTara
                try:
                    sonuc = kelimeTara(word_name)
                    instancemiz = Word.objects.create(name=sonuc.get("kelime"),description=sonuc.get("description"),voice=sonuc.get("usSoundLink"),partOfSpeech=sonuc.get("nitelik"),example=sonuc.get("example"))
                    instancemiz.save()
                except:
                    print("cambridge problems")

        return word_instance


    # get metodunu override ettik










################################# function based  api_view decoratör ile
'''@api_view(['GET','POST'])
def word_listele_create_api_view(request):
    if request.method=='GET':
        model=Word.objects.all()
        serializer=WordSerializer(model,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method=="POST":
        serializer=WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response( serializer.errors,status=status.HTTP_400_BAD_REQUEST)'''

################################# class based APIView
'''
class WordListCreateApiView(APIView):

    def get(self,request):
        model = Word.objects.all()
        serializer = WordSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''

#################################   class based Generec api views and Mixins
'''from rest_framework.generics import GenericAPIView # genericapiview mixinler için base sınıftır
from rest_framework.mixins import ListModelMixin,CreateModelMixin


class WordListGenericApiView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)'''





#Comment section
'''class CommentCreateApiView(CreateAPIView):
    throttle_scope='hasan'
    queryset = Comment
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        word_id=self.kwargs.get('pk')
        word=get_object_or_404(Word,id=word_id)
        serializer.save(user=self.request.user,word=word)


class CommentDetailApiView(RetrieveUpdateDestroyAPIView):
    throttle_scope='hasan'
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]'''


