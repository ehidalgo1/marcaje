# marcaje
El proyecto trata de una aplicación simple de marcaje desarrollada en mis tiempos libres
Se utilizó:

lenguaje de programación: Python
javascript
HTML 5
bootstrap 4
css

La base de datos esta montada en postgreSQL

# Instrucciones de instalación

Una vez descargado el proyecto antes de ejecutar se debe tener instalado los siguientes componentes para que esta pudiese ser ejecutada.

- Python (3.8 o ultima version más estable)
- PostgreSQL (ultima version más estable)
- alternativa para ejecutar (VS CODE o ATOM)

# Antes de ejecutar el proyecto

- Crear base de datos en posgreSql con el nonmbre de "marcaje_db"
- Al abrir el proyecto ejecutar los siguientes comando por la consola del IDE que esten utilizando. (presionar ENTER o INTRO después de cada comando)

  python manage.py makemigrations
  
  python manage.py migrate
  
  python manage.py runserver
  
  
 - El último comando ejecutará el proyecto y podrá utilizarlo sin problemas
