from rest_framework import status
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response


from users.models import UserSerializer

@api_view(http_method_names=['POST'])
def user_list(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
