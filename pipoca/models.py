from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

# Create your models here.
class Pipoca(models.Model):
    id = models.AutoField(primary_key=True)
    sabor = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name=('categoria'))
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='pipoca/', blank=True, null=True) 

    def __str__(self):
        return self.sabor