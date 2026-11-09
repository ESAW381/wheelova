# French pages (/fr). Standard French for France, Belgium, Switzerland and Canada.
from content_v2 import S_MDN

NOTE_HASARD = ("Wheelova utilise la fonction `crypto.getRandomValues()` de votre navigateur. Selon MDN, les navigateurs l'implémentent comme un "
               "générateur pseudo-aléatoire cryptographiquement sûr, alimenté par l'entropie du système : le même type de source que celui utilisé "
               "pour les fonctions de sécurité. En pratique, il est imprévisible, même s'il ne s'agit pas d'un appareil physique de « vrai hasard ».")

PALETTE = ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]
PRENOMS = ["Emma", "Lucas", "Chloé", "Hugo", "Léa", "Louis", "Manon", "Gabriel", "Inès", "Jules"]

JS = {  # strings used by app.js
 "add2": "Ajoutez au moins deux options", "spinning": "La roue tourne…", "winner": "GAGNANT", "pop": "NOUS AVONS UN GAGNANT !",
 "empty": "Ajoutez des options", "add2share": "Ajoutez au moins deux options pour partager", "copied": "Copié",
 "copy": "Copier", "copy_embed": "Copier le code", "share_title": "PARTAGER CETTE ROUE", "embed_title": "INTÉGRER CETTE ROUE",
 "long": "La liste est longue, donc le lien aussi ({n} caractères). Il fonctionne, mais certaines messageries peuvent le couper.",
 "iframe_title": "Faites tourner la roue – Wheelova", "credit_pre": "Roue par",
 "fs": "Plein écran", "exitfs": "Quitter le plein écran", "openmenu": "Ouvrir le menu", "closemenu": "Fermer le menu",
 "todark": "Passer en mode sombre", "tolight": "Passer en mode clair",
 "cleared": "Liste effacée.", "removedw": "« {w} » a été retiré de la roue.", "imported": "{n} entrées importées.", "impcut": "Seules les 2 000 premières ont été conservées.", "impempty": "Aucune entrée trouvée dans ce fichier.", "impbig": "Ce fichier est trop volumineux (5 Mo maximum).", "impxls": "Enregistrez d'abord la feuille au format CSV, ou copiez la colonne et collez-la.", "col": "Colonne",
 "nrange": "Indiquez une plage où « À » est plus grand que « De ».", "nmax": "500 nombres maximum par roue.",
 "replaced": "Liste remplacée.", "kept": "Roue partagée enregistrée comme votre liste.",
 "csv_spin": "Tour", "csv_winner": "Gagnant", "csv_time": "Heure", "load": "Ouvrir", "loaded": "Ouverte", "del": "Supprimer", "deleted": "Supprimée",
 "needname": "Donnez d'abord un nom à cette roue.", "updated": "Mise à jour", "saved": "Enregistrée", "full": "Vous pouvez enregistrer jusqu'à 50 roues. Supprimez-en une d'abord.",
}

NAV_FR = [("fr", "Roue aléatoire"), ("", "English"), ("es", "Español")]

FR = [
{
 "slug": "fr", "updated": "2026-11-08", "en": "", "key": "fr_home", "nav": "Roue aléatoire", "palette": PALETTE,
 "title": "Roue aléatoire – Roue du hasard en ligne gratuite | Wheelova",
 "description": "Roue aléatoire en ligne et gratuite : écrivez des prénoms ou des choix, faites tourner la roue du hasard et obtenez un résultat équitable. Sans inscription.",
 "h1": "Roue aléatoire", "subhead": "Écrivez vos choix, faites tourner la roue et laissez le hasard décider.",
 "entries": PRENOMS,
 "variants": [{"label": "10 prénoms", "entries": PRENOMS}, {"label": "Oui / Non", "entries": ["Oui", "Non"]}, {"label": "Nombres 1–10", "entries": [str(i) for i in range(1, 11)]},
   {"label": "On mange quoi ?", "entries": ["Pizza", "Crêpes", "Burger", "Sushi", "Pâtes", "Raclette", "Salade", "Couscous"]}],
 "howTo": ["Écrivez ou collez vos choix, un par ligne.", "Appuyez sur TOURNER (ou sur la barre d'espace).", "Lisez le résultat dans la fenêtre. Activez « Retirer le gagnant » pour éviter les répétitions."],
 "sections": [
  {"h2": "Qu'est-ce qu'une roue aléatoire ?", "body":
   "Une roue aléatoire, ou roue du hasard, est une roue divisée en parts égales, une pour chaque choix que vous écrivez. Quand elle tourne, elle s'arrête au hasard sur l'une d'elles. Comme tout le monde voit la roue tourner, le résultat paraît juste : personne ne peut dire que le choix était arrangé.\n\n" + NOTE_HASARD},
  {"h2": "À quoi sert-elle ?", "body":
   "**En classe :** choisir qui répond, l'ordre des exposés ou les groupes. Activez « Retirer le gagnant » pour que chaque élève passe une fois.\n\n"
   "**Tirages au sort et concours :** collez la liste des participants (ou importez un fichier CSV) et faites tourner la roue en direct. Exportez ensuite l'ordre des gagnants en CSV pour garder une trace.\n\n"
   "**Décisions du quotidien :** que manger ce soir, quel film regarder, qui fait la vaisselle.\n\n"
   "**Jeux et soirées :** défis, gages, tours de parole ou petits lots."},
  {"h2": "Probabilités : la roue est-elle équitable ?", "body":
   "Toutes les parts ont la même taille, donc chaque choix a une probabilité de **1 ÷ nombre de choix** :\n\n"
   "| Choix | Probabilité de chacun |\n|---|---|\n| 2 | 50 % |\n| 4 | 25 % |\n| 6 | 16,7 % |\n| 10 | 10 % |\n| 20 | 5 % |\n\n"
   "Pour qu'un choix sorte plus souvent, écrivez-le deux fois : avec « Oui, Oui, Non », le Oui a 2 chances sur 3 (environ 67 %). Qu'un même choix sorte deux fois de suite est normal, car chaque tour est indépendant du précédent. Nous avons testé le code de la roue sur 1 000 000 de tours par roue : les résultats et les données brutes sont publiés dans notre [étude d'équité](/is-the-wheel-random) (en anglais)."},
  {"h2": "Personnaliser votre roue", "body":
   "- **Couleurs :** dans **Réglages**, choisissez une palette (pastel, océan, coucher de soleil, forêt, niveaux de gris, adaptée aux daltoniens) ou vos propres couleurs.\n"
   "- **Vitesse et message :** réglez la vitesse de rotation et le titre de la fenêtre du gagnant.\n"
   "- **Listes enregistrées :** gardez une liste par classe ou par groupe sous **Mes roues enregistrées**.\n"
   "- **Partager et intégrer :** envoyez votre roue par lien, ou intégrez-la à votre site ou à OBS pour un direct."},
  {"h2": "Pas le jeu télévisé", "body":
   "Beaucoup de gens cherchent « roue de la chance » ou « roue de la fortune ». Wheelova est un outil indépendant, sans lien avec ces jeux télévisés : c'est une roue que vous remplissez vous-même, pour tirer au sort, décider ou jouer."},
  {"h2": "Vos choix restent privés", "body":
   "Ce que vous écrivez est enregistré dans votre navigateur, sur votre appareil, et n'est pas envoyé à nos serveurs. Si vous créez un lien de partage, les choix voyagent à l'intérieur du lien : toute personne qui l'a peut les lire, alors évitez de partager des listes privées."}
 ],
 "faq": [
  {"q": "La roue aléatoire est-elle vraiment due au hasard ?", "a": "Oui. Elle utilise le générateur cryptographiquement sûr de votre navigateur, et chaque tour est indépendant du précédent."},
  {"q": "Est-ce gratuit ? Faut-il s'inscrire ?", "a": "C'est gratuit et sans compte. Vos choix sont enregistrés dans votre navigateur."},
  {"q": "Comment éviter qu'un même choix sorte deux fois ?", "a": "Activez « Retirer le gagnant après chaque tour », ou appuyez sur « Retirer de la roue » dans la fenêtre du résultat."},
  {"q": "Combien de choix puis-je ajouter ?", "a": "Autant que vous voulez. Le texte rétrécit quand la liste s'allonge ; jusqu'à environ 50 choix restent lisibles sur un projecteur."},
  {"q": "Puis-je l'utiliser pour un tirage au sort ?", "a": "Oui. Faites tourner la roue en direct pour que tout le monde voie le résultat. Les règles des jeux-concours varient selon les pays : vérifiez celles qui s'appliquent à vous."},
  {"q": "Est-ce que ça marche sur mobile ?", "a": "Oui, dans tout navigateur récent, sans rien installer. Vous pouvez aussi l'ajouter à l'écran d'accueil de votre téléphone."}
 ],
 "related": [],
 "sources": [S_MDN],
},
]
