from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Car, Reservation
from .serializers import CarSerializer,ReservationSerializer
from .permissions import IsStaffOrReadOnly
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.utils import timezone

# for dinamic is_available field 
from django.db.models import Exists, OuterRef


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsStaffOrReadOnly,)  # [IsStaffOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(availability=True)

        start = self.request.query_params.get('start')
        # print(start)
        end = self.request.query_params.get('end')
        # print(end)
        
        if start is not None or end is not None:

            cond1 = Q(start_date__lt=end) 
            cond2 = Q(end_date__gt=start)
            # veya;
            # not_available = Reservation.objects.filter(
            #     start_date__lt=end, end_date__gt=start
            #     ).values_list('car_id', flat=True) # [1,2]

            # veya;
            # not_available = Reservation.objects.filter(
            #     Q(start_date__lt=end) & Q(end_date__gt=start)
            #     ).values_list('car_id', flat=True) # [1,2]
            
            '''
            #! Static available field:
            # cond1 ve cond2 ye göre Reservation object'lerini filtrele, values'lerinden 'car_id' lerini liste halinde ver! 
            not_available = Reservation.objects.filter(
                cond1 & cond2
                ).values_list('car_id', flat=True) # [1,2]
            # print(not_available)
        
            # not_available içindeki car ların id'leri, queryset içindeki id'lere eşit olanları, queryset'ten çıkar/exclude et!
            queryset = queryset.exclude(id__in=not_available)
            '''
                      
            #! Dinamic is_available field:
            queryset = queryset.annotate(
                is_available=~Exists(Reservation.objects.filter(
                Q(car=OuterRef('pk')) & Q(start_date__lt=end) & Q(end_date__gt=start) # Bir üst modeldeki pk leri eşleştir ve cond1 ve cond 2'yi eşleştir.
                ))       
            )
            
        return queryset

'''
    # 2. Yol;
    def get_serializer_class(self):
        from .serializers import CarStuffSerializer, CarSerializer
        if self.request.user.is_staff:
            return CarStuffSerializer
        else:
            return CarSerializer
'''     


class ReservationView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)
    
    '''
    def create(self, request, *args, **kwargs):
        contidion: Eğer user'ın reservation yapmak istediği tarih ile kesişen bir reservasyonu var ise, measaj dön ve yeni bir reservation create etmesine mani ol! 
    '''
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return super().get_queryset().filter(customer=self.request.user)
    

class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    # lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # validse datayı dön, değilse hataları/errorları raise et.
        serializer.is_valid(raise_exception=True)
        
        end = serializer.validated_data.get('end_date')
        car = serializer.validated_data.get('car')
        start = instance.start_date # update edilecek instanceın start_date i
        today = timezone.now().date()

        if Reservation.objects.filter(car=car).exists(): # Bu car a ait reservation var mı?
            # a = Reservation.objects.filter(car=car, end_date__gte=today)
            # print(len(a))    
            
            for reserv in Reservation.objects.filter(car=car, end_date__gte=today):
                if start < reserv.start_date < end:
                    return Response({'message': 'Car is not available...'}) # eğer if bloğuna girerse burasını return et. (update yapma mesajı döndür!)

        return super().update(request, *args, **kwargs) # eğer if bloğuna girmezse burasını return et. (Normal olarak update yap!)



    
