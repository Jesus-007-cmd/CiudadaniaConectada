from rest_framework import serializers
from .models import Open311ReporteProblema, SolicitudInformacion, UsuarioFuncionario, AvanceReporte

class ReporteProblemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Open311ReporteProblema
        fields = '__all__'

class SolicitudInformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudInformacion
        fields = '__all__'

class UsuarioFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioFuncionario
        fields = '__all__'
        
class AvanceReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvanceReporte
        fields = '__all__'
