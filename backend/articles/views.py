from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import ArticleListSerializer,ArticleSerializer,CommentSerializer,CommentSerializerForProfile,CommentSerializerForComments
from .models import Article,Comment

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)
    else:
        print(request.body)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('request.user:')
            print(request.user)
            user = request.user
            user.point = user.point + 100
            user.save()
            serializer.save(user=user,read=0,comments_cnt = 0)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail_update_delete(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    if not request.user.articles.filter(pk=article_pk).exists():
        return Response({'detail': '권한이 없습니다.'})
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
    else:
        article.delete()
        return Response({'id': article_pk}, status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def comment_list_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'GET':
        User = get_user_model()
        comments = article.comment_set.all()
        infos = []
        for comment in comments:
            cinfo= CommentSerializer(comment).data
            userid = cinfo['user']
            user = get_object_or_404(User,pk=userid)
            username = user.username
            tp = cinfo
            tp['username'] = username
            infos.append(tp)
        # serializer = CommentSerializer(comments,many=True)
        return Response(infos)
    else:
        userid = request.data['user']
        User = get_user_model()
        Users = User.objects.all()
        user = get_object_or_404(Users,pk=userid)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article.comments_cnt = article.comments_cnt+1
            article.save()
            user.point = user.point + 10
            user.save()
            serializer.save(article= article,user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    article = comment.article
    print(article)
    article.comments_cnt = article.comments_cnt -1
    article.save()
    comment.delete()
    return Response({'id': comment_pk}, status= status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def profile_articles(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    user = get_object_or_404(Users,pk=user_pk)
    articles = user.articles.all()
    
    ## 유저점수 확인
    print(user.point)
    ##
    
    # print(comments)
    # print(user)
    # print(articles)
    serializer = ArticleListSerializer(articles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile_comments(request, user_pk):
    User = get_user_model()
    Users = User.objects.all()
    user = get_object_or_404(Users,pk=user_pk)
    comments = user.comments.all()
    infos = []
    for comment in comments:
        cinfo= CommentSerializerForProfile(comment).data
        article_id = cinfo['article']
        article = get_object_or_404(Article,pk=article_id)
        ainfo = ArticleSerializer(article).data
        tp = cinfo
        tp['article'] = ainfo['title']
        infos.append(tp)
    print(infos)
    
    serializer = CommentSerializer(comments,many=True)
    # print(serializer.data)
    return Response(infos)


@api_view(['POST'])
def read(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    article.read = article.read+1
    article.save()
    return Response({'read': article.read }, status=status.HTTP_202_ACCEPTED)
