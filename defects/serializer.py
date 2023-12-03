from rest_framework import serializers

from defects.models import Defect
from defects.models import Comment

class DefectSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    insert_time = serializers.SerializerMethodField()
    slug  = serializers.SlugField(read_only=True)
    answers_count =  serializers.SerializerMethodField()
    user_answered = serializers.SerializerMethodField()

    class Meta:
        model = Defect
        exclude = ['update_time']


    def get_insert_time(self, instance):
        #month name, day,  year
        return instance.insert_time.strftime('%d-%b-%Y')
    
    def get_answers_count(self, instance):
        return len(instance.comments )
    
    def get_user_answered(self, instance):
        req = self.context.get("request")
        pass



class CommentSerialiser(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    insert_time = serializers.SerializerMethodField()
    votes_count =  serializers.SerializerMethodField()
    has_user_voted = serializers.SerializerMethodField()
    comment_slag = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ['defect', 'up_vote', 'update_time']

   
    def get_insert_time(self, instance):
        #month name, day,  year
        return instance.insert_time.strftime('%d-%b-%Y')
    
    def get_up_votes_count(self, instance):
        return instance.up_votes.count()
    

    def get_user_answered(self, instance):
        req = self.context.get("request")
        return instance.voters.filter(pk=req.user.pk ).existsi()
    
    def get_defect_slug(self,instance):
        return instance.defect.slug