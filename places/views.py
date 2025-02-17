from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def index(request):
    places = []
    db_places = Place.objects.all()
    for place in db_places:
        places.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places:place_details', args=[place.id])
                }
            }
        )
    context = {
        'geojson': {
            'type': 'FeatureCollection',
            'features': places
        }
    }
    return render(request, 'index.html', context)


def place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)

    data = {
        'title': place.title,
        'imgs': [object.image.url for object in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        },

    }

    return JsonResponse(data)
