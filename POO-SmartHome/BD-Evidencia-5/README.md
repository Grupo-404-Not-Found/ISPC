# Evidencia 5 — Programación I

## Proyecto: Actividad Integradora N° 5

## Docentes

* Gerlero, Martín

* Rojas Córsico, Ivana

* Accieto, Dianela

## Integrantes

* Camolotto Alejo Nicolas — DNI 44.606.044

* Flores Lopez Giancarlo — DNI 95.113.172

* Quevedo Jorge Francisco — DNI 31.218.408

* Quevedo Oscar Alberto — DNI 34.839.723

## Resumen ejecutivo

* Este repositorio contiene la entrega correspondiente a la Actividad Integradora N°5 — Programación I. Incluye:

* Diseño y justificación del Diagrama de Clases (POO) a partir del modelo relacional.

* Implementación orientada a objetos (carpeta POO-SmartHome).

* Scripts SQL organizados en DDL y DML para crear la base de datos, poblarla con datos y ejecutar consultas de verificación/actualización/borrado.

* Documentación clara para ejecutar los scripts en un DBMS online: https://www.db-fiddle.com/
 (se indica la configuración recomendada más abajo).

## Estructura del proyecto
     .    
     ├── DDL
     │   └── Database.sql         # Script DDL: creación de esquema, tablas y claves
     ├── DML
     │   ├── INSERT.sql           # Script DML: inserciones iniciales (datos)
     │   ├── QUERY.sql            # Consultas SELECT
     │   ├── UPDATE.sql           # Sentencias de UPDATE
     │   └── DELETE.sql           # Sentencias de DELETE
     └── README.md


## Orden de ejecución recomendado (imprescindible):

 1) DDL/Database.sql — crear tablas y keys.

 2) DML/INSERT.sql — insertar datos iniciales.

 3) DML/QUERY.sql, DML/UPDATE.sql, DML/DELETE.sql — Solo pueden ejecutarse posteriormente a los dos primeros.

## DBMS elegido para pruebas online

Para asegurar compatibilidad con la sintaxis usada en los scripts entregados, hemos elegido MySQL 8.0 como motor de prueba.
Plataforma online recomendada: https://www.db-fiddle.com/

En db-fiddle debes seleccionar en la UI la opción MySQL y la versión 8.0 antes de pegar y ejecutar los scripts.

## Cómo ejecutar paso a paso en db-fiddle.com (MySQL 8.0)

Abre: https://www.db-fiddle.com/.

- En la parte superior-izquierda de la interfaz selecciona:

- SQL dialect / Engine: MySQL - Version: 8.0

- En el panel izquierdo: pega el contenido de DDL/Database.sql. Pulsa "Run" (o la combinación de teclas Control + Enter).

- Verifica que no haya errores de sintaxis. Si se muestran errores, revisa el mensaje (secciones Output / Messages).

- Una vez el DDL se ejecute correctamente, debajo de las líneas de código copiadas anteriormente (Database.sql) en el panel izquierdo pegar el contenido de DML/INSERT.sql. Ejecuta Run. Las filas deben insertarse sin violación de claves foráneas.

- Si hay errores de FK, revisa que el orden de inserción respete dependencias (por ejemplo: insertar primero users, luego terminals, luego devices que referencian ids de terminales).

- Finalmente, puedes pegar y ejecutar DML/QUERY.sql, DML/UPDATE.sql y DML/DELETE.sql (en ese orden lógico) en el panel derecho para verificar selects, actualizaciones y eliminaciones. También es posible la ejecución con la combinación de teclas Control + Enter.

- Revisa los resultados de cada ejecución en el panel inferior (resultados de SELECT) y en la sección de mensajes para DDL/DML.

## Buenas prácticas y consideraciones al ejecutar en db-fiddle

Orden: Respeta el orden DDL → INSERT → QUERY/UPDATE/DELETE.

Autoincrement / tipos: Si el DDL usa AUTO_INCREMENT, JSON, TIMESTAMP DEFAULT CURRENT_TIMESTAMP u otras características específicas de MySQL 8.0, confirma que db-fiddle está en MySQL 8.0.

Nombres y comillas: MySQL utiliza backticks (`) para identificadores; si exportas a PostgreSQL habrá que transformar backticks a dobles comillas ("") o eliminarlos.

Transacciones: db-fiddle ejecuta sentencias tal cual; si necesitas agrupar operaciones usa START TRANSACTION; ... COMMIT;.

Tamaño de resultado: Si las consultas SELECT devuelven muchas filas, db-fiddle mostrará paginación en el panel de resultados.

Persistencia: Ten en cuenta que cada "Run" en db-fiddle genera un estado aislado del esquema dentro de la sesión — si recargas la página puedes perder el estado. Es recomendable mantener los scripts guardados localmente y re-ejecutarlos si hace falta.


## Verificación y pruebas (ejemplos)

Después de ejecutar INSERT.sql, ejecutar en db-fiddle algunos SELECTs de QUERY.sql para validar:

-- Ejemplo: contar registros por tabla
SELECT 'users' AS tabla, COUNT(*) FROM users;
SELECT 'terminals' AS tabla, COUNT(*) FROM terminals;
SELECT 'devices' AS tabla, COUNT(*) FROM devices;

-- Ejemplo: obtener últimos 5 eventos de cámaras
SELECT * FROM cameras ORDER BY created_at DESC LIMIT 5;


Resultados esperados: filas devueltas y contadores coherentes con el contenido de INSERT.sql. Si los contadores son menores a lo esperado, revisa si algunas inserciones fallaron por FK.

## Notas sobre los archivos entregados

* DDL/Database.sql — contiene la definición de tablas y claves tal como fue diseñada por el equipo. Revisar los CREATE TABLE por AUTO_INCREMENT, restricciones NOT NULL y FOREIGN KEY.

* DML/INSERT.sql — contiene las inserciones de datos iniciales. Verificar que el número y orden de INSERTs respete dependencias.

* DML/QUERY.sql, DML/UPDATE.sql, DML/DELETE.sql — ejemplos de consultas para verificar, actualizar y eliminar datos una vez que la base está poblada.


## Licencia y créditos

Este repositorio entrega material académico para la Actividad Integradora N°5 — Programación I. Documentación y scripts desarrollados por el equipo listado en este README.