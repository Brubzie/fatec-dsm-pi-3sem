from django.db import models
from django.core import validators
from djongo import models as djongo_models

class Endereco(models.Model):
    _id = djongo_models.ObjectIdField()
    cep = models.CharField(max_length=9, validators=[validators.RegexValidator(regex='^\d{5}-\d{3}$')])
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

class Doacao(models.Model):
    _id = djongo_models.ObjectIdField()
    material_doado = models.CharField(max_length=50)
    peso = models.IntegerField(validators=[validators.MinValueValidator(1)])
    data = models.DateField()
    item_recebido = models.CharField(max_length=50)
    validacao = models.BooleanField(default=False)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, validators=[validators.RegexValidator(regex='^\d{3}\.\d{3}\.\d{3}-\d{2}$')])
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, validators=[validators.RegexValidator(regex='^\(\d{2}\) \d{4,5}-\d{4}$')])
    data_nascimento = models.DateField()
    endereco = djongo_models.EmbeddedField(model_container=Endereco)
    doacoes = djongo_models.ArrayField(model_container=Doacao)

    class Meta:
        db_table = 'ecoshare'  # Define o nome da coleção no MongoDB
