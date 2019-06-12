from django import forms
from .models import Platinum




class PlatinumForm(forms.ModelForm):
    class Meta:
        model = Platinum
        fields = '__all__'
        exclude=('Booking_id',)
        depth=2

    def clean(self):
        cleaned_data=super().clean()
        room_number=cleaned_data['Room_number']
        query=Platinum.objects.filter(Room_number=room_number)
        if query.exists():
            raise forms.ValidationError("This Room is Already Booking")