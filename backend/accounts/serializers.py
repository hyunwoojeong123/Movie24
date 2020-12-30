from rest_framework import serializers
from django.contrib.auth import get_user_model

# 모델을 직접적으로 건들이는 일을 최소화하고 serializer를 통해 다룸
class UserSerializer(serializers.ModelSerializer):
    # password부분을 덮어씀, write_only=True는 인스턴스를 업데이트하거나 생성할때는 쓰지만, serializing을 표현할때는 포함되지 않는다.
    # read_only=True는 반대로 표현할때만쓰고 인스턴스를 serializing을 생성하거나 업데이트할때는 사용되지 않음
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')