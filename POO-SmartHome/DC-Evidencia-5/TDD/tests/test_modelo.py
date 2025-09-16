import pytest
from smarthome import Usuario, Luz, Camara, Electrodomestico, SistemaSmartHome

def test_encender_apagar_y_mostrar_estado():
    luz = Luz("Luz Living")
    assert luz.estado == "apagado"
    luz.encender()
    assert luz.estado == "encendido"
    assert "Luz Living (luz): encendido" == luz.mostrar_estado()

def test_ajustar_luz_normaliza():
    luz = Luz("Luz Dormitorio")
    luz.ajustar_luz(150)
    assert luz.nivel == 100
    luz.ajustar_luz(-20)
    assert luz.nivel == 0
    luz.ajustar_luz(42)
    assert luz.nivel == 42

def test_polimorfismo_lista_dispositivos():
    sis = SistemaSmartHome()
    sis.agregar_dispositivo(Luz("L1"))
    sis.agregar_dispositivo(Camara("C1"))
    sis.agregar_dispositivo(Electrodomestico("E1"))
    estados = sis.listar_dispositivos()
    assert len(estados) == 3
    assert any("L1 (luz)" in e for e in estados)
    assert any("C1 (cámara)" in e for e in estados)
    assert any("E1 (electrodoméstico)" in e for e in estados)

def test_usuario_sesion():
    u = Usuario("juan", "secreta", "user")
    assert not u.sesion_activa
    u.iniciar_sesion()
    assert u.sesion_activa
    u.cerrar_sesion()
    assert not u.sesion_activa
