from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , CreateAPIView

from APIViews.models import Student
from APIViews.serializer import StudentSerializer


class StudentsViews(ListCreateAPIView , CreateAPIView):
    queryset = Student.objects.filter(sex=False)
    serializer_class = StudentSerializer


class StudentViews(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
