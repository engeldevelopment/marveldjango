# MarvelInDjango :1st_place_medal:
Un API de Marverl con Django.

Esta app es una práctica que queria realizar desde hace mucho tiempo!

En esta api podrás ver los Personajes de marvel a través del end point **/api/marvel/v1/characters/** y también,
podrás filtrarlos según su género: 
  * Heroes = h  :point_right:   /api/marvel/v1/characters/?g=h
  * Villians = v :point_right:  /api/marvel/v1/characters/?g=v


## ¿Cómo poner en marcha este proyecto? :construction_worker:

Para poner en marcha este proyecto, necesitas tener instalado python => 3.6.

Los pasos son:
  * Clona el proyecto y déjame una :star: al repo :smile:
  * Crea un entorno virtual con **virtualenv** o **virtualenvwrapper**
    ```bash
      virtualenv -p python3 marvel  
      source marvel/bin/activate
    ```
  * Instala las dependencias con este comando:
    ```bash
      pip install -r requirements/dev.txt
     ```
  * Corre el proyecto :smile:
    ```bash
      make run
    ```

## El Makefile :page_facing_up:


Listado de Comandos:

  * ``` make run``` correrá el proyecto
  * ``` make lint``` revisará la calidad del código según el PEP8 y otros estandares de calidad
  * ``` make coverage``` correrá los test y el linter para saber la covertura del código y la salud del proyecto
  * ``` make test``` correrá los tests
  * ``` make migrate``` correrá las migraciones de tus modelos
  * ``` make rm``` eliminará archivos basuras del proyecto
  
  
  
  
