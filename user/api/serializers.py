from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from ..models import UserInfo, Firm

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=UserInfo.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password1 = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = UserInfo
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password1",
            "gender",
            "phone_number",
            "birth_date",
        )

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password must be same with above ! ..."}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password1')
        user = UserInfo.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "birth_date",
        )

class FirmRegisterSerializer(serializers.ModelSerializer):
    username = User._meta.get_field('username').required = False

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=UserInfo.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password1 = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = Firm
        fields = (
            "id",
            "email",
            "firm_name",
            "password",
            "password1",
            "address",
            "logo",
            "phone_number",
            "website",
        )

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password must be same with above ! ..."}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password1')
        user = Firm.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class FirmInfoSerializer(serializers.ModelSerializer):
    username = User._meta.get_field('username').required = False
    class Meta:
        model = Firm
        fields = (
            "id",
            "email",
            "username",
            "firm_name",
            "address",
            "logo",
            "phone_number",
            "website",
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserInfoSerializer(read_only=True)
    firm = FirmInfoSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = (
            "key",
            "user",
            "firm",
        )