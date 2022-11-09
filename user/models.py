from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Firm(User):
    # username = models.CharField(
    #     unique=False,
    #     default="",
    #     max_length=50
    # )
    firm_name = models.CharField(max_length=50)
    logo = models.URLField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "firms"


    def save(self, *args, **kwargs):
        if self.username is None:
            self.username = "string_temmp"
            self.save(commit=False)
            self.username = self.firm_name
            # self.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.firm_name

class UserInfo(User):
    GENDER = (
        ("F", "FEMALE"),
        ("M", "MALE"),
        ("O", "OTHER"),
        ("NM", "NOTMENTIONED"),
    )
    gender = models.CharField(max_length=2, choices=GENDER, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "userInfos"

    def __str__(self):
        return self.username