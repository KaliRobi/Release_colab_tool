from django.conf import settings
from django.db import models
from application_time.models import ApplicationTimeStamp
import uuid as uuid_library




class Defect(ApplicationTimeStamp):
      slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)  
      defect_number = models.CharField(max_length=25, blank=False)
      priorty = models.IntegerField()
      severiry = models.IntegerField()
      mode_of_transport = models.CharField(max_length=6)
      version = models.CharField(max_length=10)
      status = models.CharField(max_length=20)
      comments = models.CharField(max_length=2000, blank=True)
      author = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='reported_by' 
      )

      def __str__(self):
            return self.comments

class Comment(ApplicationTimeStamp):
      uuid = models.UUIDField(db_index=True, default=uuid_library.uuid4, editable=False )
      body = models.TextField()
      defect = models.ForeignKey(Defect, on_delete=models.CASCADE, related_name='defect_comments')
      author = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='posted_comments' 
      )
      up_votes = models.ManyToManyField(
            settings.AUTH_USER_MODEL, related_name='votes'
      )
      def __str__(self):
            return self.author.username