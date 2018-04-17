from django.db import models
from base.models import Base
from users.models import User


class StoreCategory(Base):
    title = models.CharField(max_length=50)

class Store(Base):
    title = models.CharField(max_length=100)
    description = models.TextField()
    store_related_category = models.ForeignKey(StoreCategory, related_name="store_related_category_name", on_delete=models.CASCADE)
    store_related_owner = models.ForeignKey(User, related_name="store_related_owner_name", on_delete=models.CASCADE, blank=True, null=True)
    store_related_user = models.ForeignKey(User, related_name='store_related_user_name', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)


class StoreVisit(Base):
    store_visit_related_store = models.ForeignKey(Store, related_name='store_visit_related_store', on_delete=models.CASCADE)
    store_visit_related_user = models.ForeignKey(User, related_name='store_visit_related_user', on_delete=models.CASCADE)
