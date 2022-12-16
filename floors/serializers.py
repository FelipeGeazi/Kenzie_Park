from rest_framework import serializers
from .models import Floor, Spot, SpotType
import ipdb

"""
    # 2. Criar as vagas de carro
    for _ in range(car_spots_qnt):
        Spot.objects.create(variety=SpotType.CAR, floor=floor_obj)

    # 3. Criar as vagas de moto
    for _ in range(motorcycle_spots_qnt):
        Spot.objects.create(variety=SpotType.MOTORCYCLE, floor=floor_obj)

    for _ in range(car_spots_qnt):
            Spot.objects.create(variety=SpotType.CAR, floor=floor_obj)

    # insert rodado 10k
    INSERT INTO floors_spot VALUES ('car', 1)

    # bulk
    INSERT INTO floors_spot VALUES
    ('car', 1)
    ('car', 1)
    ('car', 1)
    ('car', 1)
    ('car', 1)
    ('car', 1)
    ('car', 1)
    x 10k
"""


class FloorSerializer(serializers.ModelSerializer):
    motorcycle_spots = serializers.IntegerField(write_only=True)
    car_spots = serializers.IntegerField(write_only=True)
    spots_count = serializers.SerializerMethodField()

    def get_spots_count(self, obj: Floor):
        car_spots = obj.spots.filter(variety=SpotType.CAR).count()
        motorcycle_spots = obj.spots.filter(variety=SpotType.MOTORCYCLE).count()

        return {
            "car_spots": car_spots,
            "motorcycle_spots": motorcycle_spots,
        }

    def create(self, validated_data: dict) -> Floor:
        # ipdb.set_trace()
        car_spots_qnt = validated_data.pop("car_spots")
        motorcycle_spots_qnt = validated_data.pop("motorcycle_spots")

        # 1. Criar o piso antes para criar as vagas para ele depois
        floor_obj = Floor.objects.create(**validated_data)

        car_objects = [
            Spot(variety=SpotType.CAR, floor=floor_obj) for _ in range(car_spots_qnt)
        ]
        motorcyle_objects = [
            Spot(variety=SpotType.MOTORCYCLE, floor=floor_obj)
            for _ in range(motorcycle_spots_qnt)
        ]

        # Spot.objects.bulk_create(car_objects)
        # Spot.objects.bulk_create(motorcyle_objects)
        Spot.objects.bulk_create(car_objects + motorcyle_objects)

        return floor_obj

    class Meta:
        model = Floor
        fields = [
            "id",
            "name",
            "spot_priority",
            "parking_lot",
            "motorcycle_spots",
            "car_spots",
            "spots_count",
        ]
        read_only_fields = [
            "parking_lot",
        ]
