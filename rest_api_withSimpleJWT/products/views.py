from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from .serializers import ProductSerializer
from . models import Product






class CreateProductAPIView(CreateAPIView):
    '''
    Method: POST
    URL: http://127.0.0.1:8000/product/create/
    AUTHORIZATION BEARER TOKEN: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4ODE1ODY1LCJpYXQiOjE2Mzg4MTIyNjUsImp0aSI6IjYzOGFiMDY5OWFmZjQ4NmE4NzFmNmExMzI1MTc4NzlhIiwidXNlcl9pZCI6OH0.4Wjw27PvyLBUoAp2fFbx66us94BcI177PAhWgHFxj_g
    REQUEST PARAMETER: {
                            "name":"Bajaj Pulsar 150",
                            "price":125000,
                            "stock_count":7
                        }
    Response :{
                "name": "Bajaj Pulsar 150",
                "price": 125000,
                "stock_count": 7
                }
    '''


    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

class ProductListAPIView(ListAPIView):
    '''
        Method: GET
        URL: http://127.0.0.1:8000/product/list/
        AUTHORIZATION BEARER TOKEN: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4ODE1ODY1LCJpYXQiOjE2Mzg4MTIyNjUsImp0aSI6IjYzOGFiMDY5OWFmZjQ4NmE4NzFmNmExMzI1MTc4NzlhIiwidXNlcl9pZCI6OH0.4Wjw27PvyLBUoAp2fFbx66us94BcI177PAhWgHFxj_g

        Response :{
                "count": 8,
                "next": "http://127.0.0.1:8000/product/list/?page=2",
                "previous": null,
                "results": [
                    {
                        "name": "One Plus 9",
                        "price": 50000,
                        "stock_count": 5
                    },
                    {
                        "name": "Apple Iphone 12",
                        "price": 55000,
                        "stock_count": 9
                    },
                    {
                        "name": "Apple Airpods",
                        "price": 10000,
                        "stock_count": 15
                    },
                    {
                        "name": "dell Inspiron 5567",
                        "price": 55999,
                        "stock_count": 778
                    },
                    {
                        "name": "Apple Macbook Air",
                        "price": 105999,
                        "stock_count": 53
                    }
                ]
            }
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_view_name(self):
        return super().get_queryset()


class ProductDetailAPIView(RetrieveAPIView):
    '''
    Method: POST
    URL: http://127.0.0.1:8000/product/create/
    AUTHORIZATION BEARER TOKEN: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4ODE1ODY1LCJpYXQiOjE2Mzg4MTIyNjUsImp0aSI6IjYzOGFiMDY5OWFmZjQ4NmE4NzFmNmExMzI1MTc4NzlhIiwidXNlcl9pZCI6OH0.4Wjw27PvyLBUoAp2fFbx66us94BcI177PAhWgHFxj_g
    Response :{
                            "name": "One Plus 9",
                            "price": 50000,
                            "stock_count": 5
             }
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_view_name(self):
        return super().get_queryset()

