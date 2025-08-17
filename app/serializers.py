from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,Serializer,ValidationError
from .models import gallery
from django.contrib.auth.models import User
class galleryserializer (ModelSerializer):
     class Meta:
          model= gallery
          fields=["imgname","no","user"]
          read_only_fields=["user"]

     def validate(self, req):
          no= req.get("no")
          if no<=0:
               raise ValidationError({"no":"no should be grater than 0"})
          return req
     def create(self, req):
          imgname=req.get("imgname")
          no=req.get("no")
          user=req.get("user")
          return gallery.objects.create(imgname=imgname,no=no,user=user)
    
class signupserializer (ModelSerializer):
     email=serializers.EmailField(required=True)
     password=serializers.CharField(write_only=True,required=True)
     username=serializers.CharField()
     class Meta:
          model= User
          fields=["username","email","password"]
        
     def validate(self, req):
          if User.objects.filter(username=req.get("username")):
               raise ValidationError({"error":"Username already taken"})
          return req
     def create(self, validated_data):
          user= User(**validated_data)
          user.set_password(validated_data["password"])
          user.save()
          return user
          

class loginserializers(Serializer):
     
     username=serializers.CharField(required=True)
     password=serializers.CharField(required=True)
     def validate(self, req):
          username= req.get("username")
          password=req.get("password")
          
          try :
           user= User.objects.get(username=username)
           if  not user.check_password(password):
               raise ValidationError({"error":"invalid pasword"})
           print(f"ser user : {user}")
           return user
          except:
           raise ValidationError({"error":"invalid username"})
          
     
     
     
     
    
      
