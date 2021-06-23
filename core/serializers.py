from rest_framework import serializers
from core.models import UserTweets
from django.contrib.auth import get_user_model


class UserRegisterSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """
    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'email', 'password')
        read_only = ('name', 'id', )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """ Create and return a new user """
        user = get_user_model().objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password'),
        )

        return user


class TweetSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserTweets
        fields = ('user', 'id', 'tweet_text', 'created_on')


