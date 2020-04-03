from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class StudentView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.GET.get('id'):
            student = Student.objects.get(id=request.GET.get('id'))
            serializer = StudentSerializer(student)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        fields = {}
        fields['name'] = request.data['name']
        fields['date_birth'] = request.data['date']
        fields['mark'] = Mark.objects.get(value=request.data['mark'])
        student = Student(**fields)
        student.save()
        return Response({'status': 201})

    def patch(self, request):
        fields = {}
        fields['name'] = request.data['name']
        fields['date_birth'] = request.data['date']
        fields['mark'] = Mark.objects.get(value=request.data['mark'])
        student = Student.objects.get(id=request.data['id'])
        for attr, value in fields.items():
            setattr(student, attr, value)
        student.save()
        return Response({'status': 201})

    def delete(self, request):
        student = Student.objects.get(id=request.data['id'])
        student.delete()
        return Response({'status': 201})


class MarksView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        marks = Mark.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data)
