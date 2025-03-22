from django.utils.timezone import now
from tarefas.models import Tarefa
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Atualiza o status de tarefas cujo prazo expirou.'

    def handle(self, *args, **kwargs):
        tarefas_expiradas = Tarefa.objects.filter(prazo__lt=now(), status='em_andamento')
        total_atualizadas = tarefas_expiradas.update(status='nao_feita')

        self.stdout.write(f'{total_atualizadas} tarefa(s) atualizada(s) para "Não feita".')
