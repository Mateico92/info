
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo, Comentario
from django.contrib.auth.decorators import login_required

def detalle_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    
    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        if comentario and request.user.is_authenticated:
            nuevo_comentario = Comentario(contenido=comentario, autor=request.user, articulo=articulo)
            nuevo_comentario.save()
            return redirect('detalle_articulo', id=articulo.id)

    return render(request, 'detalle_articulo.html', {'articulo': articulo})
