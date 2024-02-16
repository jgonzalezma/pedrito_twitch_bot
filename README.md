# Project Title

IA basada en otro IA de Twitch llamado "a_n_i_v" que interactúa en el chat como si fuese una persona.

# Requerimientos

- Python 3.11.8 (o superior)
- Librería de twitchio
- Librería de markovify
# Instalación 
Para la instalación de esta IA necesitaremos tener Python 3.11.8 (o superior) instalado en nuestro ordenador. En la carpeta donde vayamos a guardar el proyecto, debemos hacer varias instalaciones usando la terminal, vamos a instalar un par de librerías:

- pip install twitchio
- pip install markovify

Twitchio es la librería que usamos para conectarnos con la API de Twitch. Markovify es la librería que usamos para generar los mensajes del chat de la IA.

Lo suyo ahora es instalar el editor de código que mas te guste (Visual Studio, Notepad++, Sublime Text...).

Ahora necesitaremos crear un archivo de configuración, por defecto lo llamamos "config.secret". Aquí irá la información de tokens de Twitch y demás que no queremos que se vea en el código (ya que es información sensible). De momento el archivo debería quedar así: 

TOKEN=   
CLIENT_ID=  
BOT_NICK=nombre_que_quieras_para_el_bot  
BOT_PREFIX=!  
CHANNEL=tu_canal

Lo siguiente será crear la cuenta de Twitch del bot (IA) con el nombre que queramos. Una vez creado, tenemos que coger el client_id desde aquí: https://dev.twitch.tv/console/apps/create Tenemos que crear y registrar la aplicación, una vez hecho esto tendremos el "ID de cliente" que copiaremos y pegaremos en "config.secret" donde el "CLIENT_ID". En principio nos redirigirá y nos saldrá también el token de autenticación que pondremos donde pone "TOKEN" en el archivo de "config.secret".

Una vez tengamos todo esto, solo faltaría crear nuestro archivo "chat.txt" que es donde almacenaremos todo el chatlog de donde sacará las frases la IA. Lo suyo sería rellenar el archivo con algún chatlog que tengamos para que tenga algo con lo que trabajar la IA, pero lo bueno es que cada vez que esté el bot activo irá registrando todo lo que se escriba en el chat en el que esté y tendrá cada vez más información con la que trabajar y aprender.

# Como Utilizarlo

Simplemente abrimos la terminal y nos colocamos donde tengamos nuestro archivo "mi_aniv.py" y escribimos "python mi_aniv.py". Esto ejecutar el programa y ya debería estar el bot perfectamente funcionando.
