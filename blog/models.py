from django.db import models

# Create your models here.
class cliente(models.Model):
    id_cliente = models.CharField(max_length=10)
    num_documento = models.CharField(max_length=11)
    nombres = models.CharField(max_length=175)
    apellidos = models.CharField(max_length=175)
    nacionalidad = models.CharField(max_length=175)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    
class empleado(models.Model):
    id_empleado = models.CharField(max_length=10)
    nombres = models.CharField(max_length=175)
    apellidos = models.CharField(max_length=175)
    dni = models.CharField(max_length=8)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    
class doc_venta(models.Model):
    id_doc_venta = models.CharField(max_length=10)
    nro_documento = models.CharField(max_length=11)
    monto = models.CharField(max_length=15)
    tipo_pago = models.CharField(max_length=50)
    fecha_venta = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.monto + ' ' + self.tipo_pago
    
class servicios(models.Model):
    id_servicios = models.CharField(max_length=10)
    transporte = models.CharField(max_length=50)
    hotel = models.CharField(max_length=100)
    tour = models.CharField(max_length=100)
    guia = models.CharField(max_length=50)
    recojos = models.CharField(max_length=50)
    traslados = models.CharField(max_length=100)
    ruta = models.CharField(max_length=100)
    id_doc_venta = models.ForeignKey(doc_venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_servicios + ' ' + self.transporte
    
class ventas(models.Model):
    id_ventas = models.CharField(max_length=10)
    descuento = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    id_empleado=models.ForeignKey(empleado, on_delete=models.CASCADE)
    id_servicios = models.ForeignKey(servicios, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ventas + ' ' + self.estado
    
class reservas(models.Model):
    id_reservas = models.CharField(max_length=10)
    precio = models.CharField(max_length=10)
    fecha_reserva = models.DateField()
    fecha_ingreso=models.DateField()
    cant_personas = models.CharField(max_length=10)
    id_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)
    id_servicios = models.ForeignKey(servicios, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_reserva + ' ' + self.precio