from rest_framework import serializers
from .models import Categoria, Consulta, Usuario, Producto, Venta, Detalle,  Detalle_comprado, Transaccion, Rol
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            rut=validated_data['rut'],
            dvrut=validated_data['dvrut'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            respuesta=validated_data['respuesta'],
            pregunta=validated_data['pregunta'],
            rol=validated_data['rol'],
            
        )
        return user
    




class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria','nombre_categoria']

class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class transaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'

class consultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class detalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'

class detalleCompradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_comprado
        fields = '__all__'

class detalleConProductoSerializer(serializers.ModelSerializer):
    producto = productoSerializer()  

    class Meta:
        model = Detalle
        fields = '__all__'
