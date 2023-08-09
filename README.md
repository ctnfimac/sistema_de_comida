# Sistema de Comidas


Tecnologías utilizadas
- Django
- Postgres
- Bootstrap
- Javascript


##### Pasos para instalar el proyecto en tu computadora
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

6) Renombro el archivo de las **variables de entorno**, previo a esto tengo que completar los datos de dicho archivo
```
  mv app/._env app/.env
```

7) para detener los contenedores
```
docker-compose stop
```

8) para iniciar los contenedores
```
docker-compose start
```

##### Ejecutar test unitarios
```
docker exec comida.web python manage.py test
```


#### Posibles Errores:
.) Al levantar el proyecto puede suceder que en linux haya problemas con el contenedor de pgadmin4 por tema de permisos.
mensaje del error: 
``` Permission denied: '/var/lib/pgadmin/sessions' ```
##### Soluciones:

Una solución es agregar la siguiente linea de código a la configuración del pgadmin del docker-compose.yml 
``` user: root ``` 
quedando así
```
  db_client:
    image: dpage/pgadmin4
    container_name: comida.cliente_db
    user: root
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@gmail.com
      PGADMIN_DEFAULT_PASSWORD: admin
    volumes:
      - ./pgadmin_data:/var/lib/pgadmin4
    ports:
      - "80:80"
 ```
Otra posible solución:
 ```
 modificar:  ./pgadmin_data:/var/lib/pgadmin
 por:        ./pgadmin_data:/var/lib/pgadmin4/storage
 ```

 una vez hecho estos cambios eliminar el contenedor, imagenes y los volumenes
 para levantarlo nuevamente con **docker-compose up [-d]**

