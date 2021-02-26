Este código fue diseñado para poder reservar turnos en las distintas sedes de Megatlon de forma automática.
Su uso es personal.
La automatización del código sirve únicamente si se corre en una computadora conectada a internet y sin apagar.
Si el programa se corta, basta con correrlo de vuelta y mantener la computadora encendida.

Instalación de paquetes:
   En la terminal de su máquina, es necesario instalar (en caso de o tenerlo instalado ya):
        - Python 3 --> https://www.python.org/downloads/
        - Schedule --> pip install schedule     (Más info: https://pypi.org/project/schedule/)
        - Selenium --> pip install -U selenium  (Más info: https://pypi.org/project/selenium/)

Una vez finalizada la instalación, hace falta modificar el código como figura a continuación y luego, desde la misma terminal:

    $ cd Desktop/megatlon/            # Nota: Es necesario estar ubicados en la carpeta correcta para poder ejecutar el programa
    $ python3 main.py

# Para saber ubicarse en una carpeta en su terminal,
    sugiero el siguiente link para Windows: https://www.falconmasters.com/offtopic/como-utilizar-consola-de-windows/
    sugiero el siguiente link para Linux/Mac: https://macpaw.com/es/how-to/use-terminal-on-mac

## Nota 2: el símbolo $ representa la terminal, no se debe incluir al correrlo

 Cualquier consulta, puede escribirme al siguiente mail: mp.coding.ar@gmail.com
-------

Para poder utilizar este código es necesario modificar los datos en main.py:
    - Megatlon("user@mail.com", "password"), colocar su mail y su contraseña entre las ""
    - (user.reserve_class, "Megatlon Sede", "dia", "clase", "hora"),
            colocar la sede a la que desea asistir SIN errores ortográficos,
            el día con el formato que figura en la página ("lun", "mar", "mié", "jue", "vie", "sáb", "dom"),
            la clase (Ej: "Musculación + Cardio"),
            y la hora ("07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22")

Nótese que hay distintas opciones para cuándo se desea reservar el turno:

 schedule.every().monday.at(9).do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")

Este código está indicando que se desea que cada lunes a las 9am se reserve tal clase, puede modificar la hora (formato 24 horas)
Si no se desea reservar una clase los lunes, puede borrar esa linea de codigo o comentarla con un # al principio de la misma
Para mayor facilidad, ya cuenta con todos los días de la semana programados, únicamente tiene que editarlos a su gusto

Por último, recordar que Megatlon sólo permite anotarse a una clase hasta 72hs antes y sólo una reserva por día

Espero que disfruten de este código y puedan sacarle provecho para estar cada día un poco más sanos


Sedes:
"Megatlon Alcorta"
"Megatlon Almagro"
"Megatlon Alto Palermo"
"Megatlon Alto Rosario"
"Megatlon Ateneo de la Juventud"
"Megatlon Barracas"
"Megatlon Barrio Jardín (Córdoba)"
"Megatlon Barrio Norte"
"Megatlon Belgrano"
"Megatlon Caballito"
"Megatlon Caballito II"
"Megatlon Center"
"Megatlon Center II"
"Megatlon Centro (Córdoba)"
"Megatlon Cerro (Córdoba)"
"Megatlon Devoto"
"Megatlon Distrito Arcos"
"Megatlon Distrito Tecnológico"
"Megatlon Floresta"
"Megatlon Gonnet"
"Megatlon La Imprenta"
"Megatlon Martínez"
"Megatlon Martínez II"
"Megatlon Núñez"
"Megatlon Olivos"
"Megatlon Pilar"
"Megatlon Puerto Madero"
"Megatlon Racing Club"
"Megatlon Recoleta"
"Megatlon Rosario"
"Megatlon Villa Crespo"
"Megatlon Outdoor Rubén Darío"
"Megatlon Outdoor Parque Centenario"
"Megatlon Outdoor Palermo"







