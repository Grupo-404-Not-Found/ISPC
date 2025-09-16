def ejecutar_automatizacion(dispositivos):
    """
    Automatización: Modo Ahorro de Energía

    Descripción:
    Recorre todos los dispositivos registrados y apaga aquellos que no son de tipo 'cámara'.
    Las cámaras deben permanecer encendidas por razones de seguridad.

    Parámetros:
    dispositivos (list[dict]): Lista de diccionarios con claves 'nombre', 'tipo' y 'estado'.

    Efectos:
    - Modifica el estado de los dispositivos no esenciales a "apagado".

    Ejemplo:
    dispositivos = [
        {"nombre": "Luz Living", "tipo": "luz", "estado": "encendido"},
        {"nombre": "Cámara Entrada", "tipo": "cámara", "estado": "encendido"}
    ]
    ejecutar_automatizacion(dispositivos)

    Resultado esperado:
    - La luz del living queda "apagado".
    - La cámara de entrada se mantiene "encendido".
    """
    print("\nEjecutando Modo Ahorro de Energía...")
    for d in dispositivos:
        t = (d.get('tipo') or '').strip().lower()
        if t not in ("cámara", "camara"):  # acepta con y sin acento
            d['estado'] = "apagado"
    print("Dispositivos no esenciales apagados.")