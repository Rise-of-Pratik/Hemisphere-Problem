from django.shortcuts import render

from rest_framework import status, generics, serializers as rest_serializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account import models as account_models
# from account import utils as account_utils
# from account.permissions import AddUserPermission, IsCmsUser
# from . import serializers as account_serializers
# from cms.core.pagination import MyCursorPaginationCreatedAtWise
# from cms.image import constants as image_constants
# from webapp.apps import gen_hash, expires

# from datetime import datetime, timedelta
# import pytz
# import logging

from django.http import request
#
# logger = logging.getLogger(__name__)


class Login(APIView):
    """
    This is a login class. Below is the sample curl request.
    curl -H "Content-Type:application/json" -X POST -d '{"email" : "admin@kuliza.com", "password" : "test@123"}' http://localhost:8000/api/account/login/
    ---
    """

    def post(self, request):
        """
        This API logs the user in.with email or phone and a password or access_token(of facebook or google).
        ---
        parameters:
            - name: username
            - name: password
            - name: identity
              required: true
            - name: access_token
        """
        params = {
            "username": request.data.get("username", None),
            "password": request.data.get("password", None),
            "identity": request.data.get("identity", ""),
            "access_token": request.data.get("access_token")
        }
        # result = account_utils.login(params, request)
        return True#api_utils.response(data={'message': result['message']}, code=status.HTTP_200_OK, request=request)


class Logout(APIView):
    """
        This is a logout class. Below is the sample curl request.
        curl -H "Content-Type:application/json" -X POST -d '{"access_token" : "XXX"}' http://localhost:8000/api/account/logout/
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        This API logs the user out.
        ---
        """
        return True
        # if account_utils.logout(request):
        #     return api_utils.response(data={"message": "User logged out successfully."}, code=status.HTTP_200_OK, request=request)
        # else:
        #     raise GenericException(status_type=STATUS_TYPE["APP"], exception_code=NONRETRYABLE_CODE["BAD_REQUEST"], detail="Some error occurred. Please try again in sometime.", request=request)
