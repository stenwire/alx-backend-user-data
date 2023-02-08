#!/usr/bin/env python3
"""
Route module to manage the API authentication
"""
import re
from flask import request
from typing import List
from typing import TypeVar


def format_path(path: List[str]) -> List:
    """formats path string
    """
    if isinstance(path, list):
        p = ''.join(str(x) for x in path)
        result = re.split('|/|', p)
    else:
        result = re.split('|/|', path)
    while ("" in result):
        result.remove("")
    return result


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """secures a route
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if format_path(path) == format_path(excluded_paths):
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """adds authorization header to request body
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """checks for current user
        """
        return None
