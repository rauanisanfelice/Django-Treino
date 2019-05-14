from django.db import models

class Perfil(models.Model):
    
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    # PARA SER CRIADO NO BANCO DE DADOS DEVE EXECUTAR O COMANDO ABAIXO NO TERMINAL
    # python manage.py makemigrations

    # POPULAR O SHEMA NO BANCO DE DADOS
    # python manage.py migrate

    # ACESSA O BANCO
    # python manage.py shell

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):

    #solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    #convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    solicitante = models.ForeignKey(Perfil, related_name="convites_feitos", on_delete=models.CASCADE)
    convidado = models.ForeignKey(Perfil, related_name="convites_recebidos", on_delete=models.CASCADE)
    
    # FILTRAR TUDO QUE É DO ID SOLICITANTE = 1
    # convites_feitos = Convite.objects.filter(solicitante__id=1)

    """
    class Perfil(object):

        def __init__ (self, nome='', email='', telefone='', nome_empresa=''):
            self.nome = nome
            self.email = email
            self.telefone = telefone
            self.nome_empresa = nome_empresa
    """