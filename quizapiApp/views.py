from django.shortcuts import render
from rest_framework .response import Response
from rest_framework import status

from rest_framework.generics import GenericAPIView
from .models import quiz

from quizapiApp.serializers import quizSerializer

# Create your views here.

class quizRegisterAPIView(GenericAPIView):
    serializer_class = quizSerializer
    
    def post(self, request):
        questions = request.data.get('questions')
        answer = request.data.get('answer')
        mark = request.data.get('mark')
        serializer = self.serializer_class(data={'questions':questions,'answer':answer,'mark':mark})

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'quiz details added successfully', 'successs':1}, status = status.HTTP_201_CREATED)
        
        return Response({'data':serializer.errors, 'message':'Failed','successs':0}, status = status.HTTP_400_BAD_REQUEST)


class get_quizAPIView(GenericAPIView):
    serializer_class = quizSerializer
    def get(self, request):
        queryset = quiz.objects.all()
        if(queryset.count()>0):
            serializer = quizSerializer(queryset, many=True) 
            # for i in serializer.data:
            #     login_id = i['log_id']   
            #     name = i['name']
            return Response({'data':serializer.data, 'message':'data get','successs':1})
        else:
            return Response({'data':'No data available'}, status=status.HTTP_400_BAD_REQUEST)

class update_quizAPIView (GenericAPIView):
    serializer_class = quizSerializer
    def put(self, request, id):
        queryset = quiz.objects.get(pk=id)
        print(queryset)
        serializer = quizSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':1}, status=status.HTTP_200_OK)

class delete_quizAPIView(GenericAPIView):

    def delete(self, request, id):
        delmember = quiz.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully'})


class SingleQuizAPIView(GenericAPIView):

    def get(self, request, id):
        queryset = quiz.objects.get(pk=id)
        serializer = quizSerializer(queryset)
        return Response(serializer.data)



























