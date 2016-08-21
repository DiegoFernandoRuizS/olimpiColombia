##[Olimpi- Colombia](http://olimpi-colombia.herokuapp.com)

Esta aplicación permite ver la actividad de la representación colombiana en los juegos olimpicos RIO 2016.


### Url kanbanflow
* https://kanbanflow.com/board/4b427c27c3e54ddee7861ad55d483ae8

### Url repositorio github
* https://github.com/Rocket-Team/olimpiColombia.git

### Url Integración continua en codeship
* https://codeship.com/projects/168050

### Url despligue continuo en heroku
* https://dashboard.heroku.com/apps/olimpi-colombia

### Url del sitio desplegado
* http://olimpi-colombia.herokuapp.com


##  Pasos para usar el repositorio

### Clonar el repositorio

Clonar el repositorio usando git y configurar los credenciales

```
git clone "https://github.com/itaimal/olimpiColombia.git"
cd olimpiColombia
git config user.name "{{your user}}"
git config user.email "{{your email}}"
git config credential.helper store
git pull
```

### Subir un cambio al repositorio
Cada que se suban cambios al repositorio, estos cambios generan un despliegue en 
http://olimpi-colombia.herokuapp.com
```
git commit -m "Commentario relacionado con el commit"
git push
```

### Ejecutar la aplicacion en servidor local de pruebas

```
python manage.py runserver
```

El resultado se puede visualizar en http://127.0.0.1:8000


### Ejemplos de uso de Heroku Toolbelt
https://toolbelt.heroku.com/ Para ejecutar commandos en Heroku,
```
heroku run python manage.py makemigrations polls --app olimpi-colombia
heroku run python manage.py migrate polls --app olimpi-colombia
heroku run python manage.py createsuperuser --app olimpi-colombia
```


Clases:
```
---------------------
|      Sport        |
| -name             |
| -description      |
| -urlImage         |
| -icon             |
---------------------
```
