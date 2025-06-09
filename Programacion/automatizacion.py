def ejecutar_automatizacion(dispositivos):
    """
    Automatización: Modo Ahorro de Energía.
    Esta función apaga todos los dispositivos cuyo tipo no sea 'cámara'.
    Se asume que las cámaras deben seguir funcionando por seguridad.
    """
    print("\n🔋 Ejecutando Modo Ahorro de Energía...")
    for d in dispositivos:
        if d['tipo'].lower() != "cámara":
            d['estado'] = "apagado"
    print("✅ Todos los dispositivos no esenciales fueron apagados.")