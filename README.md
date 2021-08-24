<h1>Gmail_API</h1>
<h2>Contenido del repositorio</h2>
<p>
Este repositorio se divide en dos proyectos:
<ul>
<li>Un script capaz de conectarse a la API de Gmail y mostrar cuantos correos sin leer tenemos en cada una de las cuentas definidas en un archivo XLSX externo. Los archivos que constituyen este proyecto son:
<ul>
<li>unreadMails.py</li>
<li>unreadMails.xlsx</li>
</ul>
</li>
<br>
<li>Un script capaz de conectarse a la API de Gmail y enviar un mensaje derterminado (texto plano/HTML) a una lista de cuentas determinadas. La lista de mails, el asunto, el remitente, y el cuerpo del mensaje se deben introducir correctamente en el archivo XLSX adjunto. Los archivos que constituyen este proyecto son:
<ul>
<li>sendMails.py</li>
<li>sendMails.xlsx</li>
</ul>
</li>
</ul>
</p>
<h2>Indicaciones</h2>
<p>❗ Para poder pasar todos los filtros que nos impone Google para conectarnos a la API del Gmail, debemos realizar dos acciones previas:
<ul>
<li>Permitir el acceso de aplicaciones poco seguras en el apartado "<i>Acceso de aplicaciones poco seguras</i>" que podremos encontrar en la configuración de la Seguridad de nuestra cuenta de Gmail (https://myaccount.google.com/security)</li>
<li>Permitir el acceso a nuestra cuenta de Google para que nuestro script sea capaz de iniciar sesión en Gmail. Podemos activar el permiso a través del siguiente enlace: https://accounts.google.com/b/0/DisplayUnlockCaptcha (su activación es temporal, por lo que puede que tengamos que volver a activarlo transcurrido un tiempo)</li>
</ul>
</p>
<p>❗ Es necesario importar específicamente la versión 1.2.0 de la libreria "xlrd" de Python para poder abrir archivos XLSX. Para ello, podemos aplicar en la consola el siguiente comando: <i>pip install xlrd==1.2.0</i></p>
<p>❗ Para que el programa se ejecute correctamente, es necesario introducir los datos correspondientes en el archivo XLSX respetando el orden establecido en las columnas</p>
<p>❗ El mensaje introducido en el archivo XLSX en lenguaje HTML tiene prioridad sobre el mensaje escrito en texto plano, de forma que si queremos enviar un escrito sin etiquetado, deberemos dejar vacía la columna "HTML TEXT" y rellenar únicamente la columna "TEXT"</p>
<h2>Estado</h2>
<p><strong>✔️ FINALIZADO</strong></p>
<p>📅 Ultima modificación: <strong>24/08/2021</strong></p>
