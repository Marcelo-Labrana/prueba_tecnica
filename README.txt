1)   $ pip install Flask
     $ pip install pandas
2) Ejecutar app.py
3) Abrir localhost:5000 en el navegador
4) Seguir los pasos explicados en la web app.
5) En caso de que lo explicado en la página no esté del todo claro: 
    -En localhost:5000/ hay que clickear en el botón "1. Subir data.db" y seleccionar el archivo data.db
    (hay una copia en la carpeta del proyecto), luego hacer click en el botón "2. Procesar", esto generará
    el archivo output.csv en la carpeta del proyecto, donde estará almacenada la data de data.db .
    -En localhost:5000/menu se presentan dos opciones:
        1.  a."Seleccionar nuevos productos": es para seleccionar un csv con productos nuevos en el formato del csv principal.
            b. "Cargar Nuevos Productos" : carga los nuevos productos al csv principal y la rest api.
        2. "Consultar Productos" : redirecciona a una api en formato json, printea la data en la consola del 
        ejecutable y actualiza la información del output.csv hacia la api.