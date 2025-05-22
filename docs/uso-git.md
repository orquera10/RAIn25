## Uso de Git

Crear una rama o branch llamada prueba:

    git branch prueba

Cambiar a esa rama:

    git checkout prueba

Listar las ramas para ver que se esté bien parado.

    git branch

Hacer los cambios necesarios y enviarlos al staging area.

    git add archivo

O, si queremos pasar todos los archivos, hacer:

    git add .

Luego, crear un commit con un mensaje:

    git commit -m "Comentario sobre los cambios hechos"

Una vez que se terminaron de hacer todos los commits necesarios y se los quiere fusionar a la rama principal, tener cuidado de no dejar archivos con cambios sin commit. Pararse en la rama principal:

    git checkout main

Fusionar los commits de la rama prueba en main:

    git merge prueba

Se puede seguir trabajando en prueba:

    git checkout prueba

O se la puede borrar:

    git branch -D prueba

Cuando se quieran subir los cambios a la nube, es decir, a GitHub, cambiarse a la rama principal:

    git checkout main

Y luego "empujar" todos los commits nuevos a la rama main de GitHub (se llama origin/main)

    git push
