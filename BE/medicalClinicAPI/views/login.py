from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        next_url = request.GET.get("next", "/")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                refresh_token = RefreshToken.for_user(user)
                access_token = str(refresh_token.access_token)
                if next_url == "/":
                    return Response({"message": "Login successful.", "access_token": access_token, "refresh_token": str(refresh_token)}, status=status.HTTP_200_OK)

                return Response({"message": "Login successful.", "access_token": access_token, "refresh_token": str(refresh_token), "next": next_url}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Email or password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Please fill in all fields."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
