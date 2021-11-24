from django.contrib.auth.base_user import BaseUserManager
#from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, number, password, **extra_fields):

        if not number:
            raise ValueError('The given email must be set')
        number = self.normalize_email(number)
        #number = PhoneNumberField(number) ???????
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(number, password, **extra_fields)

    def create_superuser(self, number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(number, password, **extra_fields)

