from rest_framework.views import APIView
from rest_framework.response import Response
from .models import userdatatable
from.serializers import userdataserializer,signupserializer
from django.contrib.auth.models import User
class userdata(APIView):
     def get (self,req):
          d=userdatatable.objects.all()
          ser=userdataserializer(d,many=True)
          print("you hit get api")
          return Response (ser.data)
     def post(self,req):
          data=req.data
          ser=userdataserializer(data=data)
          if ser.is_valid():
               ser.save()
               return Response(ser.data)
          return Response(ser.errors)
     def put(self,req):
          ins=userdatatable.objects.get(id= req.data['id'])
          data=req.data
          print(data)
          ser=userdataserializer(ins,data=data)
          if ser.is_valid () :
               ser.save()
               return Response(ser.data)
          return Response(ser.errors)
     def patch(self,req):
          ins=userdatatable.objects.get(id= req.data['id'])
          data=req.data
          print(data)
          ser=userdataserializer(ins,data=data,partial=True)
          if ser.is_valid () :
               ser.save()
               return Response(ser.data)
          return Response(ser.errors)
     def delete (self,req):
          ins=userdatatable.objects.get(id=req.data['id'])
          ins.delete()
          return Response({'messagee':'details deleted'})
               
       
class signup(APIView):
     def post(self,req):
          
          data=req.data
          print(data)
          
          username=data['username']
          print(username)
          email=data['email']
          password=data['password']

          if User.objects.filter(username=username).exists():
               return Response({'error message': 'username already exists'})
          user=User.objects.create_user(username=username,email=email,password=password)

          ser=signupserializer(user)
          return Response({'message':'new user created',
                           'user':ser.data})
          

        
        
