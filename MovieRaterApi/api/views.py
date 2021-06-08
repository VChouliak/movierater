from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

from django.contrib.auth.models import User


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        response = {'message': 'its working'}
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = User.objects.get(id=1)  #request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {
                    'message': 'Rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user,
                                               movie=movie,
                                               stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {
                    'message': 'Rating created',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_201_CREATED)

        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer