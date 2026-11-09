# Spanish pages (/es/). Neutral Spanish for Latin America and Spain.
from content_v2 import S_MDN, S_NBER

NOTA_AZAR = ("Wheelova usa la función `crypto.getRandomValues()` de tu navegador. Según MDN, los navegadores la implementan como un "
             "generador pseudoaleatorio criptográficamente seguro, alimentado con entropía del sistema: el mismo tipo de fuente que se usa "
             "para funciones de seguridad. En la práctica es impredecible, aunque no es un dispositivo físico de \"azar verdadero\".")

PALETA = ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]
NOMBRES = ["Sofía", "Mateo", "Valentina", "Santiago", "Camila", "Sebastián", "Lucía", "Diego", "Isabella", "Martín"]

UI = {
 "lang": "es",
 "spin_hint": "Pulsa GIRAR o la barra espaciadora",
 "spin": "GIRAR", "spin_aria": "Girar la ruleta",
 "entries": "Opciones", "shuffle": "Mezclar", "sort": "Ordenar", "clear": "Borrar",
 "help": "Una opción por línea. Se guarda automáticamente en tu navegador.",
 "remove": "Quitar al ganador después de cada giro", "sound": "Sonido",
 "results": "Resultados", "share": "Compartir enlace", "embed": "Insertar",
 "fullscreen": "Pantalla completa",
 "shared_note": "Abriste una ruleta compartida.", "my_list": "Volver a mi lista",
 "pop_remove": "Quitar de la ruleta", "close": "Cerrar",
 "share_title": "COMPARTIR ESTA RULETA",
 "share_help": "Quien tenga este enlace podrá ver tus opciones: van codificadas dentro del enlace (no cifradas). No guardamos nada en nuestro servidor, pero el enlace queda en el historial del navegador y donde lo pegues, así que evita compartir listas privadas.",
 "link": "Enlace", "copy": "Copiar",
 "embed_label": "Código para insertar: pégalo en tu web, blog o en OBS como fuente de navegador",
 "copy_embed": "Copiar código",
 "how": "Cómo usar la", "faq": "Preguntas frecuentes", "related": "Otras ruletas",
 "crumb_home": "Wheelova", "crumb_hub": "Ruletas",
 "rand_src": "Azar: Wheelova usa <a href=\"https://developer.mozilla.org/es/docs/Web/API/Crypto/getRandomValues\" rel=\"noopener\">crypto.getRandomValues()</a> del navegador (MDN Web Docs).",
 "sources": "Fuentes:",
}

JS = {  # strings used by app.js
 "add2": "Añade al menos dos opciones", "spinning": "Girando…", "winner": "GANADOR", "pop": "¡TENEMOS GANADOR!",
 "empty": "Añade opciones", "add2share": "Añade al menos dos opciones para compartir", "copied": "Copiado",
 "copy": "Copiar", "copy_embed": "Copiar código", "share_title": "COMPARTIR ESTA RULETA", "embed_title": "INSERTAR ESTA RULETA",
 "long": "La lista es larga, así que el enlace también ({n} caracteres). Funciona, pero algunas apps de mensajería podrían cortarlo.",
 "iframe_title": "Gira la ruleta – Wheelova", "credit_pre": "Ruleta de",
 "fs": "Pantalla completa", "exitfs": "Salir de pantalla completa", "openmenu": "Abrir menú", "closemenu": "Cerrar menú",
 "todark": "Cambiar a modo oscuro", "tolight": "Cambiar a modo claro",
 "cleared": "Lista borrada.", "imported": "Se importaron {n} entradas.", "impcut": "Solo se conservaron las primeras 2000.", "impempty": "No se encontraron entradas en ese archivo.", "impbig": "El archivo es demasiado grande (máximo 5 MB).", "impxls": "Guarda la hoja como CSV primero, o copia la columna y pégala.", "col": "Columna", "replaced": "Lista reemplazada.", "kept": "Ruleta compartida guardada como tu lista.",
 "nrange": "Indica un rango en el que «Hasta» sea mayor que «Desde».", "nmax": "Hasta 500 números por ruleta.", "csv_spin": "Giro", "csv_winner": "Ganador", "csv_time": "Hora", "load": "Cargar", "loaded": "Cargada", "del": "Eliminar", "deleted": "Eliminada",
 "needname": "Escribe primero un nombre para esta ruleta.", "updated": "Actualizada", "saved": "Guardada", "full": "Puedes guardar hasta 50 ruletas. Elimina una primero.",
}

NAV_ES = [("es/ruleta-de-nombres", "Ruleta de nombres"), ("es/ruleta-si-o-no", "Sí o no"), ("es/ruleta-de-sorteo", "Sorteos"), ("es/ruleta-de-decisiones", "Decisiones"), ("", "English")]

ES = [
# ------------------------------------------------------------------ HOME
{
 "slug": "es", "en": "", "key": "es_home", "nav": "Ruleta aleatoria", "palette": PALETA,
 "title": "Ruleta aleatoria y virtual – Gira la ruleta online gratis | Wheelova",
 "description": "Ruleta aleatoria online y gratis: escribe nombres u opciones, gira la ruleta y obtén un resultado justo al azar. Sin registro, funciona en el móvil.",
 "h1": "Ruleta aleatoria", "subhead": "Escribe tus opciones, gira la ruleta y deja que el azar decida.",
 "entries": NOMBRES,
 "variants": [{"label": "10 nombres", "entries": NOMBRES}, {"label": "Sí / No", "entries": ["Sí", "No"]}, {"label": "Números 1–10", "entries": [str(i) for i in range(1, 11)]}, {"label": "¿Qué comemos?", "entries": ["Pizza", "Tacos", "Hamburguesa", "Sushi", "Pasta", "Empanadas", "Ensalada", "Pollo asado"]}],
 "howTo": ["Escribe o pega tus opciones, una por línea.", "Pulsa GIRAR (o la barra espaciadora).", "Lee el resultado en la ventana. Activa «Quitar al ganador» si no quieres repeticiones."],
 "sections": [
  {"h2": "¿Qué es una ruleta aleatoria?", "body":
   "Una ruleta aleatoria es una rueda dividida en partes iguales, una por cada opción que escribes. Al girarla, la ruleta se detiene en una de ellas al azar. Como todos ven girar la rueda, el resultado se percibe como justo: nadie puede decir que la elección estaba arreglada.\n\n" + NOTA_AZAR},
  {"h2": "Para qué sirve", "body":
   "**En clase:** elegir quién responde, el orden de las exposiciones o los equipos. La [ruleta de nombres](/es/ruleta-de-nombres) quita a cada alumno después de salir para que todos tengan su turno.\n\n"
   "**Sorteos y concursos:** pega a los participantes y gira en directo. La [ruleta de sorteo](/es/ruleta-de-sorteo) explica cómo hacerlo de forma justa.\n\n"
   "**Decisiones del día a día:** qué cenar, qué película ver o quién lava los platos. Prueba la [ruleta de decisiones](/es/ruleta-de-decisiones) o la [ruleta sí o no](/es/ruleta-si-o-no).\n\n"
   "**Juegos y fiestas:** retos, turnos, premios o castigos divertidos."},
  {"h2": "Probabilidades: qué tan justa es la ruleta", "body":
   "Todas las partes tienen el mismo tamaño, así que la probabilidad de cada opción es **1 ÷ número de opciones**:\n\n"
   "| Opciones | Probabilidad de cada una |\n|---|---|\n| 2 | 50 % |\n| 4 | 25 % |\n| 6 | 16,7 % |\n| 10 | 10 % |\n| 20 | 5 % |\n\n"
   "Para que una opción salga más, escríbela dos veces. Con «Sí, Sí, No», el Sí tiene 2 de 3 probabilidades (un 67 %). Que la misma opción salga dos veces seguidas es normal: cada giro es independiente del anterior."},
  {"h2": "Una alternativa a la ruleta de Google", "body":
   "Mucha gente busca la «ruleta de Google». Wheelova es una herramienta independiente, no de Google, que añade lo que una búsqueda rápida no tiene: tus propias opciones, quitar ganadores, historial de resultados, modo de pantalla completa para el proyector, enlace para compartir y código para insertar la ruleta en tu web o en un directo."},
  {"h2": "Tus opciones son privadas", "body":
   "Lo que escribes se guarda solo en tu navegador, en tu dispositivo. No se sube a nuestros servidores. Al compartir un enlace, las opciones viajan dentro del propio enlace."}
 ],
 "faq": [
  {"q": "¿La ruleta aleatoria es realmente al azar?", "a": "Sí. Usa el generador criptográficamente seguro de tu navegador, y cada giro es independiente del anterior."},
  {"q": "¿Es gratis? ¿Tengo que registrarme?", "a": "Es gratis y no necesitas cuenta. Tus opciones se guardan en tu navegador."},
  {"q": "¿Cómo evito que salga dos veces la misma opción?", "a": "Activa «Quitar al ganador después de cada giro» o pulsa «Quitar de la ruleta» en la ventana del resultado."},
  {"q": "¿Cuántas opciones puedo poner?", "a": "Todas las que quieras. El texto se hace más pequeño cuantas más opciones hay; hasta unas 50 se leen bien."},
  {"q": "¿Puedo usarla para un sorteo?", "a": "Sí. Gira en directo para que todos lo vean. Las normas sobre sorteos cambian según el país, así que revisa las que te apliquen."},
  {"q": "¿Funciona en el móvil?", "a": "Sí, en cualquier navegador moderno, sin instalar nada."}
 ],
 "related": ["es/ruleta-de-nombres", "es/ruleta-si-o-no", "es/ruleta-de-sorteo", "es/ruleta-de-decisiones"],
 "sources": [S_MDN],
},
# ------------------------------------------------------------------ NOMBRES
{
 "slug": "es/ruleta-de-nombres", "en": "name-picker-wheel", "key": "es_names", "nav": "Ruleta de nombres", "removeWinner": True,
 "title": "Ruleta de nombres – Elige un nombre al azar | Wheelova",
 "description": "Ruleta de nombres online y gratis: pega tu lista, gira y elige a alguien al azar. Quita a cada ganador para que todos tengan su turno. Ideal para clase.",
 "h1": "Ruleta de nombres", "subhead": "Pega tu lista de nombres, gira y elige a alguien al azar, de forma justa.",
 "entries": NOMBRES,
 "variants": [{"label": "10 nombres", "entries": NOMBRES}, {"label": "Equipo A / Equipo B", "entries": ["Equipo A", "Equipo B"]}, {"label": "Grupos 1–6", "entries": [f"Grupo {i}" for i in range(1, 7)]}],
 "howTo": ["Pega o escribe los nombres, uno por línea (puedes copiar una columna de Excel o Google Sheets).", "Deja activado «Quitar al ganador» para que nadie salga dos veces.", "Gira. El nombre elegido desaparece de la ruleta para el siguiente turno."],
 "sections": [
  {"h2": "Una ruleta de nombres para clase, equipos y eventos", "body":
   "Pega la lista, gira y la ruleta elige un nombre al azar. Como todos ven girar la rueda, la elección es transparente: nadie puede decir que el profesor o el anfitrión tuvo favoritos.\n\n" + NOTA_AZAR},
  {"h2": "Ideas para el aula", "body":
   "- **Quién responde:** gira para elegir al siguiente alumno y quítalo para que todos participen.\n"
   "- **Orden de exposiciones:** gira hasta vaciar la ruleta; la lista de **Resultados** guarda el orden.\n"
   "- **Encargados de la semana:** gira una vez por cada tarea.\n"
   "- **Parejas de lectura:** gira dos nombres seguidos para formar cada pareja.\n\n"
   "Para que no genere nervios, da tiempo para pensar antes de girar, deja que respondan en pareja y permite «pasar» una vez."},
  {"h2": "Cómo hacer que el sorteo sea justo", "body":
   "- **Una línea por persona.** Un nombre escrito dos veces tiene el doble de probabilidad.\n"
   "- **Revisa la ortografía.** «Jose» y «José» cuentan como dos personas distintas.\n"
   "- **Usa «Quitar al ganador»** cuando cada persona deba salir solo una vez.\n\n"
   "En una clase de 30, cada alumno tiene un 3,3 % en el primer giro. Con «Quitar al ganador», el segundo giro es 1 entre 29, luego 1 entre 28, y así hasta que todos han salido."},
  {"h2": "Equipos, oficinas y eventos", "body":
   "Úsala para decidir quién habla primero en una reunión, quién se encarga de la siguiente tarea o quién gana un premio en un evento. Para muchos participantes, la [ruleta de sorteo](/es/ruleta-de-sorteo) explica cómo hacerlo con registro."},
  {"h2": "Privacidad", "body":
   "Los nombres se guardan solo en tu navegador. No se suben ni se comparten. Pulsa **Borrar** para eliminarlos."}
 ],
 "faq": [
  {"q": "¿Cuántos nombres puedo poner?", "a": "Todos los que quieras. Hasta unos 50 se leen bien en un proyector."},
  {"q": "¿Cómo evito que salga dos veces el mismo nombre?", "a": "Deja activado «Quitar al ganador después de cada giro»."},
  {"q": "¿Puedo pegar nombres desde Excel o Google Sheets?", "a": "Sí. Copia una columna y pégala: cada celda se convierte en una línea."},
  {"q": "¿Los nombres son privados?", "a": "Sí. Se guardan solo en tu navegador, en este dispositivo."},
  {"q": "¿Sirve como ruleta para un sorteo?", "a": "Sí. Escribe cada participante una sola vez y gira en directo."}
 ],
 "related": ["es", "es/ruleta-de-sorteo", "es/ruleta-si-o-no", "es/ruleta-de-decisiones"],
 "sources": [S_MDN],
},
# ------------------------------------------------------------------ SI O NO
{
 "slug": "es/ruleta-si-o-no", "en": "yes-or-no-wheel", "key": "es_sino", "nav": "Sí o no",
 "title": "Ruleta sí o no – Gira y obtén una respuesta al azar | Wheelova",
 "description": "Ruleta sí o no gratis: haz una pregunta, gira y la ruleta responde. Añade «Tal vez» o cambia las probabilidades. Sin registro.",
 "h1": "Ruleta sí o no", "subhead": "Haz una pregunta, gira y deja que la ruleta responda sí o no.",
 "entries": ["Sí", "No"], "resultLabel": "LA RESPUESTA ES", "popLabel": "LA RULETA DICE",
 "variants": [{"label": "Sí / No", "entries": ["Sí", "No"]}, {"label": "Sí / No / Tal vez", "entries": ["Sí", "No", "Tal vez"]}, {"label": "Sí / No / Pregunta otra vez", "entries": ["Sí", "No", "Pregunta otra vez"]}],
 "howTo": ["Piensa en una pregunta de sí o no.", "Pulsa GIRAR (o la barra espaciadora).", "Lee la respuesta. Si quieres, juega al mejor de tres."],
 "sections": [
  {"h2": "¿Cómo funciona la ruleta sí o no?", "body":
   "La ruleta tiene dos mitades iguales, **Sí** y **No**. Cada giro cae en una de ellas al azar, como lanzar una moneda pero viéndolo girar. Puedes añadir «Tal vez» o cambiar las probabilidades añadiendo más partes.\n\n" + NOTA_AZAR},
  {"h2": "Probabilidades", "body":
   "| Ruleta | Sí | No | Otra |\n|---|---|---|---|\n"
   "| Sí, No | 50 % | 50 % | — |\n| Sí, No, Tal vez | 33,3 % | 33,3 % | Tal vez 33,3 % |\n| Sí, Sí, No | 66,7 % | 33,3 % | — |\n\n"
   "**Las rachas son normales.** Con una ruleta 50/50, que salga la misma respuesta tres veces seguidas pasa una de cada cuatro veces."},
  {"h2": "Úsala para descubrir lo que de verdad quieres", "body":
   "Gira y fíjate en tu primera reacción. ¿Sientes alivio cuando sale «No»? Probablemente no querías hacerlo. ¿Te decepciona? Seguramente querías el «Sí». No es ciencia, pero ayuda a decidir más rápido que otra lista de pros y contras."},
  {"h2": "Buenas preguntas para la ruleta", "body":
   "**Del día a día:** ¿pido comida hoy? ¿Voy al gimnasio? ¿Veo otro capítulo?\n\n"
   "**Juegos y clase:** ¿este equipo gana un punto extra? ¿Jugamos otra ronda?\n\n"
   "**Desempates:** cuando un grupo está dividido, acuerden antes de girar que todos aceptarán el resultado.\n\n"
   "Úsala cuando las dos respuestas sean aceptables. Para temas de salud, dinero o asuntos legales, busca información o asesoría primero."},
  {"h2": "Ruleta sí o no o moneda", "body":
   "Las dos dan un 50/50. La ruleta se ve mejor en pantalla (clase, directos, videollamadas), permite añadir «Tal vez» y cambiar las probabilidades, algo que una moneda no puede hacer. Para más de dos opciones, usa la [ruleta de decisiones](/es/ruleta-de-decisiones)."}
 ],
 "faq": [
  {"q": "¿La ruleta sí o no es 50/50?", "a": "Sí. Con las dos opciones por defecto, cada una tiene un 50 %."},
  {"q": "¿Puedo añadir «Tal vez»?", "a": "Sí. Pulsa el ajuste «Sí / No / Tal vez». Cada opción tendrá entonces un 33,3 %."},
  {"q": "¿Cómo hago que el Sí salga más?", "a": "Escribe Sí dos veces. Con «Sí, Sí, No», el Sí tiene un 67 %."},
  {"q": "¿Por qué me sale siempre lo mismo?", "a": "Las rachas son normales en el azar: tres respuestas iguales seguidas pasan una de cada cuatro veces."},
  {"q": "¿Debo usarla para decisiones importantes?", "a": "Úsala para desempatar entre opciones que ya te parecen bien. Para decisiones serias, busca información o asesoría primero."}
 ],
 "related": ["es/ruleta-de-decisiones", "es", "es/ruleta-de-nombres", "es/ruleta-de-sorteo"],
 "sources": [S_MDN],
},
# ------------------------------------------------------------------ SORTEO
{
 "slug": "es/ruleta-de-sorteo", "en": "raffle-wheel", "key": "es_sorteo", "nav": "Sorteos", "removeWinner": True,
 "title": "Ruleta de sorteo y rifas online – Elige ganadores al azar | Wheelova",
 "description": "Ruleta de sorteo online y gratis: pega participantes o números de boleto, gira en directo y quita a cada ganador. Ideal para sorteos en redes y rifas.",
 "h1": "Ruleta de sorteo", "subhead": "Elige a los ganadores de tu sorteo o rifa en directo, delante de todos.",
 "entries": [f"Boleto {i:03d}" for i in range(1, 9)],
 "variants": [{"label": "Boletos 1–50", "entries": [f"Boleto {i:03d}" for i in range(1, 51)]}, {"label": "Boletos 1–100", "entries": [f"Boleto {i:03d}" for i in range(1, 101)]}, {"label": "Premios", "entries": ["Primer premio", "Segundo premio", "Tercer premio"]}],
 "howTo": ["Pega los nombres de los participantes o los números de boleto, uno por línea.", "Deja activado «Quitar al ganador» para que nadie gane dos veces.", "Gira una vez por cada premio, en el orden que anunciaste."],
 "sections": [
  {"h2": "Cómo funciona la ruleta de sorteo", "body":
   "Cada línea es una participación y una parte igual de la ruleta. Gira para sacar un ganador; con **Quitar al ganador** activado, esa participación sale de la ruleta y no puede volver a ganar. La lista de **Resultados** guarda a todos los ganadores en orden.\n\n" + NOTA_AZAR},
  {"h2": "Un sorteo justo en seis pasos", "body":
   "1. **Escribe las bases antes:** quién puede participar, cuántas participaciones por persona, fecha de cierre, premios y cómo se contactará a los ganadores.\n"
   "2. **Cierra las participaciones** a la hora anunciada y arma la lista. Quita duplicados y a quien no cumpla las bases.\n"
   "3. **Di los números en voz alta:** «Tenemos 214 participaciones válidas y 3 premios».\n"
   "4. **Anuncia el orden de los premios** antes del primer giro.\n"
   "5. **Gira en directo**, en pantalla o en un video grabado.\n"
   "6. **Guarda un registro:** captura de la lista y de los Resultados hasta entregar los premios."},
  {"h2": "¿Nombres o números de boleto?", "body":
   "- **Una participación por persona:** pega los nombres.\n"
   "- **Varias participaciones:** pega **números de boleto**, no nombres. Quien tenga cinco boletos tendrá cinco partes de la ruleta, justo lo que le corresponde."},
  {"h2": "¿Qué probabilidad tengo de ganar?", "body":
   "| Participaciones | Tus boletos | Premios | Tu probabilidad |\n|---|---|---|---|\n"
   "| 100 | 1 | 1 | 1,0 % |\n| 100 | 3 | 1 | 3,0 % |\n| 100 | 3 | 3 | 8,8 % |\n| 100 | 10 | 3 | 27,3 % |\n| 250 | 5 | 1 | 2,0 % |\n| 500 | 20 | 5 | 18,5 % |"},
  {"h2": "Sorteos en Instagram, TikTok y otras redes", "body":
   "1. Copia los usuarios que participaron (comentarios o la herramienta que uses).\n"
   "2. Quita duplicados, la cuenta organizadora y a quien no cumpla las bases.\n"
   "3. Pega los usuarios aquí, uno por línea, y gira grabando la pantalla.\n"
   "4. Comprueba que el ganador cumple las bases antes de anunciarlo.\n\n"
   "Cada red social tiene sus propias reglas para promociones. Léelas antes de publicar."},
  {"h2": "¿Es legal un sorteo al azar?", "body":
   "Una ruleta justa hace que la **elección** sea justa, pero no hace que el **sorteo** sea legal por sí misma. Las normas sobre sorteos, rifas y concursos con premio cambian mucho según el país, y en algunos casos exigen permisos o una forma gratuita de participar. Esto es información general, no asesoría legal: revisa las normas de tu país antes de lanzar un sorteo con premios de valor."}
 ],
 "faq": [
  {"q": "¿Cuántos participantes admite la ruleta?", "a": "Cientos funcionan bien. El texto se hace más pequeño, pero el sorteo sigue siendo al azar."},
  {"q": "¿Cómo saco varios ganadores?", "a": "Deja activado «Quitar al ganador» y gira una vez por premio."},
  {"q": "¿Pongo nombres o números?", "a": "Nombres si cada persona tiene una participación; números de boleto si alguien puede tener varias."},
  {"q": "¿Cómo demuestro que el sorteo fue limpio?", "a": "Gira en directo o graba la pantalla, y guarda una captura de la lista y de los Resultados."},
  {"q": "¿Usar una ruleta hace legal mi sorteo?", "a": "No. Hace justa la elección, pero las normas dependen de tu país y de la red social. Revísalas antes."}
 ],
 "related": ["es/ruleta-de-nombres", "es", "es/ruleta-de-decisiones", "es/ruleta-si-o-no"],
 "sources": [S_MDN],
},
# ------------------------------------------------------------------ DECISIONES
{
 "slug": "es/ruleta-de-decisiones", "en": "decision-wheel", "key": "es_decide", "nav": "Decisiones",
 "title": "Ruleta de decisiones – Gira para decidir entre opciones | Wheelova",
 "description": "¿No sabes qué elegir? Pon tus opciones en la ruleta de decisiones y gira. Gratis para comida, planes, películas y desempates. Sin registro.",
 "h1": "Ruleta de decisiones", "subhead": "Pon tus opciones en la ruleta y deja que ella decida.",
 "entries": ["Opción 1", "Opción 2", "Opción 3", "Opción 4"],
 "variants": [{"label": "¿Qué comemos?", "entries": ["Pizza", "Tacos", "Hamburguesa", "Sushi", "Pasta", "Empanadas", "Ensalada", "Pollo asado"]}, {"label": "Género de película", "entries": ["Comedia", "Acción", "Drama", "Terror", "Ciencia ficción", "Romance", "Animación", "Documental"]}, {"label": "Plan de fin de semana", "entries": ["Quedarnos en casa", "Salir a comer", "Ir de excursión", "Visitar amigos", "Ir de compras", "Noche de películas"]}, {"label": "¿Quién paga?", "entries": ["Yo", "Tú", "A medias"]}],
 "howTo": ["Cambia las opciones de ejemplo por las tuyas, una por línea.", "Gira.", "¿No te convence el resultado? Eso te dice qué opción preferías de verdad."],
 "sections": [
  {"h2": "Cómo funciona la ruleta de decisiones", "body":
   "Escribe tus opciones —restaurantes, planes, películas— y gira. Cada opción es una parte igual, así que todas tienen la misma probabilidad.\n\n" + NOTA_AZAR},
  {"h2": "¿Ayuda de verdad dejar que el azar decida?", "body":
   "Hay datos interesantes. En un estudio de 2016, el economista Steven Levitt invitó a personas indecisas a lanzar una moneda virtual en su web: cara significaba «haz el cambio». Se registraron más de 20 000 lanzamientos y se encuestó a los participantes a los dos y seis meses. Quienes sacaron cara tuvieron un **25 % más de probabilidad** de hacer el cambio, y quienes cambiaron —de trabajo, de hábito, de relación— dijeron sentirse más felices seis meses después.\n\n"
   "El estudio tiene límites: los participantes eran voluntarios y la felicidad era autodeclarada. Aun así, sugiere que cuando de verdad dudamos, un empujón al azar ayuda a actuar."},
  {"h2": "Cuándo usarla y cuándo no", "body":
   "| Sí conviene | No conviene |\n|---|---|\n"
   "| Todas las opciones te parecen bien | Una opción es claramente mejor |\n"
   "| Llevas más tiempo decidiendo del que merece | Afecta a la salud, la seguridad, el dinero o la ley |\n"
   "| Un grupo no se pone de acuerdo | Alguien saldría perjudicado |"},
  {"h2": "Cinco trucos para decidir mejor", "body":
   "1. **Pon solo opciones que aceptarías.**\n"
   "2. **Da más peso a tu favorita** escribiéndola dos veces.\n"
   "3. **Usa la prueba de la decepción:** si al ver el resultado quieres volver a girar, ya sabes qué preferías.\n"
   "4. **Pónganse de acuerdo antes de girar** cuando decidan en grupo.\n"
   "5. **Elimina hasta quedarte con dos:** activa «Quitar al ganador» y gira para descartar."},
  {"h2": "Otras ruletas", "body":
   "Para una sola pregunta, la [ruleta sí o no](/es/ruleta-si-o-no) es más rápida. Para elegir personas, usa la [ruleta de nombres](/es/ruleta-de-nombres)."}
 ],
 "faq": [
  {"q": "¿Cómo me ayuda la ruleta a decidir?", "a": "Desempata entre opciones que te parecen bien, ahorra tiempo, y tu reacción al resultado suele mostrar qué querías de verdad."},
  {"q": "¿Puedo hacer que una opción salga más?", "a": "Sí. Escríbela más de una vez: cada copia es otra parte igual."},
  {"q": "¿Hay pruebas de que decidir al azar ayude?", "a": "Un estudio de Steven Levitt (2016) encontró que quienes hicieron un cambio tras lanzar una moneda se sentían más felices seis meses después. Usó voluntarios y felicidad autodeclarada, así que tómalo como una pista."},
  {"q": "¿Cuántas opciones puedo poner?", "a": "Las que quieras, aunque entre 3 y 12 es lo más cómodo."},
  {"q": "¿Es justa para decidir en grupo?", "a": "Sí, si todos aceptan la lista y el resultado antes de girar."}
 ],
 "related": ["es/ruleta-si-o-no", "es", "es/ruleta-de-nombres", "es/ruleta-de-sorteo"],
 "sources": [S_NBER, S_MDN],
},
# ------------------------------------------------------------------ COLORES
{
 "slug": "es/ruleta-de-colores", "updated": "2026-11-08", "en": "color-wheel", "key": "es_colors", "nav": "Ruleta de colores",
 "title": "Ruleta de colores – Rueda de colores aleatoria con código HEX | Wheelova",
 "description": "Gira la ruleta de colores y obtén un color al azar con su código HEX. Arcoíris, colores básicos, primarios o pastel, o tu propia lista. Gratis y sin registro.",
 "h1": "Ruleta de colores", "subhead": "Gira la rueda de colores y obtén un color al azar, con su código HEX.",
 "mode": "color",
 "colorMap": {"rojo": "#E53935", "naranja": "#FB8C00", "amarillo": "#FDD835", "verde": "#43A047", "azul": "#1E88E5", "añil": "#3949AB", "índigo": "#3949AB", "violeta": "#8E24AA", "morado": "#7B1FA2", "rosa": "#EC407A", "marrón": "#6D4C41", "café": "#6D4C41", "negro": "#212121", "blanco": "#FAFAFA", "gris": "#9E9E9E", "celeste": "#87CEEB", "cian": "#00ACC1", "turquesa": "#26C6DA", "verde azulado": "#00897B", "lima": "#C0CA33", "dorado": "#D4AF37", "plateado": "#BDBDBD", "azul marino": "#1A237E", "granate": "#800000", "beige": "#D7C4A3", "magenta": "#D81B60", "oliva": "#808000", "melocotón": "#FFB38A", "durazno": "#FFB38A", "lavanda": "#B39DDB", "menta": "#98E2C6", "coral": "#FF7F6B"},
 "entries": ["Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil", "Violeta"],
 "variants": [{"label": "Arcoíris (7)", "entries": ["Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Añil", "Violeta"]},
   {"label": "Colores básicos (12)", "entries": ["Rojo", "Naranja", "Amarillo", "Verde", "Azul", "Morado", "Rosa", "Marrón", "Negro", "Blanco", "Gris", "Turquesa"]},
   {"label": "Primarios (3)", "entries": ["Rojo", "Amarillo", "Azul"]},
   {"label": "Pastel", "entries": ["Melocotón", "Lavanda", "Menta", "Celeste", "Coral", "Beige"]}],
 "resultLabel": "TU COLOR", "popLabel": "TU COLOR ES",
 "howTo": ["Elige un conjunto de colores o escribe nombres de colores, uno por línea.", "Pulsa GIRAR.", "Mira el nombre del color, la muestra y su código HEX en la ventana."],
 "sections": [
  {"h2": "Cómo funciona la ruleta de colores", "body":
   "Cada color de la lista ocupa una parte igual de la rueda y se pinta con su propio color. Al girar, la ruleta se detiene en uno al azar y te muestra el nombre, una muestra y el **código HEX**, el código de seis caracteres que usan programas como Canva, Figma, PowerPoint o CSS.\n\n" + NOTA_AZAR},
  {"h2": "Qué colores reconoce y con qué códigos", "body":
   "La ruleta pinta cada parte cuando el nombre coincide con un color conocido, sin importar mayúsculas:\n\n"
   "| Color | HEX | Color | HEX |\n|---|---|---|---|\n"
   "| Rojo | #E53935 | Morado | #7B1FA2 |\n| Naranja | #FB8C00 | Rosa | #EC407A |\n| Amarillo | #FDD835 | Marrón (o café) | #6D4C41 |\n| Verde | #43A047 | Negro | #212121 |\n| Azul | #1E88E5 | Blanco | #FAFAFA |\n| Añil (o índigo) | #3949AB | Gris | #9E9E9E |\n| Violeta | #8E24AA | Turquesa | #26C6DA |\n\n"
   "También reconoce celeste, cian, verde azulado, lima, dorado, plateado, azul marino, granate, beige, magenta, oliva, melocotón (o durazno), lavanda, menta y coral. Si escribes un color que no está en la lista, la parte usa un color normal de la ruleta y la ventana muestra solo el nombre."},
  {"h2": "¿Qué es un código HEX?", "body":
   "Un código HEX describe un color con tres pares de dígitos hexadecimales: rojo, verde y azul. #FF0000 es rojo puro, #00FF00 verde puro y #0000FF azul puro. Copia el código de la ventana y pégalo en tu programa de diseño para obtener exactamente el mismo tono."},
  {"h2": "Ideas para usar un color al azar", "body":
   "- **Clase de arte:** cada alumno gira y dibuja algo de ese color, o mezcla pinturas hasta conseguirlo.\n"
   "- **Juegos para niños:** «busca algo de este color en la habitación» es un juego rápido para aprender los colores.\n"
   "- **Retos creativos:** diseña un logo o una ilustración usando solo el color que salga.\n"
   "- **Equipos y fiestas:** asigna un color a cada equipo o un código de vestimenta."},
  {"h2": "¿Es una rueda cromática de teoría del color?", "body":
   "No. Una rueda cromática de teoría del color organiza los colores para explicar combinaciones como complementarios o análogos. Esta ruleta sirve para **elegir un color al azar**. Si buscas teoría del color, consulta un libro de arte o diseño; si quieres que el azar elija por ti, estás en el lugar correcto."}
 ],
 "faq": [
  {"q": "¿Cómo obtengo un color al azar?", "a": "Elige un conjunto (arcoíris, básicos, primarios o pastel) o escribe tus colores, y pulsa GIRAR. La ventana muestra el nombre, la muestra y el código HEX."},
  {"q": "¿Puedo usar mis propios colores?", "a": "Sí. Escribe los nombres, uno por línea. Los que la ruleta reconoce se pintan con su color; los demás usan un color normal de la ruleta."},
  {"q": "¿Todos los colores tienen la misma probabilidad?", "a": "Sí. Cada color es una parte igual. Si escribes un color dos veces, tendrá el doble de probabilidad."},
  {"q": "¿Por qué no salen los colores que escribo en inglés?", "a": "Esta página reconoce nombres en español. Para nombres en inglés, usa la versión en inglés de la ruleta de colores."},
  {"q": "¿Es gratis?", "a": "Sí, sin registro y sin instalar nada."}
 ],
 "related": ["es", "es/ruleta-de-decisiones", "es/ruleta-de-nombres", "es/ruleta-de-numeros"],
 "sources": [S_MDN],
},
# ------------------------------------------------------------------ NUMEROS
{
 "slug": "es/ruleta-de-numeros", "updated": "2026-11-08", "en": "number-wheel", "key": "es_numbers", "nav": "Ruleta de números", "numberRange": True,
 "title": "Ruleta de números aleatorios – Del 1 al 100 o el rango que quieras | Wheelova",
 "description": "Ruleta de números aleatorios gratis: elige un rango (1–10, 1–100 o el que quieras), gira y obtén un número al azar. Ideal para sorteos, bingo y clase.",
 "h1": "Ruleta de números", "subhead": "Elige un rango, gira y obtén un número al azar.",
 "entries": [str(i) for i in range(1, 11)],
 "variants": [{"label": "1–10", "entries": [str(i) for i in range(1, 11)]}, {"label": "1–20", "entries": [str(i) for i in range(1, 21)]}, {"label": "1–50", "entries": [str(i) for i in range(1, 51)]}, {"label": "1–100", "entries": [str(i) for i in range(1, 101)]}],
 "resultLabel": "TU NÚMERO", "popLabel": "EL NÚMERO ES",
 "howTo": ["Elige un rango rápido o escribe «Desde» y «Hasta» y pulsa «Crear ruleta».", "Gira la ruleta.", "Activa «Quitar al ganador» si no quieres que un número se repita."],
 "sections": [
  {"h2": "Cómo funciona la ruleta de números", "body":
   "Cada número del rango es una parte igual de la ruleta. Al girar, se detiene en uno al azar. Es la versión visual de un generador de números aleatorios: mejor cuando la gente está mirando, como en un sorteo, un bingo o un juego en clase.\n\n" + NOTA_AZAR},
  {"h2": "Probabilidades y repeticiones", "body":
   "Cada número tiene una probabilidad de **1 ÷ cantidad de números**: un 10 % en 1–10 y un 1 % en 1–100.\n\n"
   "| Rango | Probabilidad por giro | Probabilidad de que un número salga al menos una vez en 10 giros (con repeticiones) |\n|---|---|---|\n"
   "| 1–6 | 16,7 % | 83,8 % |\n| 1–10 | 10 % | 65,1 % |\n| 1–20 | 5 % | 40,1 % |\n| 1–50 | 2 % | 18,3 % |\n| 1–100 | 1 % | 9,6 % |\n\n"
   "- **Sin «Quitar al ganador»:** los números pueden repetirse, como al lanzar un dado.\n"
   "- **Con «Quitar al ganador»:** cada número sale una sola vez, como sacar papeletas de una bolsa. Es lo correcto para sorteos y bingo."},
  {"h2": "Ideas para usarla", "body":
   "- **Sorteos con papeletas numeradas:** crea la ruleta con el rango de tus papeletas y gira en directo.\n"
   "- **Bingo:** del 1 al 75 o del 1 al 90, con «Quitar al ganador» activado.\n"
   "- **Clase de matemáticas:** gira dos números y multiplícalos, o usa el número como pregunta del examen.\n"
   "- **Juegos:** sustituye un dado perdido con 1–6, o elige quién empieza."},
  {"h2": "Tus propias listas de números", "body":
   "La caja de opciones acepta cualquier número, uno por línea: solo pares, negativos o una lista de asientos. Con «Desde» y «Hasta» puedes crear hasta 500 números por ruleta."}
 ],
 "faq": [
  {"q": "¿Cómo saco un número al azar del 1 al 100?", "a": "Pulsa el botón 1–100 y gira. Cada número tiene un 1 % de probabilidad."},
  {"q": "¿Puedo evitar que se repitan los números?", "a": "Sí. Activa «Quitar al ganador después de cada giro»."},
  {"q": "¿Cuántos números caben?", "a": "Hasta 500 con «Desde» y «Hasta». Más de 100 se ven pequeños; para muchos números, un generador en lista es más cómodo."},
  {"q": "¿Sirve para un sorteo?", "a": "Sí, para sorteos informales. Los sorteos oficiales pueden tener normas propias según el país."}
 ],
 "related": ["es/ruleta-de-sorteo", "es", "es/ruleta-de-colores", "es/ruleta-si-o-no"],
 "sources": [S_MDN],
},
]

# ---- Spanish homepage rewrite (Nov 9 2026): keyword map from competitor export; SEO/AEO/E-E-A-T.
ES_HOME = {
 "updated": "2026-11-09",
 "title": "Ruleta aleatoria online – Ruleta personalizada gratis | Wheelova",
 "description": "Ruleta aleatoria online y gratis: escribe nombres u opciones, gira y obtén un resultado justo. Ruleta personalizada para sorteos, clase y decisiones. Sin registro.",
 "h1": "Ruleta aleatoria online",
 "subhead": "Escribe tus opciones, gira la ruleta y deja que el azar decida. Gratis, sin registro y probada con 1 millón de giros.",
 "howTo": ["Escribe o pega tus opciones, una por línea (o pulsa Importar para cargar un CSV).", "Pulsa GIRAR o la barra espaciadora.", "Lee el resultado en la ventana. Activa «Quitar al ganador» si no quieres repeticiones."],
 "sections": [
  {"h2": "¿Qué es una ruleta aleatoria?", "body":
   "**Una ruleta aleatoria es una rueda virtual dividida en partes iguales, una por cada opción que escribes, que se detiene en una de ellas al azar.** Sirve para elegir un nombre, un ganador, una respuesta de sí o no o cualquier opción sin que nadie influya en el resultado. Como todos ven girar la rueda, la elección se percibe como justa.\n\n"
   "También se la conoce como **ruleta virtual**, **ruleta online**, **ruleta digital** o **rueda aleatoria**. En Wheelova la ruleta es **personalizable**: tú decides las opciones, los colores, la velocidad y el mensaje del ganador."},
  {"h2": "Cómo hacer una ruleta personalizada", "body":
   "1. **Escribe tus opciones,** una por línea: nombres, premios, números o tareas. Puedes pegar una columna de Excel o Google Sheets, o pulsar **Importar** para cargar un archivo CSV.\n"
   "2. **Ajusta la ruleta** en **Ajustes**: colores (pastel, océano, atardecer, bosque, escala de grises, apta para daltónicos o tus propios colores), velocidad de giro y texto de la ventana del ganador.\n"
   "3. **Gira** con el botón GIRAR o la barra espaciadora. Pulsa **F** para pantalla completa en un proyector.\n"
   "4. **Guarda o comparte:** guarda la lista con un nombre en **Mis ruletas guardadas**, copia un enlace para compartirla o inserta la ruleta en tu web o en OBS.\n\n"
   "No necesitas cuenta ni instalar nada: funciona en el navegador del móvil, la tableta o el ordenador."},
  {"h2": "¿La ruleta es realmente aleatoria? Lo comprobamos con 1.000.000 de giros", "body":
   "Sí. Cada giro usa la función `crypto.getRandomValues()` de tu navegador. Según MDN Web Docs, los navegadores la implementan como un **generador pseudoaleatorio criptográficamente seguro** alimentado con entropía del sistema, el mismo tipo de fuente que se usa en funciones de seguridad. El número aleatorio decide cuánto gira la rueda, y gana la parte que queda bajo el indicador.\n\n"
   "Para comprobarlo, ejecutamos el código real de la ruleta **1.000.000 de veces** en ruletas de 2, 6 y 10 opciones:\n\n"
   "| Ruleta | Giros | Esperado por opción | Resultado real | Prueba chi-cuadrado |\n|---|---|---|---|---|\n"
   "| 2 opciones (sí o no) | 1.000.000 | 500.000 | 499.629 – 500.371 | p = 0,458 · sin sesgo |\n"
   "| 6 opciones (como un dado) | 1.000.000 | 166.667 | 165.897 – 167.442 | p = 0,107 · sin sesgo |\n"
   "| 10 opciones (lista de clase) | 1.000.000 | 100.000 | 99.417 – 100.657 | p = 0,066 · sin sesgo |\n\n"
   "En las tres ruletas, ninguna opción se alejó más de un 0,7 % de lo esperado, y la prueba chi-cuadrado no encontró ningún sesgo (un valor p mayor que 0,05 significa que no hay evidencia de sesgo). Tampoco encontramos relación entre un giro y el siguiente. El método, los datos brutos y el script están en el [estudio completo](/is-the-wheel-random) (en inglés), para que cualquiera pueda repetirlo."},
  {"h2": "Probabilidades de la ruleta", "body":
   "Todas las partes tienen el mismo tamaño, así que la probabilidad de cada opción es **1 ÷ número de opciones**:\n\n"
   "| Opciones | Probabilidad de cada una por giro | Probabilidad de que una opción concreta salga al menos una vez en 10 giros |\n|---|---|---|\n"
   "| 2 | 50 % | 99,9 % |\n| 3 | 33,3 % | 98,3 % |\n| 4 | 25 % | 94,4 % |\n| 6 | 16,7 % | 83,8 % |\n| 10 | 10 % | 65,1 % |\n| 20 | 5 % | 40,1 % |\n| 50 | 2 % | 18,3 % |\n\n"
   "La última columna se calcula como 1 − (1 − 1/n)¹⁰ y supone que los ganadores no se quitan de la ruleta. Puedes usar estas tablas en tus clases o artículos con un enlace a esta página."},
  {"h2": "¿Por qué sale la misma opción varias veces seguidas?", "body":
   "Porque cada giro es **independiente**: la ruleta no recuerda el resultado anterior. Con 2 opciones, la misma sale dos veces seguidas la mitad de las veces. En nuestro millón de giros de una ruleta de sí o no ocurrió esto:\n\n"
   "| Racha del mismo resultado | Veces que pasó | Esperado por probabilidad |\n|---|---|---|\n"
   "| 5 o más seguidas | 31.199 | unas 31.250 |\n| 10 o más seguidas | 944 | unas 977 |\n| 15 o más seguidas | 27 | unas 31 |\n| Racha más larga | 19 | normalmente 19–20 en un millón de giros |\n\n"
   "Creer que «ya le toca» a otra opción es la **falacia del jugador**. Si quieres que cada opción salga una sola vez, activa **Quitar al ganador después de cada giro**."},
  {"h2": "¿Se puede trucar la ruleta?", "body":
   "Wheelova no tiene ningún ajuste oculto para elegir un ganador por adelantado, y el resultado nunca depende de la posición ni del nombre de la opción. Lo que sí se puede hacer, **a la vista de todos**, es dar más peso a una opción escribiéndola varias veces: con «Sí, Sí, No», el Sí tiene 2 de 3 probabilidades (un 67 %).\n\n"
   "Por eso, en un sorteo público: muestra la lista completa antes de girar, elimina los duplicados que no estén permitidos y gira en directo o graba la pantalla. Quien controla la lista controla las probabilidades, así que la lista debe ser visible."},
  {"h2": "Para qué sirve una ruleta aleatoria", "body":
   "| Uso | Ruleta recomendada | Consejo |\n|---|---|---|\n"
   "| Elegir alumnos en clase | [Ruleta de nombres](/es/ruleta-de-nombres) | Activa «Quitar al ganador» para que todos tengan su turno |\n"
   "| Sorteos y concursos | [Ruleta de sorteo](/es/ruleta-de-sorteo) | Muestra la lista y exporta los ganadores en CSV |\n"
   "| Preguntas de sí o no | [Ruleta sí o no](/es/ruleta-si-o-no) | Añade «Tal vez» o haz al mejor de tres |\n"
   "| Decidir entre opciones | [Ruleta de decisiones](/es/ruleta-de-decisiones) | Pon solo opciones que aceptarías |\n"
   "| Números al azar, bingo | [Ruleta de números](/es/ruleta-de-numeros) | Elige el rango con «Desde» y «Hasta» |\n"
   "| Un color al azar | [Ruleta de colores](/es/ruleta-de-colores) | Muestra el código HEX de cada color |"},
  {"h2": "Una alternativa a la ruleta de Google", "body":
   "Mucha gente busca la «ruleta de Google». Wheelova es una herramienta independiente, sin relación con Google, que añade lo que una búsqueda rápida no tiene: **tus propias opciones**, quitar ganadores, historial de resultados con exportación a CSV, listas guardadas, colores personalizados, pantalla completa para el proyector, enlace para compartir y código para insertar la ruleta en tu web o en un directo de OBS."},
  {"h2": "Privacidad: tus opciones se quedan en tu dispositivo", "body":
   "Lo que escribes se guarda en tu navegador, no en nuestros servidores, y la ruleta está oculta para nuestra herramienta de estadísticas. Si creas un enlace para compartir, las opciones viajan dentro del enlace (codificadas, no cifradas), así que cualquiera que lo tenga puede leerlas: no compartas listas con datos privados."},
  {"h2": "Quién está detrás de Wheelova", "body":
   "Wheelova es un sitio independiente de herramientas aleatorias gratuitas. Su contenido lo escribe y revisa Sajid Ali, editor de Wheelova, y las afirmaciones sobre el azar se basan en la documentación de MDN y en nuestro propio estudio publicado con datos abiertos. Si encuentras un error, escríbenos a [support@wheelova.com](mailto:support@wheelova.com)."}
 ],
 "faq": [
  {"q": "¿La ruleta aleatoria es realmente al azar?", "a": "Sí. Usa el generador criptográficamente seguro del navegador (crypto.getRandomValues), y en una prueba de 1.000.000 de giros por ruleta no mostró ningún sesgo."},
  {"q": "¿Cómo hago una ruleta personalizada?", "a": "Escribe tus opciones, una por línea, o importa un CSV. En Ajustes eliges colores, velocidad y el mensaje del ganador. Guárdala con un nombre o compártela con un enlace."},
  {"q": "¿Es gratis? ¿Tengo que registrarme?", "a": "Es gratis y no necesitas cuenta ni descargar ninguna aplicación."},
  {"q": "¿Cómo evito que salga dos veces la misma opción?", "a": "Activa «Quitar al ganador después de cada giro» o pulsa «Quitar de la ruleta» en la ventana del resultado."},
  {"q": "¿Se puede trucar la ruleta?", "a": "No hay ningún ajuste oculto. Solo se puede cambiar la probabilidad escribiendo una opción varias veces, algo que todos ven en la lista."},
  {"q": "¿Cuántas opciones puedo poner?", "a": "No hay un límite fijo. Hasta unas 50 se leen bien en un proyector; los enlaces para compartir admiten hasta 1.000."},
  {"q": "¿Puedo usarla para un sorteo en Instagram o en directo?", "a": "Sí. Pega o importa la lista de participantes y gira en directo. Las normas de los sorteos cambian según el país y la red social, así que revisa las que te apliquen."},
  {"q": "¿Funciona en el móvil?", "a": "Sí, en cualquier navegador moderno. En iPhone puedes añadirla a la pantalla de inicio desde Compartir → Añadir a pantalla de inicio."}
 ],
}
ES[0].update(ES_HOME)
