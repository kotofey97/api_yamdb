from django.contrib.auth.tokens import default_token_generator
from django.db.models import query 
from django.shortcuts import get_object_or_404 
from django.core.mail import send_mail 
from rest_framework import permissions, serializers, status, viewsets 
from rest_framework.decorators import action, api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdmin
from api_yamdb import settings 


@api_view(['POST']) 
@permission_classes([permissions.AllowAny])
def get_confirmation_code(request): 
    if not User.objects.filter(email=request.data['email']).exists(): 
        return Response(status=status.HTTP_204_NO_CONTENT) 
    user = get_object_or_404(User, email=request.data['email']) 
    confirmation_code = default_token_generator.make_token(user) 
    send_mail( 
        'Код подтверждения YaMDb', 
        f'Ваш код подтверждения: {confirmation_code}', 
        settings.DEFAULT_FROM_EMAIL, 
        [f'{request.data["email"]}'], 
        fail_silently=False, 
    )
    return Response({'Код подтверждения выслан на указанный адрес'}, 
                status=status.HTTP_200_OK)

@api_view(['POST']) 
@permission_classes([permissions.AllowAny]) 
def get_token(request): 
    email = request.data['email'] 
    user = get_object_or_404(User, email=email) 
    confirmation_code = request.data['confirmation_code'] 
    if not default_token_generator.check_token(user, confirmation_code): 
        return Response(status=status.HTTP_403_FORBIDDEN) 
    token = AccessToken.for_user(user) 
    return Response({'token': str(token)}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    
    @action(methods=['patch', 'get'], detail=False, 
            permission_classes=[permissions.IsAuthenticated]) 
    def me(self, request): 
        if request.method == 'GET': 
            serializer = UserSerializer(self.request.user) 
        else: 
            serializer = UserSerializer(self.request.user, 
                                        data=request.data, partial=True) 
            serializer.is_valid(raise_exception=True) 
            serializer.save() 
        return Response(serializer.data)