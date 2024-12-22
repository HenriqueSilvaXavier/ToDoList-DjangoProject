from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm  # Assumindo que você tenha um formulário definido.
from django.utils.timezone import now


def atualizar_status_tarefas_expiradas():
    """
    Atualiza o status das tarefas cujo prazo expirou e estão em andamento.
    """
    tarefas_expiradas = Tarefa.objects.filter(prazo__lt=now(), status='em_andamento')
    tarefas_expiradas.update(status='nao_feita')


def listar_tarefas(request):
    """
    Exibe a lista de todas as tarefas.
    """
    atualizar_status_tarefas_expiradas()  # Atualiza status antes de listar
    tarefas = Tarefa.objects.all()
    return render(request, 'listar_tarefas.html', {'tarefas': tarefas})


def atualizar_status(request):
    """
    Atualiza o status das tarefas selecionadas para 'concluída'.
    """
    if request.method == 'POST':
        tarefa_ids = request.POST.getlist('tarefa_ids')  # Obter a lista de IDs selecionados
        if tarefa_ids:
            Tarefa.objects.filter(id__in=tarefa_ids).update(status='concluida')
        return redirect('listar_tarefas')
    return redirect('listar_tarefas')


def criar_tarefa(request):
    """
    Cria uma nova tarefa com base nos dados enviados pelo formulário.
    """
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova tarefa no banco de dados
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'criar_tarefa.html', {'form': form})


def excluir_tarefa(request, tarefa_id):
    """
    Exclui a tarefa especificada pelo ID.
    """
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('listar_tarefas')


def editar_tarefa(request, tarefa_id):
    """
    Edita os dados de uma tarefa existente.
    """
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})


def your_name(request, name):
    """
    Exibe uma página com o nome fornecido.
    """
    return render(request, 'yourname.html', {'name': name})
