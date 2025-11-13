from django.shortcuts import render, redirect
from .models import Empleado
from .models import Cliente
from .models import Atraccion
# Página de inicio
def inicio(request):
    return render(request, "inicio.html")

# Agregar empleado
def agregar_empleado(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        puesto = request.POST.get("puesto")
        telefono = request.POST.get("telefono")
        salario = request.POST.get("salario")
        id_atr = request.POST.get("id_atr")

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            salario=salario,
            id_atr=id_atr
        )
        return redirect("ver_empleados")

    return render(request, "empleado/agregar_empleado.html")

# Ver empleados
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "empleado/ver_empleados.html", {"empleados": empleados})

# Actualizar empleado
def actualizar_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    return render(request, "empleado/actualizar_empleado.html", {"empleado": empleado})

# Realizar actualización
def realizar_actualizacion_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    empleado.nombre = request.POST.get("nombre")
    empleado.apellido = request.POST.get("apellido")
    empleado.puesto = request.POST.get("puesto")
    empleado.telefono = request.POST.get("telefono")
    empleado.salario = request.POST.get("salario")
    empleado.id_atr = request.POST.get("id_atr")
    empleado.save()
    return redirect("ver_empleados")

# Borrar empleado
def borrar_empleado(request, id):
    empleado = Empleado.objects.get(id_emp=id)
    empleado.delete()
    return redirect("ver_empleados")
# CLIENTES 
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        id_atr = request.POST.get('id_atr') or None

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            id_atr=id_atr
        )
        return redirect('ver_cliente')

    return render(request, 'clientes/agregar_cliente.html')

# Ver clientes (listado)
def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('id_cli')
    return render(request, 'clientes/ver_cliente.html', {'clientes': clientes})

# Mostrar formulario con datos para actualizar
def actualizar_cliente(request, id_cli):
    cliente = Cliente.objects.get(id_cli=id_cli)
    return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})

# Guardar actualización
def realizar_actualizacion_cliente(request, id_cli):
    cliente = Cliente.objects.get(id_cli=id_cli)
    cliente.nombre = request.POST.get('nombre')
    cliente.apellido = request.POST.get('apellido')
    cliente.telefono = request.POST.get('telefono')
    cliente.correo = request.POST.get('correo')
    cliente.id_atr = request.POST.get('id_atr') or None
    cliente.save()
    return redirect('ver_cliente')

# Borrar cliente
def borrar_cliente(request, id_cli):
    cliente = Cliente.objects.get(id_cli=id_cli)
    # Si quieres una vista de confirmación separada, puedes renderizar una plantilla antes de borrar.
    # Aquí borramos directamente y redirigimos al listado:
    cliente.delete()
    return redirect('ver_cliente')

def ver_atraccion(request):
    atracciones = Atraccion.objects.all().order_by('id_atr')
    return render(request, 'atracciones/ver_atraccion.html', {'atracciones': atracciones})

# Agregar una nueva atracción

def agregar_atraccion(request):
    empleados = Empleado.objects.all()  # para el selector desplegable

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        capacidad = request.POST.get('capacidad')
        estado = request.POST.get('estado')
        altura_min = request.POST.get('altura_min')
        id_emp = request.POST.get('id_emp')  # este ya es el número del empleado

        # ✅ aquí ya no buscamos el objeto, solo guardamos el ID
        Atraccion.objects.create(
            nombre=nombre,
            tipo=tipo,
            capacidad=capacidad,
            estado=estado,
            altura_min=altura_min,
            id_emp=id_emp  # guarda el número, no el objeto
        )
        return redirect('ver_atraccion')

    return render(request, 'atracciones/agregar_atraccion.html', {'empleados': empleados})

# Editar (mostrar formulario con datos)
def actualizar_atraccion(request, id_atr):
    atraccion = Atraccion.objects.get(id_atr=id_atr)
    return render(request, 'atracciones/actualizar_atraccion.html', {'atraccion': atraccion})

# Guardar los cambios
def realizar_actualizacion_atraccion(request, id_atr):
    atraccion = Atraccion.objects.get(id_atr=id_atr)
    atraccion.nombre = request.POST.get('nombre')
    atraccion.tipo = request.POST.get('tipo')
    atraccion.capacidad = request.POST.get('capacidad')
    atraccion.estado = request.POST.get('estado')
    atraccion.altura_min = request.POST.get('altura_min')
    atraccion.id_emp = request.POST.get('id_emp')
    atraccion.save()
    return redirect('ver_atraccion')

# Borrar atracción
def borrar_atraccion(request, id_atr):
    atraccion = Atraccion.objects.get(id_atr=id_atr)
    atraccion.delete()
    return redirect('ver_atraccion')