from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'



# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     # url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='pk')

#     class Meta:
#         model = Book
#         fields = ['url','id','title','author']
#         # extra_kwarg = {'url':{'view_name':'book-detail','lookup_field':'id'}}