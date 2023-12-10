from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from django.middleware.csrf import get_token

from defects.permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyComment
from defects.models import Defect, Comment
from defects.serializer import DefectSerializer, CommentSerialiser



class DefectSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all().order_by("-insert_time")
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


class CommentCRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyComment]
    lookup_field = "uuid"


class CommentListApiView(generics.ListAPIView):
    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Comment.objects.filter(defect__slug=kwarg_slug).order_by("-insert_time")

class CommentVoteAPIView(APIView):
    serializer_class = CommentSerialiser
    permission_classes = [IsAuthenticated]

    def post(self, req, uuid):
        comment = get_object_or_404(Comment, uuid=uuid)
        comment.up_votes.add(req.user)
        comment.save()
        serializer_context = {"resquest": req}
        serializer = self.serializer_class(comment, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, req, uuid):
        comment = get_object_or_404(Comment, uuid=uuid)
        comment.up_votes.remove(req.user)
        comment.save()
        serializer_context = {"resquest": req}
        serializer = self.serializer_class(comment, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class CSRFproviderView(View):

    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)
        return JsonResponse({'csrfToken': csrf_token})