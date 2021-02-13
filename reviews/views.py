from rest_framework.pagination import LimitOffsetPagination

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 6


class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewLimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(author=user)
