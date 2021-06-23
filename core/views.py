from django.contrib.auth import get_user_model
from rest_framework import views, filters

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import TweetsPagination
from .permissions import OwnTweetViewPermission
from .serializers import UserRegisterSerializer, TweetSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import UserTweets


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class TweetsView(views.APIView):
    serializer_class = TweetSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = TweetsPagination()

    def get(self, request):
        data = UserTweets.objects.all().order_by("-created_on")
        # print(request.GET.get('page_size'))
        page = self.pagination_class.paginate_queryset(queryset=data, request=request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.pagination_class.get_paginated_response(serializer.data)

    def post(self, request):
        data = dict(request.data)
        data['user'] = request.user.id
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "Message": "Object Created Successfully",
                "Response Code": HTTP_201_CREATED
            })

        else:

            return Response({
                "Message": "There Was An Error Creating The Tweet!",
                "Response Code": HTTP_403_FORBIDDEN
            })


class OwnTweetsView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OwnTweetViewPermission,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ['tweet_text']

    def get(self, request):
        data = get_user_model().objects.filter(id=request.user.id)[0]
        tweets = data.tweets.filter(tweet_text=request.GET.get('search'))
        return Response({
            'data': [
                {
                    "user_id": data.id,
                    "username": data.name,
                    "email": data.email,
                    "tweets": [{"text": i.tweet_text, "created_on": i.created_on} for i in tweets]
                }

            ]
        })