from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Note, Profile, GeneratePassword, DeveloperMode
from .serializers import NoteSerializer, ProfileSerializer, GeneratePasswordSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import UserCreateSerializer, DeveloperModeSerializer
from django.http import JsonResponse

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_generated_password(request):
    data_context = {
        'person': User.objects.get(email=request.data.get('email')).pk,
        'password_val': request.data.get('password'),
    }
    serializer = GeneratePasswordSerializer(data=data_context)
    if serializer.is_valid():
        save_password = GeneratePassword(
            person = User.objects.get(email=request.data.get('email')),
            password_val = request.data.get('password'),
        )
        save_password.save()
        return Response(status=200)
    else:
        data = serializer.errors
        return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):
    data_context = {
        'author': User.objects.get(email=request.data.get('email')).pk,
        'name': request.data.get('name'),
        'body': request.data.get('body')
    }
    serializer = NoteSerializer(data=data_context)
    if serializer.is_valid():
        new_note = Note(
            author =User.objects.get(email=request.data.get('email')),
            name = request.data.get('name'),
            body = request.data.get('body')
        )
        new_note.save()
        return Response(status=200)
    else:
        data = serializer.errors
        return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeleteNote(request):
    note_name = request.data.get('name')
    author =User.objects.get(email=request.data.get('email'))
    get_note = Note.objects.get(author=author, name=note_name)
    get_note.delete()
    return Response(status=200)

@api_view(['POST'])
def CreateUser(request):
    if request.method == 'POST':
        serializer =  UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=request.data.get('username'),
                email=request.data.get('email'),
                first_name= request.data.get('first_name'),
                last_name = request.data.get('last_name'),
                password= request.data.get('password'),
            )
            if len(request.data.get('password')) < 8:
                return Response({'Error': 'Passwords is too short'})
            if request.data.get('password') == request.data.get('re_password'):
                user.save()
                return Response({'success': 'User Created Successfully'})
            else:
                return Response({'Error': 'Passwords do not match'})
        else:
            data = serializer.errors
            return Response(data)



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_profile(request):
    data_context = {
        'person': User.objects.get(email=request.data.get('email')).pk,
        'gender': request.data.get('gender'),
        'hobby': request.data.get('hobby')
    }
    serializer = ProfileSerializer(data=data_context)
    if serializer.is_valid():
        new_profile = Profile(
            person = User.objects.get(email=request.data.get('email')),
            gender = request.data.get('gender'),
            hobby = request.data.get('hobby')
        )
        new_profile.save()
        return Response(status=200)
    else:
        data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def download_template(request, name):
    serializer = DeveloperModeSerializer(data=request.data)
    if serializer.is_valid():
        get_template = DeveloperMode.objects.get(name=name)
        return Response(data=get_template)
    else:
        data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_all_templates(request):
    data = DeveloperMode.objects.all().order_by('-name')
    serializer = DeveloperModeSerializer(data, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)