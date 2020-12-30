from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save(point=0)
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # print(user.password)
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def takename(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    #print(User.objects.all())
    # print(user_pk)
    user = get_object_or_404(Users,pk=user_pk)
    # print(user)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def points(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    #print(User.objects.all())
    # print(user_pk)
    user = get_object_or_404(Users,pk=user_pk)
    return Response({'point': user.point})

@api_view(['GET'])
def recommend(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    user = get_object_or_404(Users,pk=user_pk)
    fav_movies = user.favorite_movies.all()
    if len(fav_movies) == 0:
        fav_movie = -1
    else:
        fav_movie = fav_movies[len(fav_movies)-1].movie_id
    # dict = {'fav_movies' : []}
    # for each in fav_movies[:3]:
    #     dict['fav_movies'].append(each.movie_id)
    return Response({'fav_movie' : fav_movie}, status=status.HTTP_202_ACCEPTED)