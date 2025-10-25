Este folder contiene el **DML** solicitado en la AI-6:
- Inserts suficientes por tabla
- Consultas simples por tabla
- **≥ 4 consultas multitabla (JOIN)**
- **≥ 2 subconsultas**

Se deben instalar librerias:
pip install mysql-connector-python
pip install python-dotenv

## Archivos
- `DML.sql` — ejecutar en el motor indicado (ver más abajo).

## Motor/DBMS recomendado (online)
- **MySQL 8.0** (OneCompiler / dbfiddle / RunSQL)
- Alternativa local: MySQL 8.0 o MariaDB 10.5+

## Orden de ejecución
1. Asegurarse de tener el **DDL** creado previamente con estas tablas (en español):
   - `usuarios`, `terminales`, `dispositivos`, `camaras`, `dispositivos_moviles`,
     `automatizaciones`, `automatizacion_dispositivo`.
2. Ejecutar `DML.sql` completo (inserts + consultas).

> Si tu esquema difiere (nombres en inglés, otra convención), adapta los nombres en las sentencias.

## Notas
- Los `device_id` usados por las cámaras presuponen autoincremento consecutivo a partir de los inserts de `dispositivos`. Si tu motor no asigna así, ajusta manualmente los `device_id` en `INSERT INTO camaras`.
- Las consultas están comentadas y ordenadas (simples → JOINs → subconsultas).

## Variables de entorno (para la app)
Verificar el archivo .env, este mismo se adjunta por afuera de github (se sube en la carpeta de entrega de la evidencia)