from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import gallery
from django.contrib.auth.models import User
from.serializers import galleryserializer,signupserializer,loginserializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class gallerydetails(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,req):
        print(req.user)
        d= gallery.objects.filter(user=req.user)
        print(d)
        ser= galleryserializer(d,many=True)

        return Response(ser.data)
    
    def post(self,req):
        r=req.data
        print(r)
        ser=galleryserializer(data=r)
        if ser.is_valid(): 
         ser.save(user=req.user) 
         return Response(ser.data)
        return Response(ser.errors)

class signupdetails(APIView):
   
    def get(self,req):
        d= User.objects.all()
        print(d)
        ser=signupserializer(d,many=True)
        return Response(ser.data)

    
    def post(self,req):
        r=req.data
        ser=signupserializer(data=r)
        if ser.is_valid(): 
         ser.save() 
         return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status= status.HTTP_401_UNAUTHORIZED)
    
class logindetails(APIView):
   def get(self,req):
        d= User.objects.all()
        print(d)
        ser=loginserializers(d,many=True)
        return Response(ser.data)

    
   def post(self,req):
        r=req.data
        ser=loginserializers(data=r)
        if ser.is_valid(): 
          user= User.objects.get(username=ser.validated_data)
          print(user)
          token= RefreshToken.for_user(user)
          print(f"access token : {token.access_token},\n\ntoken: {token}")
          
          return Response({"user": user.username,"accestoken":str(token.access_token),"refreshtoken":str(token)},status=status.HTTP_200_OK)
        return Response(ser.errors,status= status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
   

class tokenrefresh(APIView):
      
      def post(self,req):
         r= req.data["req"]
         try:
            token= RefreshToken(r)
            print(r)
            print(f"\n\n token : {token}")
            print(f"\n\naccess token : {token.access_token}")
            return Response({"accesstoken":str(token.access_token)})
         except :
             return Response({"expire":"token expired please log in again"})
         
    


