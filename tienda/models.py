from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor = models.IntegerField()
    nombre = models.CharField(max_length=100)

    def __str__(selft):
        return selft.nombre
    
opciones_categoria = [
    [0, "Romance"],
    [1, "Fantasia"],
    [2, "Romance Clasico"]
]
    
class Libro(models.Model):
    isbn = models.IntegerField()
    nombre = models.CharField(max_length=400)
    precio = models.IntegerField()
    categoria = models.IntegerField(choices=opciones_categoria)
    nuevo = models.BooleanField()
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="Libros",null=True)

    def __str__(selft):
        return selft.nombre
    

tipoConsulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    tipoConsulta = models.IntegerField(choices=tipoConsulta)
    mensaje = models.TextField()
    
    def __str__(selft):
        return selft.nombre