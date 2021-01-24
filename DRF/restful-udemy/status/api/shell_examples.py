from status.api.serializers import StatusSerializer
from status.models import Status

# new record in database using serializer
data = {'user': 1, 'content': 'Some content'}
serializer = StatusSerializer(data=data)
if serializer.is_valid():
    serializer.save()



# update reacord in database using serializer
obj = Status.objects.last()
data = {'user': 1, 'content': 'Some new content'}
update_serializer = StatusSerializer(instance=obj, data=data)
if update_serializer.is_valid():
    update_serializer.save()


# serializer jako walidator
from rest_framework import serializers

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()

sent_data = {"content": "ble ble ble", "email": "wk@op.pl"}
create_serializer = CustomSerializer(data=sent_data)
if create_serializer.is_valid():
    new_data = create_serializer.data
    print(new_data)

