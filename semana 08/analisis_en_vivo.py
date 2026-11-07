"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
# cada clave es un nombre de medicamento, su valor es el nombre estandarizado
equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol" : "acetaminofén",
    "antiacido" : "antiácido",
    "lorsatán" : "lorsatan"
}

conteo_medicamentos = {}
total_medicamentos = 0
print("\nANALISIS FASE #1: MEDICAMENTOS DE TRES ATENCIONES")
for indice in range (3):
    registro = registros[indice]
    print(registro["paciente_nombre"])
    print(f"\nCedula: ")
    print(registro["paciente_cedula"])
    print(f"\nMedicamentos: ")
    print(registro["medicamentos"])
    print(f"\nDiagnostico: ")
    print(registro["diagnostico"])
    
    for medicamento in registro["medicamentos"]:
        #Limpieza
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
            
print("\nTotal de medicamento recetados:", total_medicamentos) 

print(conteo_medicamentos)    


# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\nANALISIS FASE #2: MEDICAMENTOS Y ATENCIONES")
conteo_medicamentos = {}
total_medicamentos = 0
for registro in registros:
    for medicamento in registro['medicamentos']:
        #Limpieza PARACETAMOL -> paracetamol -> aceteminofén
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        #Contar medicamentos
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
            
print("\nTotal de medicamentos recetados:", total_medicamentos)
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}: {cantidad}")

# FASE 3: CONTAR ATENCIONES POR HOSPITAL
print("\nANALISIS FASE #3: ATENCIONES POR HOSPITAL")
conteo_hospitales = {}

for registro in registros:
    hospital = registro['hospital']
    if hospital not in conteo_hospitales:
        conteo_hospitales[hospital]=0
    conteo_hospitales[hospital]+=1
print(f"\nHospital visitado:")
for hospital, cantidad in conteo_hospitales.items():
    print(f"- {hospital}: {cantidad}")


# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA
print("\nANALISIS FASE #4: ATENCIONES POR ENFERMEDAD DIAGNOSTICADA")
conteo_enfermedades = {}

for registro in registros:
    enfermedad = registro['diagnostico']
    if enfermedad not in conteo_enfermedades:
        conteo_enfermedades[enfermedad]=0
    conteo_enfermedades[enfermedad]+=1
print(f"\nEnfermedad diagnosticada:")
for enfermedad, cantidad in conteo_enfermedades.items():
    print(f"- {enfermedad}: {cantidad}")