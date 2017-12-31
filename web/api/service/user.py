from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


def deleteToken(user):
    """
    delete token of the user from database

    :param user: the requester
    """
    try:
        token = Token.objects.get(user=user)
        if token:
            token.delete()
    except Exception:
        pass


def refreshToken(user):
    """
    refresh token of the user

    :param user: the requester
    :return: just created token for the user
    """
    deleteToken(user)
    return Token.objects.create(user=user)
