class Admin(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255)

    def permisos(self):
        return True

    def sesion(self):
        return True

    def crearLista(self):
        return True


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=255)

    def sesion(self):
        return True

    def crearLista(self):
        return True


class Medidor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    tipoMedicion = models.CharField(max_length=255)
    datoConsumo = models.FloatField()

    def registrarConsumo(self):
        return 0.0

    def obtenerReporte(self):
        return 0.0


class AreaCasa(models.Model):
    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE)
    nombreArea = models.CharField(max_length=255)

    def obtenerConsumo(self):
        return 0.0


class Casa(models.Model):
    medidor = models.OneToOneField(Medidor, on_delete=models.CASCADE)
    tamaño = models.CharField(max_length=255)

    def obtenerConsumo(self):
        return 0.0


class FuenteEnergiaExterna(models.Model):
    tipo = models.CharField(max_length=255)
    capacidad = models.FloatField()

    def generarElectricidad(self):
        return 0.0

    def evaluarEficiencia(self):
        return 0.0


class Generador(FuenteEnergiaExterna):
    cantidad = models.FloatField()

    def evaluarAhorro(self):
        return 0.0


class PanelSolar(FuenteEnergiaExterna):
    cantidad = models.FloatField()

    def obtenerGeneracion(self):
        return 0.0


class Sensor(FuenteEnergiaExterna):
    cantidad = models.FloatField()

    def evaluarAhorro(self):
        return 0.0


class Eolico(FuenteEnergiaExterna):
    cantidad = models.FloatField()

    def obtenerGeneracion(self):
        return 0.0


class CalculadoraCosto(Medidor):
    gastoEnergetico = models.FloatField()
    gastoMonetario = models.FloatField()

    def calcularCosto(self):
        return 0.0

    def generarGasto(self):
        return 0.0


class Estadistica(CalculadoraCosto):
    tiempo = models.CharField(max_length=255)

    def gestionarUsuario(self):
        return True


class Grafico(CalculadoraCosto):
    tipo = models.CharField(max_length=255)

    def generarGrafica(self):
        return True
