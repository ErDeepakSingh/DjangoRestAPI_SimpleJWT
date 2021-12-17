from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.utils.translation import ugettext as _
from django.utils import timezone, translation
from django.db.models import Q
from .response import Response as response

from .models import MyUser


class CustomUserSignup(APIView):
    '''
    Method: POST
    URL: http://127.0.0.1:8000/api/user/sign_up/
    REQUEST PARAMETER: {
                        "email":"harshitjain@gmail.com",
                        "username":"harshitjain",
                        "password": "pass@123"
                            }
    Response :{
                    "error": 0,
                    "code": 1,
                    "data": {
                        "email": "harshitjain@gmail.com",
                        "username": "harshitjain"
                    },
                    "msg": "Your account has been created successfully"
                }
    '''

    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(response.parsejson(_("Your account has been created successfully"), json,  status=status.HTTP_201_CREATED))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomUserLogin(APIView):
    '''
    Method: POST
    URL: http://127.0.0.1:8000/api/user/
    REQUEST PARAMETER: {
                        "email":"harshitjain@gmail.com",
                        "password": "pass@123"
                        }
    Expected Response :{
                        "error": 0,
                        "code": 1,
                        "data": {
                            "id": 10,
                            "email": "harshitjain@gmail.com",
                            "username": "harshitjain",
                            "last_login": "2021-12-07T02:56:07.551105Z",
                            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTQ1MDU2NywiaWF0IjoxNjM4ODQ1NzY3LCJqdGkiOiJmNjhlM2Y4NzgxMTc0YmZlODhmM2VhN2YzY2ExMDJjYSIsInVzZXJfaWQiOjEwfQ.DRWr_bZB68XJnHZ7jeIICiYh18IbOmwSuRaLy9TWMqs",
                            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4ODQ5MzY3LCJpYXQiOjE2Mzg4NDU3NjcsImp0aSI6IjY1MWM3Y2E1YWIyYjQ1NDM4YTA4MzNmMjliZGMyOWU1IiwidXNlcl9pZCI6MTB9.6PMjNd9_jRW8rqEF72SxCWMGmG0-XdNw3xBLDZY3zEQ"
                        },
                        "msg": "Login successfully"
                    }
    '''

    def post(self, request):
        if "email" in request.data and request.data['email'] != "":
            email = request.data.get('email')
            try:
                print(email)
                userObj = MyUser.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
            except Exception:
                return Response(response.parsejson(_("Email/Username does not exist"), "", status=404))
        else:
            return Response(response.parsejson(_("Email/Username is required"), {}, status=404))

        if "password" in request.data and request.data['password'] != "":
            password = request.data.get('password')
        else:
            return Response(response.parsejson(_("password is required"), {}, status=404))

        if (not userObj.check_password(password)):
            return Response(response.parsejson(_("Email/Username or password do not match"), "",status=status.HTTP_404_NOT_FOUND))

        if userObj.is_active == False:
            return Response(response.parsejson(_("Your account is inactive state, Please contact to administrator"), {}, status=404))

        userObj.last_login = timezone.now()
        userObj.save(update_fields=['last_login'])

        serialized_user = UserSerializer(userObj).data
        __resultlist = dict(UserSerializer(userObj).data.items())

        refresh = RefreshToken.for_user(userObj)
        __resultlist['refresh'] = str(refresh)
        __resultlist['access'] = str(refresh.access_token)
        return Response(response.parsejson(_("Login successfully"),__resultlist, 201))


class BlacklistTokenUpdateView(APIView):
    '''
    Method: POST
    URL: http://127.0.0.1:8000/api/user/
    REQUEST PARAMETER: {
                        "refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTQ1MDU2NywiaWF0IjoxNjM4ODQ1NzY3LCJqdGkiOiJmNjhlM2Y4NzgxMTc0YmZlODhmM2VhN2YzY2ExMDJjYSIsInVzZXJfaWQiOjEwfQ.DRWr_bZB68XJnHZ7jeIICiYh18IbOmwSuRaLy9TWMqs"
                        }
    Expected Response :{
                    "error": 0,
                    "code": 0,
                    "data": {},
                    "msg": "You have been logged out successfully"
                        }
    '''

    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(response.parsejson(_("You have been logged out successfully"), {},status=status.HTTP_205_RESET_CONTENT))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)