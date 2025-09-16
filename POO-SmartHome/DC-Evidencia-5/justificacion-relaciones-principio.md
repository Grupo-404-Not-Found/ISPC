DC-Evidencia-5 — Programación I — SmartHome

1) Contexto y alcance
Diseñamos un diagrama de clases UML que modela el sistema SmartHome con enfoque POO.

Entidades principales (UML):
- Usuario
- Dispositivo (abstracta) y sus especializaciones: Luz, Camara, Electrodomestico
- Automatizacion y AutomatizacionAhorroEnergia (subclase)
- SistemaSmartHome (orquestador)

2) Relaciones del diagrama
- Herencia
  - Luz, Camara, Electrodomestico heredan de Dispositivo.
  - AutomatizacionAhorroEnergia hereda de Automatizacion.
- Composicion
  - SistemaSmartHome 1 a 0 a muchos Usuario
  - SistemaSmartHome 1 a 0 a muchos Dispositivo
  - SistemaSmartHome 1 a 0 a muchos Automatizacion
- Asociacion N a N
  - Automatizacion N a N Dispositivo

3) Principios POO aplicados y justificacion

Abstraccion
- Dispositivo (abstracta) concentra lo comun del dominio: nombre, tipo, estado y operaciones encender(), apagar(), mostrar_estado().
- Automatizacion abstrae la idea de regla o escena, definiendo ejecutar(); las variantes concretas (por ejemplo, AutomatizacionAhorroEnergia) implementan la logica especifica.

Encapsulamiento
- Atributos tratados como protegidos o privados y cambios de estado solo por metodos, garantizando invariantes como estado en {encendido, apagado}.
- En Usuario, la contraseña se trata como dato sensible con acceso controlado.
- SistemaSmartHome expone operaciones de alto nivel (agregar_dispositivo(), ejecutar_automatizacion()) y oculta las colecciones internas.

Herencia y Polimorfismo
- Las subclases (Luz, Camara, Electrodomestico) reutilizan el contrato de Dispositivo y lo extienden con metodos propios (ajustar_luz(), grabar(), ejecutar()).
- AutomatizacionAhorroEnergia redefine ejecutar() segun su regla.
- El sistema opera sobre colecciones polimorficas: una lista de Dispositivo admite luces, camaras y electrodomesticos indistintamente; una lista de Automatizacion admite cualquier regla concreta.

Asociacion N a N
- Automatizacion y Dispositivo es muchos a muchos: una regla puede afectar varios dispositivos y un dispositivo puede pertenecer a varias reglas.

Agregacion
- En este diseno no se utiliza agregacion: se eligio composicion desde SistemaSmartHome hacia Usuario, Dispositivo y Automatizacion porque el sistema posee y administra estas colecciones (ciclo de vida controlado por la aplicacion).
- Alternativa: si en el futuro Usuario o Dispositivo fueran gestionados por servicios externos u otros contextos, esa relacion podria relajarse a agregacion (el sistema solo los reune sin ser su dueno).

Aclaracion de cardinalidades en texto
- SistemaSmartHome a Usuario, Dispositivo y Automatizacion: 1 a 0 a muchos.
- Automatizacion con Dispositivo: N a N (muchos a muchos).

Beneficios de diseno (cohesion y acoplamiento)
- Alta cohesion: cada clase tiene responsabilidad clara.
- Bajo acoplamiento: reglas (Automatizacion) separadas de dispositivos; SistemaSmartHome orquesta sin mezclar logicas.
- Escalabilidad: agregar un nuevo tipo de dispositivo (por ejemplo, Termostato) o una nueva regla (por ejemplo, AutomatizacionNocturna) no impacta al resto; basta con heredar e implementar.
- Testeabilidad: el polimorfismo facilita dobles de prueba y tests unitarios aislados.
