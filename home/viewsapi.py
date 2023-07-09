from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
class login_view(APIView):
    def post(self, request):
        response ={}
        response['status'] = 200
        response['message'] = 'something went wrong'
        try:
            data = request.data 
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            check_user =User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'invalid username not found'
                raise Exception(' username not found')
            user_obj = authenticate(username = data.get('username'), password=data.get('password'))
            if user_obj:
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password found'
                raise Exception(' password not found')
        except Exception as e:
            print(e)
        return Response(response)
login_view = login_view.as_view()
class register_view(APIView):
    def post(self, request):
        response ={}
        response['status'] = 200
        response['message'] = 'something went wrong'
        try:
            data = request.data 
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            if data.get('password') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            check_user =User.objects.filter(username = data.get('username')).first()
            if check_user:
                response['message'] = ' username is already exist not found'
                raise Exception(' usernam is already taken')
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message'] = 'user created'
            response['status']  = 200
            return Response(response)
        except Exception as e:
            print(e)
register_view = register_view.as_view()