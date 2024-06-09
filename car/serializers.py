from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):

    is_available = serializers.BooleanField(
        default=True # anonymous userlar için..
        )

    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability',
            'is_available',
        )
# 1. Yol;
    # Bu method u override etmek yerine staff ve normal userlar için ayrı ayrı serializerlar oluşturulup
    # View de get_serializer_class methode u override edilerek user a göre serializerlar seçilebilir.
    def get_fields(self):
        fields = super().get_fields() # superindeki tüm fieldları al
        request = self.context.get('request') # context içindeki request i al. O anki user bilgisi requestin içinde var.
        
        # if request.user and not request.user.is_staff: # user var ve o user staff değil ise:
        #     fields.pop('availability') # availability field ını çıkar
        #     fields.pop('plate_number') # plate_number field ını çıkar
        # return fields  # if bloğuna girmezse tüm fieldları dön. user var ve o user staff ise superdeki tüm fieldları dön.

        if request.user and not request.user.is_staff: # user var ve o user staff değil ise:
            fields.pop('availability') # availability field ını çıkar
            fields.pop('plate_number') # plate_number field ını çıkar
        return fields  # if bloğuna girmezse tüm fieldları dön. user var ve o user staff ise superdeki tüm fieldları dön.


'''
# 2. Yol;
class CarStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability',
        )

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
        )
'''


class ReservationSerializer(serializers.ModelSerializer):
    
    total_price = serializers.SerializerMethodField(method_name='toplam') # method name tanımlanırsa aşağıda o isimle çağırabiliriz, tanımlamaz isek def get_total_price() olarak çağırmamız gerekir.
    # total_prize = serializers.SerializerMethodField()
    
    class Meta:
        model = Reservation
        fields = (
            'id',
            'customer',
            'car',
            'start_date',
            'end_date',
            'total_price',
        )
        # Modeldeki kısıtlamanın hata/crash vermemesi için; 
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Reservation.objects.all(),
                fields=('customer', 'start_date', 'end_date',),
                message=('You already have a reservation between these dates...')
            )
        ]
    
    def toplam(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days
    # def get_total_price(self, obj):
    #     return obj.car.rent_per_day * (obj.end_date - obj.start_date).days

