from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import random
import string


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)
    referral_code = models.CharField(max_length=6, unique=True, null=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='referred_users')

    USERNAME_FIELD = 'phone_number'

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super(User, self).save(*args, **kwargs)



