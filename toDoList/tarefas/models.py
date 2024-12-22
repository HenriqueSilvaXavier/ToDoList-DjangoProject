from django.db import models
from django.utils.timezone import now


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('em_andamento', 'Em andamento'),
        ('nao_feita', 'Não feita'),
        ('concluida', 'Concluída'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='em_andamento',
    )
    materia = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    prazo = models.DateTimeField(null=True, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Verifica se o prazo já passou e a tarefa não está concluída
        if self.prazo and self.prazo < now() and self.status != 'concluida':
            self.status = 'nao_feita'
        super().save(*args, **kwargs)
