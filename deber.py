def obtener_sueldo_base(cargo):
    sueldos = {"Director": 2500, "Especialista": 1800, "Analista": 1200, "Asistente": 900}
    return sueldos.get(cargo, 0)

def calcular_bono(cargo):
    bonos = {"Director": 0.09, "Especialista": 0.06, "Analista": 0.03}
    if cargo in bonos:
        return obtener_sueldo_base(cargo) * bonos[cargo]
    return 0

def aplicar_descuento(sueldo_base):
    if sueldo_base > 1300:
        return sueldo_base * 0.08
    return 0

def aplicar_cargo_transferencia(sueldo_depositar):
    return sueldo_depositar * 0.001

def calcular_sueldo_depositar(nombre, cargo, pago):
    sueldo_base = obtener_sueldo_base(cargo)
    bono = calcular_bono(cargo)
    descuento = aplicar_descuento(sueldo_base)
    sueldo_depositar = sueldo_base + bono - descuento

    if pago == "transferencia":
        cargo_transferencia = aplicar_cargo_transferencia(sueldo_depositar)
        sueldo_depositar -= cargo_transferencia
    else:
        cargo_transferencia = 0

    return sueldo_depositar, sueldo_base, bono, descuento, cargo_transferencia

nombre = input("Ingrese el nombre del trabajador: ")
cargo = input("Ingrese el cargo del trabajador (Director, Especialista, Analista, Asistente: ")
pago = input("Ingrese el tipo de mecanismo de pago (transferencia/efectivo): ")

sueldo_depositar, sueldo_base, bono, descuento, cargo_transferencia = calcular_sueldo_depositar(nombre, cargo, pago)

print("\nDatos del trabajador:")
print("Nombre:", nombre)
print("Cargo:", cargo)
print("Tipo de mecanismo de pago:", pago)
print("\nDetalles del sueldo:")
print("Sueldo base:", sueldo_base)
print("Bono:", bono)
print("Descuento por impuesto:", descuento)
if pago == "transferencia":
    print("Cargo por transferencia bancaria:", cargo_transferencia)
print("\nSueldo a depositar:", sueldo_depositar)
