from rest_framework import serializers
from .models import Student

def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("First letter should start's with r")
class StudetSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)    

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validate_data):
        print("Before update:- ",instance.name)
        instance.name = validate_data.get('name',instance.name)
        print("After update:- ",instance.name)
        instance.roll = validate_data.get('roll',instance.roll)
        instance.city = validate_data.get('city',instance.city)
        instance.save()
        return instance

    #Function Level Validation for apply validation on single field.
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object level Validation for apply validation on multiple fields.
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError("City must be Ranchi")
        return data