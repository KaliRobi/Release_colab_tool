from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from defects.permissions import IsAuthorOrReadOnly
from defects.models import Defect, Comment
from defects.serializer import DefectSerializer, CommentSerialiser



class DefectSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all().order_by("insert_time")
    serializer_class = DefectSerializer
    lookup_field = "slug"
# it is a must here so we can iterate over them during authetication
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def create(self, serializer):
        serializer.save(auth=self.request.user)




class CommentCreateApiView(generics.CreateAPIView):
    query_set = Comment.objects.all()
    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        reques_user  = self.request.user
        kwar_slug = self.kwargs.get('slug')
        defect = get_object_or_404(Defect, slug=kwar_slug)
        serializer.save(author=reques_user, defect=defect )
