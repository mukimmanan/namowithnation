from django.urls import path
from core.views import LoginView, UserRegisterView, TweetsView, OwnTweetsView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('tweets/', TweetsView.as_view()),
    path('owntweets/', OwnTweetsView.as_view())
]