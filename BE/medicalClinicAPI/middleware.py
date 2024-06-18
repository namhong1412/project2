import os
import jwt
from datetime import datetime
from django.http import JsonResponse
from django.utils.html import escape

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response:
            return response
        return self.get_response(request)

    def process_request(self, request):
        # Allow access to 'login' and 'signup' views without authentication
        if request.path_info.endswith("/login/") or request.path_info.endswith("/signup/"):
            return None

        # Check Authorization header for JWT token
        authorization = request.headers.get("Authorization")
        if not authorization:
            return JsonResponse({"error": "Authorization header missing"}, status=401)

        try:
            # Extract token from 'Bearer <token>' format
            token = authorization.split()[1]
            # Verify JWT token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
            # Add user information to request for use in views if needed
            request.user_id = decoded_token.get('user_id')
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return None
