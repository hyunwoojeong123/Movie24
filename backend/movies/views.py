from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model


from .serializers import MovieSerializer,ReviewSerializer, ReviewSerializerForReviews
from .models import Movie, Review

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
@api_view(['GET'])
def movielist(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bestFive(request):
    movies = Movie.objects.all().order_by('-vote_average')[:20]
    # print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def moviedetail(request,movie_id):
    movie = get_object_or_404(Movie,movie_id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET','POST'])
def reviews_create(request, movie_id):
    movie = get_object_or_404(Movie,movie_id=movie_id)
    if request.method == 'GET':
        User = get_user_model()
        reviews = movie.review_set.all()
        infos = []
        for review in reviews:
            rinfo = ReviewSerializer(review).data
            userid = rinfo['user']
            user = get_object_or_404(User,pk=userid)
            username = user.username
            tp = rinfo
            tp['username'] = username
            infos.append(tp)
        # serializer = ReviewSerializer(reviews,many=True)
        return Response(infos)
    else:
        #print(request.user)
        userid = request.data['user']
        User = get_user_model()
        Users = User.objects.all()
        user = get_object_or_404(Users,pk=userid)
        rating = int(request.data['rating'])
        # print(type(rating))
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie = movie, user = user)
            if rating >= 7:
                if not movie.like_users.filter(pk=userid).exists():
                    movie.like_users.add(user)
            print(movie.like_users)
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['DELETE'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    review.delete()
    return Response({'id': review_pk}, status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def forUserMovieSave(request):
    # print(request.body)
    # print(request.body)
    init_movies = request.data['forusermovies']
    # print(init_movies[0])
    for init_movie in init_movies:
        print(init_movie['title'],init_movie['id'])
        if not Movie.objects.filter(movie_id=init_movie['id']).exists():
            print('새로만듬')
            
            Movie.objects.create(
                poster_path=init_movie['poster_path'],
                title=init_movie['title'],
                vote_average=init_movie['vote_average'],
                overview=init_movie['overview'],
                release_date=init_movie['release_date'],
                movie_id=init_movie['id'],
                )
        else:
            print('이미 있어서 안만듬~')
            pass
    return Response({'봉현': '봉현'}, status= status.HTTP_202_ACCEPTED)