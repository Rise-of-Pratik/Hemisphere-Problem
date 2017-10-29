from django.contrib.auth.models import UserManager
from random import randint


# class CustomUserManager(UserManager):
#     """
#         This class is necessary to create if using custom user model is desired
#     """
#
#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         """
#             Creates and saves a User with the given username, email and password.
#         """
#         email = self.normalize_email(email)
#         # extra_fields['username'] = extra_fields['username'] if extra_fields.get('username') else email
#         user = self.model(email=email, is_staff=is_staff, is_active=True, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, *args, **kwargs):
#         """
#         :param args:
#         :param kwargs:
#         :return: creates a super user
#         """
#         # if 'is_cms_user key' is present it means createcmsuser command has been executed
#         if account_constants.CMS_SUPERUSER_KEY in kwargs:
#             # this has been imported over here to take care of circular import
#             from .models import OurGroup
#             phone = ''.join(["%s" % randint(0, 9) for num in range(0, account_constants.MOBILE_NUMBER_LENGTH)])
#             u = self.create_user(kwargs['email'], password=kwargs['password'], phone=phone)
#             role_name = account_constants.ROLES.get(account_constants.CMS_USER)
#             u.permissions['roles'] = [role_name]
#             writer_group, writer_created = OurGroup.objects.get_or_create(name=account_constants.WRITER)
#             admin_group, admin_created = OurGroup.objects.get_or_create(name=account_constants.ADMIN)
#             approver_group, approver_created = OurGroup.objects.get_or_create(name=account_constants.APPROVER)
#             u.groups.add(writer_group.id, admin_group.id, approver_group.id)
#         else:
#             u = self.create_user(kwargs['email'], password=kwargs['password'])
#         u.username = kwargs['email']
#         u.is_staff = True
#         u.save(using=self._db)
#         return u
#
#     def create_user(self, email, password=None, **extra_fields):
#         return self._create_user(email, password, False, False, **extra_fields)
