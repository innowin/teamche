from rest_framework.serializers import ModelSerializer
from base.serializers import BaseSerializer, ReadOnlyField
from .models import (
    StoreCategory,
    Store,
    StoreVisit
)
from users.models import User


class UserDetailSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class StoreCategorySerializer(BaseSerializer):
    image = ReadOnlyField()

    class Meta:
        model = StoreCategory
        fields = '__all__'


class StoreDetailSerializer(BaseSerializer):
    store_related_category = StoreCategorySerializer()
    images = ReadOnlyField()
    store_related_owner = UserDetailSerializer()
    store_related_user = UserDetailSerializer()

    class Meta:
        model = Store
        fields = '__all__'


class StoreSerializer(BaseSerializer):
    image = ReadOnlyField()
    bookmark = ReadOnlyField()

    class Meta:
        model = Store
        fields = '__all__'
        extra_kwargs = {
          'store_related_user': { 'read_only': True }
        }


class StoreVisitDetailSerializer(BaseSerializer):
    store_visit_related_user = UserDetailSerializer()

    class Meta:
        model = StoreVisit
        fields = '__all__'


class StoreVisitSerializer(BaseSerializer):
    class Meta:
        model = StoreVisit
        fields = '__all__'
        extra_kwargs = {
          'store_visit_related_user': { 'read_only': True }
        }
