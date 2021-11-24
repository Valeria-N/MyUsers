from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(_('firstname'), max_length=30)
    lastname = models.CharField(_('lastname'), max_length=30)
    patronymic = models.CharField(_('patronymic'), max_length=30)
    number = PhoneNumberField(_('number'), unique=True)
    address = models.TextField(_('address'), max_length=1000)
    is_private = False

    objects = UserManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['lastname', 'firstname', 'patronymic', 'address']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')

    def get_full_name(self):
        full_name = '%s%s%s' % (self.lastname, self.firstname, self.patronymic)
        return full_name.strip()

    def get_short_name(self):
        return self.firstname

    def __str__(self):
        return str(self.number)


