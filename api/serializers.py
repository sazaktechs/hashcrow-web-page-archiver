'''
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily rendered into 
JSON, XML or other content types. 

Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, 
after first validating the incoming data.
'''
from rest_framework import serializers
from .models import SnapShot, Hash, Url 

class SnapShotSerializer(serializers.ModelSerializer):
    ''' SnapShot Serializer '''
    class Meta:
        ''' Serialize html and created_date '''
        model = SnapShot
        fields = ['created_date'] # 'html', 

class HashSerializer(serializers.ModelSerializer):
    ''' Hash Serializer '''
    content = SnapShotSerializer(many=True, read_only=True)

    class Meta:
        ''' Serialize hash and content '''
        model = Hash
        fields = ['hash', 'content'] 

class UrlSerializer(serializers.ModelSerializer):
    ''' Url Serializer '''
    snapshots = HashSerializer(many=True, read_only=True)
    class Meta:
        ''' Serialize url and snapshots'''
        model = Url
        fields = ['code','url','snapshots']
