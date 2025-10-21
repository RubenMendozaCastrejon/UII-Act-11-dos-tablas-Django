from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password # Necesario para hashear contraseñas
from .models import Usuario, Portafolio
from .forms import UsuarioForm, PortafolioForm

# Vistas para el modelo Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def detalle_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES) # request.FILES para la foto_perfil
        if form.is_valid():
            usuario = form.save(commit=False)
            # Hashear la contraseña antes de guardar
            usuario.contrasena = make_password(form.cleaned_data['contrasena'])
            usuario.save()
            return redirect('app_Usuario:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Crear Usuario'})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            # Obtener la contraseña del formulario para ver si ha cambiado
            nueva_contrasena = form.cleaned_data.get('contrasena')
            # Si la contraseña es nueva o ha cambiado, hashearla
            if nueva_contrasena and not nueva_contrasena.startswith('pbkdf2_sha256$'): # Simple chequeo si ya está hasheada
                usuario.contrasena = make_password(nueva_contrasena)
            elif not nueva_contrasena: # Si el campo de contraseña viene vacío, no lo actualizamos
                form.instance.contrasena = usuario.contrasena # Mantenemos la contraseña existente
            
            form.save()
            return redirect('app_Usuario:detalle_usuario', usuario_id=usuario.id)
    else:
        # Al cargar el formulario para editar, no queremos rellenar el campo de contraseña
        # con el hash, ni dejarlo en blanco si no se va a cambiar.
        # Por lo tanto, se pasa la instancia, pero el campo de contraseña del formulario
        # se renderizará vacío (ya que no hay valor inicial para 'confirmar_contrasena').
        form = UsuarioForm(instance=usuario)
        # Limpiamos los campos de contraseña para que no muestren valores existentes
        form.fields['contrasena'].initial = ''
        form.fields['confirmar_contrasena'].initial = ''

    return render(request, 'formulario_usuario.html', {'form': form, 'titulo': 'Editar Usuario'})

def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('app_Usuario:listar_usuarios')
    return render(request, 'confirmar_borrar_usuario.html', {'usuario': usuario})

# Vistas para el modelo Portafolio

def listar_portafolios(request):
    portafolios = Portafolio.objects.all()
    return render(request, 'listar_portafolios.html', {'portafolios': portafolios})

def detalle_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id=portafolio_id)
    return render(request, 'detalle_portafolio.html', {'portafolio': portafolio})

def crear_portafolio(request):
    if request.method == 'POST':
        form = PortafolioForm(request.POST)
        if form.is_valid():
            portafolio = form.save(commit=False)
            # Asigna el usuario actual o un usuario predeterminado.
            # Aquí asumimos que el usuario que crea el portafolio es el usuario actual,
            # pero puedes ajustar esta lógica según tus necesidades.
            # Por ejemplo, si el usuario está logueado:
            # portafolio.usuario = request.user
            # Para este ejemplo, vamos a buscar un usuario existente (esto DEBE ser mejorado en producción)
            # Para fines de demostración simple, asignamos al primer usuario encontrado
            primer_usuario = Usuario.objects.first()
            if primer_usuario:
                portafolio.usuario = primer_usuario
            else:
                # Manejar el caso donde no hay usuarios (o redirigir, o mostrar un error)
                # Por ahora, simplemente no asignamos y esperamos que el save falle si el campo es obligatorio
                pass 
            portafolio.save()
            return redirect('app_Usuario:listar_portafolios')
    else:
        form = PortafolioForm()
    return render(request, 'formulario_portafolio.html', {'form': form, 'titulo': 'Crear Portafolio'})

def editar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id=portafolio_id)
    if request.method == 'POST':
        form = PortafolioForm(request.POST, instance=portafolio)
        if form.is_valid():
            form.save()
            return redirect('app_Usuario:detalle_portafolio', portafolio_id=portafolio.id)
    else:
        form = PortafolioForm(instance=portafolio)
    return render(request, 'formulario_portafolio.html', {'form': form, 'titulo': 'Editar Portafolio'})

def borrar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id=portafolio_id)
    if request.method == 'POST':
        portafolio.delete()
        return redirect('app_Usuario:listar_portafolios')
    return render(request, 'confirmar_borrar_portafolio.html', {'portafolio': portafolio})