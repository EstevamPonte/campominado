from django.shortcuts import render, redirect
from .forms import JogadaForm
from  .models import Jogada, Game
from django.utils import timezone

# Create your views here.

def iniciar_jogo(request):
    if request.method == 'GET':
        return render(request, 'tela_iniciar.html')
    elif request.method == 'POST':
        Game.novo_jogo()
        return redirect('jogar_jogo')

def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.created_date = timezone.now()
            jogada.save()
    else:
        form = JogadaForm()

    jogadas = Jogada.objects.all()

    return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})