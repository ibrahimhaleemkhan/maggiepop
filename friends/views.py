from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialApp, SocialToken, SocialLogin
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# Log in from Facebook
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from friends.models import UserProfile, Game


@csrf_exempt
def mobile_facebook_login(request):
    if request.method=="POST":
        response=HttpResponse
        access_token =str(request.POST['access_token'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                profile=UserProfile.objects.get_or_create(user=user,dp=account.get_avatar_url(),fullName=user.get_full_name())[0]
                return HttpResponse(serializers.serialize("json",[profile]))
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))

@csrf_exempt
def update_location(request):
    if request.method=="POST":
        lon=str(request.POST['longitude'])
        lat=str(request.POST['latitude'])
        access_token =str(request.POST['access_token'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                profile=UserProfile.objects.update(longitude=lon,latitude=lat)
                return HttpResponse("done")
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))



@csrf_exempt
def create_game(request):
    if request.method=="POST":
        lon=str(request.POST['longitude'])
        lat=str(request.POST['latitude'])
        access_token =str(request.POST['access_token'])
        type=str(request.POST['type'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                location = Point(lon, lat)
                game=Game.objects.create(host=user,location=location,type=type)
                return HttpResponse("done")
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))

@csrf_exempt
def create_game(request):
    if request.method=="POST":
        lon=str(request.POST['longitude'])
        lat=str(request.POST['latitude'])
        access_token =str(request.POST['access_token'])
        type=str(request.POST['type'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                location = Point(lon, lat)
                game=Game.objects.create(host=user,location=location,type=type)
                return HttpResponse(serializers.serialize("json",[game]))
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))


@csrf_exempt
def join_game(request):
    if request.method=="POST":
        id=str(request.POST['uuid'])
        access_token =str(request.POST['access_token'])
        type=str(request.POST['type'])
        #email=str(request.POST['email'])
        try:
            app=SocialApp.objects.get(provider="facebook")
            token=SocialToken(app=app,token=access_token)
             # Check token against facebook
            login = fb_complete_login(request, app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            # Add or update the user into users table
            ret = complete_social_login(request, login)
            a=SocialToken.objects.get(token=access_token)
            try:
                account=a.account
                user=account.user
                game=Game.objects.create(id=id)
                game.participants.add(user)
                return HttpResponse(serializers.serialize("json",[game]))
            except User.DoesNotExist:
                return HttpResponse("User Dosent Exist")
            return HttpResponse("wuhoo")
        except Exception as e:
            # If we get here we've failed
           return HttpResponse("ASdsa "+str(e))

