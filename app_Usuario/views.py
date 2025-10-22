from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario, Portafolio
from .forms import UsuarioForm, PortafolioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    portafolios = usuario.portafolios.all()  # Obtiene todos los portafolios del usuario
    return render(request, 'detalle_usuario.html', {
        'usuario': usuario, 
        'portafolios': portafolios
    })

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_Usuario:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Crear Usuario'})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('app_Usuario:detalle_usuario', usuario_id=usuario.id_usuario)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Editar Usuario'})

def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_Usuario:listar_usuarios')
    return render(request, 'confirmar_borrar.html', {'usuario': usuario})

# Vistas para Portafolios
def crear_portafolio(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    if request.method == 'POST':
        form = PortafolioForm(request.POST)
        if form.is_valid():
            portafolio = form.save(commit=False)
            portafolio.id_usuario = usuario  # Asigna automáticamente el usuario
            portafolio.save()
            return redirect('app_Usuario:detalle_usuario', usuario_id=usuario.id_usuario)
    else:
        # Excluimos el campo id_usuario del formulario
        form = PortafolioForm()
        form.fields.pop('id_usuario', None)  # Elimina el campo del formulario
    
    return render(request, 'formulario_portafolio.html', {
        'form': form, 
        'titulo': f'Crear Portafolio para {usuario.nombre}',
        'usuario': usuario
    })

def editar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id_portafolio=portafolio_id)
    if request.method == 'POST':
        form = PortafolioForm(request.POST, instance=portafolio)
        if form.is_valid():
            form.save()
            return redirect('app_Usuario:detalle_usuario', usuario_id=portafolio.id_usuario.id_usuario)
    else:
        form = PortafolioForm(instance=portafolio)
    
    return render(request, 'formulario_portafolio.html', {
        'form': form, 
        'titulo': 'Editar Portafolio',
        'usuario': portafolio.id_usuario
    })

def borrar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id_portafolio=portafolio_id)
    usuario_id = portafolio.id_usuario.id_usuario
    if request.method == 'POST':
        portafolio.delete()
        return redirect('app_Usuario:detalle_usuario', usuario_id=usuario_id)
    return render(request, 'confirmar_borrar_portafolio.html', {'portafolio': portafolio})