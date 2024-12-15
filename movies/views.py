import random
from django.shortcuts import render
from .models import Serial, Kinolar, Serial_item, Multfilm, Anime_item, Anime
from .serializers import SerialSerializer, KinolarSerializer, SerialItemSerializer, MultfilmSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# bu yerda qiziqarli bolishi uchun random orqali kinolarni chaqiramiz
ratings = [1, 2, 3, 4, 5]


def Index(reuqest):
    kinolars = Kinolar.objects.all()
    serials = Serial.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:2])
    random_multfilms = multfilms.order_by('?'[:2])
    random_movies = [random_kinolars, random_serials, random_multfilms]
    select_movies = random.choice(random_multfilms)

    ratings = [1, 2, 3, 4, 5]
    return render(reuqest, 'index.html',
                  {'ratings': ratings, 'kinolars': kinolars, 'serials': serials,
                   'select_movies': select_movies,
                   'multfilms': multfilms})


def Kinolar_views(request):
    kinolars = Kinolar.objects.all()
    serials = Serial.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:2])
    random_multfilms = multfilms.order_by('?'[:2])
    random_movies = [random_kinolars, random_serials]
    select_movies = random.choice(random_multfilms)
    return render(request, 'kino.html', {'kinolars': multfilms, 'select_movies': select_movies, 'ratings': ratings})


def Multfilimlar_views(request):
    kinolars = Kinolar.objects.all()
    serials = Serial.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:2])
    random_multfilms = multfilms.order_by('?'[:2])
    random_movies = [random_kinolars, random_serials]
    select_movies = random.choice(random_multfilms)
    return render(request, 'multfilm.html',
                  {'multfilims': multfilms, 'select_movies': select_movies, 'ratings': ratings})


def Seriallar_views(request):
    kinolars = Kinolar.objects.all()
    serials = Serial.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:2])
    random_multfilms = multfilms.order_by('?'[:2])
    random_movies = [random_kinolars, random_serials]
    select_movies = random.choice(random_multfilms)
    return render(request, 'serial.html', {'serials': serials,
                                           'select_movies': select_movies,
                                           'ratings': ratings})


def Animelar_views(request):
    kinolars = Kinolar.objects.all()
    animes = Anime.objects.all()
    anime_item = Anime_item.objects.all()
    serials = Serial.objects.all()
    multfilms = Multfilm.objects.all()
    random_kinolars = kinolars.order_by('?'[:2])
    random_serials = serials.order_by('?'[:2])
    random_multfilms = multfilms.order_by('?'[:2])
    random_movies = [random_kinolars, random_serials]
    select_movies = random.choice(random_multfilms)
    return render(request, 'anime.html',
                  {'animes': animes,
                   'anime_item': anime_item,
                   'select_movies': select_movies,
                   'ratings': ratings})


class KinoListApi(APIView):
    def get(self, request):
        kino = Kinolar.objects.all()
        serializer = KinolarSerializer(kino, many=True)
        return Response(serializer.data)  # Response qoidaga muvofiq

    def post(self, request):
        serializer = KinolarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Response qoidaga muvofiq
        return Response(serializer.errors, status=400)  # Errorni 400 status bilan qaytarish


class KinoDetailApi(APIView):
    def get(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)
        serializer = KinolarSerializer(kino)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)
        serializer = KinolarSerializer(instance=kino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            kino = Kinolar.objects.get(id=pk)
            kino.delete()
            return Response({'deleted': True})
        except Kinolar.DoesNotExist:
            return Response({'error': 'Kino not found'}, status=404)


class SerialListApi(APIView):
    def get(self, request):
        serial = Serial.objects.all()
        serializer = SerialSerializer(serial, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SerialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SerialDetailApi(APIView):
    def get(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)
        serializer = SerialSerializer(serial)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)
        serializer = SerialSerializer(instance=serial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            serial = Serial.objects.get(id=pk)
            serial.delete()
            return Response({'deleted': True})
        except Serial.DoesNotExist:
            return Response({'error': 'Serial not found'}, status=404)


class SerialItemApi(APIView):
    def get(self, request, pk):
        serial_items = Serial_item.objects.filter(serial_id=pk)
        serializer = SerialItemSerializer(serial_items, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = SerialItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class SerialItemDetailApi(APIView):
    def get(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)
        serializer = SerialItemSerializer(serial_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)
        serializer = SerialItemSerializer(instance=serial_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            serial_item = Serial_item.objects.get(id=pk)
            serial_item.delete()
            return Response({'deleted': True})
        except Serial_item.DoesNotExist:
            return Response({'error': 'Serial item not found'}, status=404)


class MultfilmListApi(APIView):
    def get(self, request):
        multfilm = Multfilm.objects.all()
        serializer = MultfilmSerializer(multfilm, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MultfilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class MultfilmDetailApi(APIView):
    def get(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)
        serializer = MultfilmSerializer(multfilm)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)
        serializer = MultfilmSerializer(instance=multfilm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            multfilm = Multfilm.objects.get(id=pk)
            multfilm.delete()
            return Response({'deleted': True})
        except Multfilm.DoesNotExist:
            return Response({'error': 'Multfilm not found'}, status=404)
