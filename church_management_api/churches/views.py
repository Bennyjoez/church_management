from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models

def churches(request):
  churches = models.Church.objects.all()
  return JsonResponse(list(churches.values()), safe=False) #churches

@csrf_exempt
def create_church(request):
  data = json.loads(request.body)

  # verify data
  required_fields = ['name', 'parish', 'description', 'address', 'latitude', 'longitude']
  missing_fields = [field for field in required_fields if not data.get(field)]
  if missing_fields:
    return JsonResponse({'error': f'Missing required fields: {", ".join(missing_fields)}'}, status=400)
  
  name = data.get('name')
  parish = data.get('parish')
  description = data.get('description')
  address = data.get('address')
  latitude = data.get('latitude')
  longitude = data.get('longitude')

  church = models.Church.objects.create(name=name, parish=parish, description=description, address=address, latitude=latitude, longitude=longitude)
  return JsonResponse({'id': church.id})


@csrf_exempt
def edit_church(request, id):
  church = models.Church.objects.get(id=id)
  data = json.loads(request.body)

  for field, value in data.items():
    if hasattr(church, field):
      setattr(church, field, value)

  church.save()
  return JsonResponse({'id': id})

def delete_church(request, id):
  church = models.Church.objects.get(id=id)
  church.delete()
  return JsonResponse({'id': id})
