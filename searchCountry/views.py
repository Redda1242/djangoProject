from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.shortcuts import render

from .models import Country


from django.shortcuts import render

def home(request):
    # Logic for your home page
    return render(request, 'nearby_countries_form.html')

def map_view(request):
    # Logic for your map page
    return render(request, 'map.html')


def find_nearby_countries(request):
    # Ensure the input types are correct
    lat = float(request.GET['lat'])
    lon = float(request.GET['lon'])
    distance = float(request.GET['distance'])  # Assume distance is in meters

    current_point = Point(lon, lat, srid=4326)

    # Query for nearby countries
    nearby_countries = Country.objects.filter(
        mpoly__dwithin=(current_point.transform(3857, clone=True), distance)
    ).annotate(
        distance=Distance('mpoly', current_point.transform(3857, clone=True))
    ).order_by('distance')

    # Serialize the results into a list of dictionaries
    results = [
        {
            'name': country.name,
            'distance': country.distance.m  # Convert the distance to meters
        } for country in nearby_countries
    ]

    # Return a JsonResponse
    return JsonResponse(results, safe=False)

