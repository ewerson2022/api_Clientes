from clientes.models import Cliente
from rest_framework import serializers
from clientes.validators import *

# classe responsavel por hedar as validações assim mantendo a organização do codigo 

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


    def validate(self, data): 
       if not cpf_valido(data['cpf']):
              raise serializers.ValidationError({'cpf': "o cpf deve conter 11 digitos"}) 
          
       if not nome_valido(data['nome']):
              raise serializers.ValidationError({'nome': "o nome do usuario não pode conter números"})

       if not rg_valido(data['rg']):
               raise serializers.ValidationError({'rg': "o rg não pode conter menos de 5 digitos ou de mais do 9 digitos"})
 
       if not celular_valido(data['celular']):
                raise serializers.ValidationError({'celular': "o número de celular deve ter 11 digitos"})
         
       return data 

 


        


        
