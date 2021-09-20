from rest_framework import serializers     
from rest_framework.serializers import(     
HyperlinkedIdentityField,ModelSerializer,SerializerMethodField)
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

CHOICES=(
    ("Driver","Driver"),
    ("Customer","Customer"),
    ("Consumer","Consumer")
)

class CustomRegisterSerialize(RegisterSerializer):
    last_name = serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    type = serializers.ChoiceField(choices=CHOICES,required=True)
    # image=serializers.ImageField(required=True)      
    def get_cleaned_data(self):
        super(CustomRegisterSerialize,self).get_cleaned_data()
        return {
            'email': self.validated_data.get('email'),
            'type': self.validated_data.get('type'),
            'last_name': self.validated_data.get('last_name'),
            'password1': self.validated_data.get('password1'),
            # 'image': self.validated_data.get('image')
        }
    def save(self, request):
        user = super().save(request)
        user.username=self.data.get("username")
        user.last_name=self.data.get("last_name")
        user.first_name=self.data.get("username")
        user.save()
        myacount=user.account
        # print(self.data.get("image") )
        myacount.type=self.data.get("type") 
        # myacount.image=self.data.get("image") 
        # print(myacount.image)
        myacount.save()
        # user.save()
        return user          
    
class CustomLoginSerializer(LoginSerializer):
    # first_name = serializers.CharField(required=True)
    # last_name = serializers.CharField(required=True)
    # profile = serializers.IntegerField(required=True)

    def get_cleaned_data(self):
        super(CustomLoginSerializer,self).get_cleaned_data()
        return {
            # 'first_name': self.validated_data.get('first_name', ''),
            # 'last_name': self.validated_data.get('last_name', ''),
            # 'email': self.validated_data.get('email', ''),
            # 'password1': self.validated_data.get('password1', ''),
            # 'id': self.validated_data.get('id', ''),
            # 'profile': self.validated_data.get('profile','')
        }
    def save(self, request):
        user = super().save(request)
        # user.profile = self.data.get('profile')
        # user.save()
        return user