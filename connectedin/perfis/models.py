from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    contatos = models.ManyToManyField('self')

    usuario = models.OneToOneField(User, related_name="perfil", on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey("Perfil", related_name="convites_feitos", on_delete=models.CASCADE)
    convidado = models.ForeignKey("Perfil", related_name="convites_recebidos", on_delete=models.CASCADE)

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        
        # DELETE CONVITE
        self.delete()

    # PARA SER CRIADO NO BANCO DE DADOS DEVE EXECUTAR O COMANDO ABAIXO NO TERMINAL
    # python manage.py makemigrations

    # POPULAR O SHEMA NO BANCO DE DADOS
    # python manage.py migrate

    # ACESSA O BANCO
    # python manage.py shell

    # FILTRAR TUDO QUE É DO ID SOLICITANTE = 1
    # convites_feitos = Convite.objects.filter(solicitante__id=1)