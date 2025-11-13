import django
import os

# 🔹 Configura Django para que funcione fuera del servidor
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_parque.settings')
django.setup()

from app_empleado.models import Atraccion, Empleado

# 🔹 Lista de empleados existentes
empleados_existentes = list(Empleado.objects.values_list('id_emp', flat=True))

# 🔹 Buscar atracciones con empleados inválidos
atracciones_invalidas = Atraccion.objects.exclude(id_emp_id__in=empleados_existentes)

print(f"🔍 Se encontraron {atracciones_invalidas.count()} atracciones con empleado inexistente.")

if atracciones_invalidas.exists():
    # ✅ Opción 1: Eliminar las atracciones inválidas
    atracciones_invalidas.delete()
    print("🧹 Se eliminaron las atracciones con referencias inválidas.")

    # Si prefieres reasignarlas al empleado 1, usa este código en lugar de delete():
    # for atr in atracciones_invalidas:
    #     atr.id_emp_id = 1  # cambia al ID del empleado que tengas
    #     atr.save()
    # print("♻️ Se reasignaron las atracciones al empleado 1.")
else:
    print("✅ No hay atracciones inválidas, todo limpio.")
