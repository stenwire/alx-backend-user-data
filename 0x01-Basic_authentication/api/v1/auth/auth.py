#!/usr/bin/env python3
"""
Route module to manage the API authentication
"""
from flask import request
from typing import List
from typing import TypeVar


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """secures a route
        """
        return False

    def authorization_header(self, request=None) -> str:
        """adds authorization header to request body
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """checks for current user
        """
        return None
