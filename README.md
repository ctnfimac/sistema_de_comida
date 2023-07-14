# Sistema de Comidas


Tecnologías utilizadas
- Django
- Postgres
- Bootstrap


#####Pasos para instalar el proyecto en tu computadora
Previamente hay que tener instalado:
- [Git](https://git-scm.com/) 
- [Docker](https://www.docker.com/) 
- [Docker compose](https://docs.docker.com/compose/) 


1) Clono el proyecto del repositorio, abro una terminal y ejecuto:
```
git clone https://github.com/ctnfimac/sistema_de_comida.git
```


2) Me muevo a la carpeta del proyecto
```
cd sistema_de_comida
```

3) Para crear la imagen, los 3 contenedores y los volumenes.
```
docker-compose up [-d]
el parámetro -d es opcional
```

4) Verifico si se crearon los 3 contenedores: comida.web, comida.db y comida.cliente_db
```
docker ps
```

5) abro un explorador y entro a la siguiente uri
```
 http://127.0.0.1:8000/web/
```

6) para detener los contenedores
```
docker-compose stop
```

6) para iniciar los contenedores
```
docker-compose start
```