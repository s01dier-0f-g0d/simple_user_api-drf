from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response   # JSON RENDERER  # application/data
from django.shortcuts import get_object_or_404
from .models import UserProfile
from .serializers import UserProfileSerializer

@api_view(['GET'])
def api_home(request):
    return Response({
        'message': 'User Profile API',
        'endpoints': {
            'get_all_users': 'GET /api/users/',
            'create_user': 'POST /api/users/',
            'get_user': 'GET /api/users/<id>/',
            'update_user': 'PUT /api/users/<id>/',
            'delete_user': 'DELETE /api/users/<id>/',
        },
        'fields': ['id', 'name', 'date_of_birth', 'age (auto-calculated)']
    })

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        # Get all users from database
        users = UserProfile.objects.all().order_by('id')
        serializer = UserProfileSerializer(users, many=True)
        
        return Response({
            'count': users.count(),
            'users': serializer.data
        })
    
    elif request.method == 'POST':
        # Create new user
        serializer = UserProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    # Find the user or return 404
    user = get_object_or_404(UserProfile, id=user_id)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update user
        serializer = UserProfileSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(
            {'message': f'User {user.name} deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET'])
def search_users(request):
    #Search users by name
    search_name = request.GET.get('name', '').strip()
    
    if not search_name:
        return Response(
            {'error': 'Please provide a name to search using ?name=search_term'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Search for users with similar names
    users = UserProfile.objects.filter(name__icontains=search_name)
    serializer = UserProfileSerializer(users, many=True)
    
    return Response({
        'search_term': search_name,
        'results_found': users.count(),
        'users': serializer.data
    })