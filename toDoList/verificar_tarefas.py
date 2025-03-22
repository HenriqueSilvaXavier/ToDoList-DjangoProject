from django.core.management.base import BaseCommand
from tarefas.models import Tarefa

class Command(BaseCommand):
    help = "Verifica tarefas com valores inválidos no campo 'prazo'."

    def handle(self, *args, **kwargs):
        invalid_tarefas = Tarefa.objects.filter(prazo__isnull=False).exclude(prazo__regex=r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')
        if invalid_tarefas.exists():
            self.stdout.write("Tarefas com valores inválidos no campo 'prazo':")
            for tarefa in invalid_tarefas:
                self.stdout.write(f"ID: {tarefa.id}, Prazo: {tarefa.prazo}")
        else:
            self.stdout.write("Nenhuma tarefa inválida encontrada.")
