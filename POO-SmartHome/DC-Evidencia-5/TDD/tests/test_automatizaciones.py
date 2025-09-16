from smarthome import SistemaSmartHome, Luz, Camara
from smarthome import AutomatizacionAhorroEnergia

def test_automatizacion_ahorro_apaga_todo_menos_camaras():
    sis = SistemaSmartHome()
    luz = Luz("Luz Cocina", estado="encendido")
    cam = Camara("Camara Entrada", estado="encendido")
    sis.agregar_dispositivo(luz)
    sis.agregar_dispositivo(cam)

    auto = AutomatizacionAhorroEnergia()
    sis.agregar_automatizacion(auto)

    sis.ejecutar_automatizacion("Ahorro de energía")

    assert luz.estado == "apagado"           # se apaga
    assert cam.estado == "encendido"         # permanece encendida
