from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(email=request.GET['email']).values()
        except User.DoesNotExist:
            user = {}
        return Response(user)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        User.objects.create(email=email, first_name=first_name, last_name=last_name)
        return Response('User created')


@api_view(('GET',))
def hello_world(request):
    return Response('Hello world')


@api_view(('GET',))
def health_check(request):
    return Response('Status: OK')
