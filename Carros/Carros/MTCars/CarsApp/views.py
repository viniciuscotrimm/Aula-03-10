from django.shortcuts import render
from CarsApp.models import MTCars
from django.db.models import Q # Importe o Q para buscas "icontains"

# Create your views here.

def searchf(request):
    
    # Por defeito, mostre todos os carros
    carros = MTCars.objects.all()
    search_query = "" # Inicializa a variável de busca

    # Se o método for POST (formulário de busca enviado)
    if request.method == 'POST':
        search_query = request.POST.get('search', "") # Pega o valor da busca
        
        # Filtra os carros se houver uma consulta
        if search_query:
            carros = MTCars.objects.filter(name__icontains=search_query)
        # Se a busca for vazia, continua a mostrar todos os carros
            
    # O contexto é enviado tanto no GET (todos os carros) como no POST (carros filtrados)
    contexto = {
        'search_query': search_query,
        'carros': carros
    }
    return render(request, 'CarsApp/home.html', contexto)