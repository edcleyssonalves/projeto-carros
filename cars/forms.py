from django import forms
from cars.models import Brand, Car

       
class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is None:
            self.add_error('value', 'Insira o valor do carro para prosseguir com o cadastro')
        elif value < 20000:
            self.add_error('value', 'O valor do veículo deve ser superior a R$20.000')
        return value
    
    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        print(plate)
        if not plate:
            self.add_error('plate', 'Insira a placa do carro para prosseguir com o cadastro')
        return plate
            
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo: 
            self.add_error('photo', 'Insira uma foto do carro para prosseguir com o cadastro')
        return photo