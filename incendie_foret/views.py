from django.shortcuts import get_object_or_404, render, redirect
from .forms import IncendieForm, ForetForm
from .models import Incendie, Foret

def my_template(request):
    incendies = Incendie.objects.all()
    return render(request, 'incendie_foret/my_template.html', {'incendies': incendies})

def incendie_foret_detail(request, pk):
    incendie = get_object_or_404(Incendie, pk=pk)
    return render(request, 'incendie_foret/incendie_foret_detail.html', {'incendie': incendie})

def nouvelle_foret(request):
    if request.method == 'POST':
        form = ForetForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la nouvelle forêt dans la base de données
            return redirect('nouveau_incendie')  # Redirige vers le formulaire de nouvel incendie
    else:
        form = ForetForm()
    
    return render(request, 'incendie_foret/nouvelle_foret.html', {'form': form})

def nouveau_incendie(request):
    if request.method == 'POST':
        form = IncendieForm(request.POST)
        if form.is_valid():
            incendie = form.save(commit=False)
            incendie.id_foret = form.cleaned_data['id_foret']
            incendie.save()
            return redirect('nouveau_incendie')
    else:
        form = IncendieForm()
    
    context = {'form': form}
    return render(request, 'incendie_foret/nouveau_incendie.html', context)

def recherche_foret(request):
    query = request.GET.get('query')
    resultats = Foret.objects.filter(nom__icontains=query)
    context = {
        'query': query,
        'resultats': resultats
    }
    return render(request, 'incendie_foret/recherche_foret.html', context)

    

