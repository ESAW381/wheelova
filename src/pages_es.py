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
}

NAV_ES = [("es/ruleta-de-nombres", "Ruleta de nombres"), ("es/ruleta-si-o-no", "Sí o no"), ("es/ruleta-de-sorteo", "Sorteos"), ("es/ruleta-de-decisiones", "Decisiones"), ("", "English")]

ES = [
# ------------------------------------------------------------------ HOME
{
 "slug": "es", "en": "", "key": "es_home", "nav": "Ruleta aleatoria", "palette": PALETA,
 "title": "Ruleta aleatoria – Gira la ruleta online gratis | Wheelova",
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
 "title": "Ruleta de sorteo online – Elige ganadores al azar | Wheelova",
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
]
