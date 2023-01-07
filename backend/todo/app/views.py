from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TodoSerializer,UserSerializer
from django.contrib.auth.models import User
from .models import AddTodo
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAdminUser




class Register(APIView):
  
    # def get(self,format=None):
    #     permission_classes=[IsAdminUser]
    #     authentication_classes=[TokenAuthentication]
    #     user=User.objects.all()
    #     user_serializer=UserSerializer(user, many=True)
    #     return Response(user_serializer.data)
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.get(username=serializer.data["username"])
            obj_token =Token.objects.create(user=user)
            return Response({"status":201,"payload":serializer.data,"token":str(obj_token), "message":"Ok"})
        return Response(serializer.data,status=status.HTTP_403_FORBIDDEN)
    


class TodoList(APIView):
    def get(self,request,format=None):
        permission_classes=[IsAuthenticated]
        authentication_classes=[TokenAuthentication]
        if request.user:
            todo_list=AddTodo.objects.filter(username=request.user)
            todo_serializer=TodoSerializer(todo_list,many=True)
            return Response(todo_serializer.data)
        else:
            todo_list=AddTodo.objects.all()
            todo_serializer=TodoSerializer(todo_list,many=True)
            return Response(todo_serializer.data)
        print(request)
    
    def post(self,request,format=None):
        permission_classes=[IsAuthenticated]
        authentication_classes=[TokenAuthentication]
        todo_serializer=TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save(username=request.user)
            return Response(todo_serializer.data)
        return Response(todo_serializer.errors)
