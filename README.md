# Prueba Tecnica
Repositorio con los archivos correspondientes a la prueba tecnica solicitada por TalentPitch para el rol de Data Engineer

## Configuración del Proyecto
### Requisitos previos: </br>
* Tener instalado docker en tu sistema operativo, si no lo tienes instalado puedes descargarlo siguiendo el link dependiendo de tu sistema operativo</br>
  * sistemas operativos linux: </br>
    https://docs.docker.com/engine/install/ubuntu/
  * sistemas operativos unix (mac os): </br>
    https://docs.docker.com/desktop/install/mac-install/
  * sistemas operativos windows: </br>
    https://docs.docker.com/desktop/install/windows-install/ 
* PASO 1. Clonar el repositorio </br>
  <git clone https://github.com/Lina-Arroyo/PruebaTecnica.git>
* PASO 2. Lee el archivo 'rquirements.txt' en el encontraras las dependencias necesarias para ejecutar airflow de manera local en un ambiente docker
* PASO 3. Ingresar a la linea de comandos o bash de tu computadora
  * sistemas operativos linux: </br>
    Pulsa las teclas (control + alt + t)
  * sistemas operativos unix (mac os): </br>
    Pulsa las tecla (control y la barra espaciadora) para abrir Spotlight, escribir “Terminal” y hacer doble clic en el resultado de la búsqueda
  * sistemas operativos windows: </br>
    Pulsa las teclas ([Windows] + [R]), escribe “cmd” en el cuadro y pulsa “OK” para abrir cmd.exe
* PASO 4. Desde la linea de comandos ingresar a la carpeta donde se clono el repositorio</br>
    Ejemplo: C:\Users\Lina_\onedrive\Escritorio\PruebaTecnica>
* PASO 5. Prueba que Docker este funcionando correctamente ejecuntando <docker ps -a> </br>
* PASO 6. Una vez que verifiques que docker se esta ejecutando correctamente ejecuta el siguiente comando 'docker compose up' esto hara que se descarguen
    las imagenes especificadas en el docker-compose.yml con las configuraciones del Dockerfile que estan dentro del repositorio que clonaste, con este comando <docker compose up> se crean y ejecutan los contenedores necesarios para trabajar con airflow
* PASO 7. Una vez se terminen de crear y ejecutar los contenedores el webserver de airflow ya esta listo para que naveges en el
* PASO 8. Ingresa al webserver de airflow ingresando en tu navegador esta url <http://127.0.0.1:8080/> inicia sesion con las siguientes credenciales:</br>
        user: airflow</br>
        password: airflow</br>
* PASO 9. Ejecuta los DAG´s esto lo puedes hacer haciendo click en el botón "Activar" en la interfaz de usuario de Airflow. Los DAGs se ejecutarán de acuerdo con su  programación.
* PASO 10. Si deseas detener los contenedores desde la consola en la que creaste los contenedores oprime las teclas(control + c) esto empezara a detener los contenedores uno a uno, si lo que deseas es detener los contenedores y eliminarlos ejecuta el comando <docker compose down> esto dentendrá y eliminara los contenedores y las redes creadas para ejecutar los contenedores 
## ¡Listo ya ejecutaste airflow de manera local en un ambiente Docker!
</br>

# Especificaciones del contenido del repositorio
* dags: </br>
Esta carpeta contiene el archivo de definicion de los dag´s creados
* Data </br>
Esta carpeta contiene el csv disponibilizado para realizar la prueba
* logs </br>
Esta carpeta contiene el historial de acciones que realiza cada dag
* pluggins </br>
Esta carpeta aunque no tiene archivos, puede contener archivos de python para la personalización de airflow
* Scripts </br>
Esta carpeta tiene un archivo .py con la definicion de las funciones usadas para la creación del dag
* Docker-compose.yml </br>
Este archivo contiene la configuracion de los contenedores para la ejecucion de airflow
* Dockerfile </br>
Este archivo contiene la especificacion de la imagen de airflow usada en los contenedores del docker-compose
adicional instala las dependencias especificadas
* requirements.txt </br>
Este archivo contiene las dependencias usadas para ejecutar airflow y su versión 