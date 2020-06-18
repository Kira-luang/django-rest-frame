from rest_framework import serializers

from APIViews.models import Teacher , Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name' , 'sex']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name' , 'sex']
