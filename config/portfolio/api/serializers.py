from portfolio.models import *
from rest_framework import serializers



class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'

class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class AboutMeSerializers(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = AboutMe
        fields = '__all__'
        
    def get_skill(self, obj):
        skill = obj.skill

        serializer_skill = SkillSerializers(skill, many=False)

        return serializer_skill.data