# ✅ **ROADMAP — Console v2.0 (modulaire, simple, efficace)**

*(Format prêt à copier dans PyCharm)*

---

## 🔹 **[TODO] 1. Cursor Manager (base indispensable)**

**Créer une classe Cursor** pour manipuler proprement le curseur :

* [ ] Ajouter `cursor.hide()` – cacher le curseur
* [ ] Ajouter `cursor.show()` – montrer le curseur
* [ ] Ajouter `cursor.move_up(n=1)`
* [ ] Ajouter `cursor.move_down(n=1)`
* [ ] Ajouter `cursor.move_right(n=1)`
* [ ] Ajouter `cursor.move_left(n=1)`
* [ ] Ajouter `cursor.save()` – sauvegarder la position
* [ ] Ajouter `cursor.restore()` – restaurer position
* [ ] Ajouter `cursor.clear_line()` – effacer ligne entière

**Note :** utilise les séquences ANSI suivantes :

* Haut : `\033[{n}A`
* Bas : `\033[{n}B`
* Droite : `\033[{n}C`
* Gauche : `\033[{n}D`
* Sauver : `\033[s`
* Restor : `\033[u`
* Clear line : `\033[2K`

*(je peux t’expliquer une par une si tu veux)*

---

## 🔹 **[TODO] 2. ProgressBar (outil pratique réutilisable)**

**Créer une classe ProgressBar intégrée à Animation et Packed** :

* [ ] Option `length` (largeur)
* [ ] Option `style` (pack BASIS : on/off/borders)
* [ ] Option `color`
* [ ] Option `percent_style`: numérique, barre seulement ou mix
* [ ] Méthode `update(percent)`
* [ ] Méthode `render(delete=True)`

Fonctionnalités standards :

* [ ] Animation optionnelle (spinner en parallèle)
* [ ] Suppression automatique de la ligne précédente
* [ ] Support script / boucle / async léger

---

## 🔹 **[TODO] 3. Module ANSI (simple, centralisé, pour tout usage futur)**

**Créer un fichier ansi.py** contenant les codes courants :

* [ ] CURSOR_UP = "\033[{n}A"
* [ ] CURSOR_DOWN = "\033[{n}B"
* [ ] CLEAR_LINE = "\033[2K"
* [ ] HIDE_CURSOR = "\033[?25l"
* [ ] SHOW_CURSOR = "\033[?25h"

*But : éviter de dupliquer du code partout.*

---

## 🔹 **[TODO] 4. Amélioration d’Action (console utils)**

Ajouts simples et utiles :

* [ ] `Action.pause(msg="Press ENTER to continue...")`
* [ ] `Action.wait(seconds)` (wrapper sur sleep)
* [ ] `Action.flush()` : `stdout.flush()`
* [ ] `Action.clear_lines(n)` : efface n lignes d’un coup

---

## 🔹 **[TODO] 5. Améliorer color() et styles (sans complexifier)**

Tu as déjà un système de log, donc on garde simple :

* [ ] Ajouter `bold`, `underline` en options
* [ ] Ajouter un argument `auto_reset=True`
* [ ] Ajouter un helper `colored(text, fg=None, bg=None, style=None)`

Styles optionnels (sans casser ton existant) :

* [ ] style.bold("text")
* [ ] style.error("text")
* [ ] style.warn("text")
* [ ] style.ok("text")

---

## 🔹 **[TODO] 6. Spinner (classe simple)**

Une version plus petite que `Animation`, spécialement pour les scripts :

* [ ] Choisir des sets : `|/-\`, `◐◓◑◒`, etc.
* [ ] Méthode `next()` → retourne l’image suivante
* [ ] Méthode `reset()`

---

## 🔹 **[TODO] 7. Timer & Stopwatch (outil script très utile)**

Créer un mini module pour mesurer le temps :

* [ ] Classe `Stopwatch` :

  * start()
  * stop()
  * reset()
  * elapsed() en secondes ou formaté

---

## 🔹 **[TODO] 8. Wrapper "pretty print"**

Pour afficher proprement dans les scripts :

* [ ] `pp.dict(d)` – dictionnaire coloré
* [ ] `pp.list(lst)` – liste stylée
* [ ] `pp.title(text)` – titre encadré avec Pack

Toujours optionnel et utilisable partout.

---

## 🔹 **[TODO] 9. Documentation interne minimale**

* [ ] Exemple d’utilisation pour chaque classe
* [ ] Ajout d’un dossier /examples
* [ ] Ajouter un README clair dans ton projet

---

## 🔹 **[TODO] 10. Système Light de Config Globale**

Optionnel mais puissant :

* [ ] Global config (auto color ON/OFF)
* [ ] Option “safe mode” pour Windows
* [ ] Option “minimal mode” sans animation pour CI

---

## 🔹 **[TODO] 11. Tests rapides (sans frameworks)**

Pour garder ton module fiable :

* [ ] Script test pour vérifier les couleurs
* [ ] Script test pour vérifier les animations
* [ ] Test ProgressBar simple

---

# 🎯 Résultat attendu de cette roadmap

À la fin de ça, tu auras :

✔ un module simple
✔ très modulaire
✔ utilisable dans tous tes scripts
✔ avec des utilities vraiment pratiques
✔ facile à maintenir
✔ avec animations, couleurs, curseur, progress bar
