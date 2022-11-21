from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


from API.serializer import usuarioSerializer
from API.models import Usuario

# Create your views here.
class LoginViewset(APIView):
    def post(self, request):
        emailRecebido = request.data['email']
        senhaRecebida = request.data['senha']

        usuario = Usuario.objects.filter(email=emailRecebido).first()

        if usuario is None:
            raise AuthenticationFailed('Usario nao encontrado')
        
        if not usuario.check_password(senhaRecebida):
            raise AuthenticationFailed('Senha incorreta')

        payload = {
            'id': usuario.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }
        
        tokenDeAutenticacao = jwt.encode(payload, 'secret', algorithm='HS256')

        resposta = Response()
        resposta.set_cookie(key='jwt', value=tokenDeAutenticacao, httponly=True)
        resposta.data = {
            'jwt': tokenDeAutenticacao
        }

        return resposta