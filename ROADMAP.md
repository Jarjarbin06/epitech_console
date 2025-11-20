# ✅ **ROADMAP — Console v2.0 (modular, simple, efficient)**

*(Format ready to copy into PyCharm)*

---

## 🔹 **[TODO] 1. Cursor Manager (essential foundation)**

**Create a `Cursor` class** to handle the cursor properly:

* [x] Add `cursor.hide()` – hide the cursor
* [x] Add `cursor.show()` – show the cursor
* [x] Add `cursor.move_up(n=1)`
* [x] Add `cursor.move_down(n=1)`
* [x] Add `cursor.move_right(n=1)`
* [x] Add `cursor.move_left(n=1)`
* [x] Add `cursor.save()` – save position
* [x] Add `cursor.restore()` – restore position
* [x] Add `cursor.clear_line()` – clear entire line

**Note:** use the following ANSI sequences:

* Up: `\033[{n}A`
* Down: `\033[{n}B`
* Right: `\033[{n}C`
* Left: `\033[{n}D`
* Save: `\033[s`
* Restore: `\033[u`
* Clear line: `\033[2K`

---

## 🔹 **[TODO] 2. ProgressBar (reusable handy tool)**

**Create a `ProgressBar` class integrated with `Animation` and `Packed`:**

* [x] Option `length` (width)
* [x] Option `style` (BASIS pack: on/off/borders)
* [x] Option `color`
* [x] Option `percent_style`: numeric, bar only, or mixed
* [x] Method `update(percent)`
* [x] Method `render(delete=True)`

Standard features:

* [x] Optional animation (spinner in parallel)
* [x] Automatically remove previous line
* [ ] Support scripts / loops / lightweight async

---

## 🔹 **[TODO] 3. ANSI Module (simple, centralized, for all future use)**

**Create a file `ansi.py` containing common codes:**

* [x] CURSOR_UP = "\033[{n}A"
* [x] CURSOR_DOWN = "\033[{n}B"
* [x] CLEAR_LINE = "\033[2K"
* [x] HIDE_CURSOR = "\033[?25l"
* [x] SHOW_CURSOR = "\033[?25h"

*Goal: avoid duplicating code everywhere.*

---

## 🔹 **[TODO] 4. Improve Action (console utils)**

Simple and useful additions:

* [ ] `Action.pause(msg="Press ENTER to continue...")`
* [ ] `Action.wait(seconds)` (wrapper around `sleep`)
* [ ] `Action.flush()` : `stdout.flush()`
* [ ] `Action.clear_lines(n)` : clears `n` lines at once

---

## 🔹 **[TODO] 5. Improve color() and styles (keep it simple)**

You already have a logging system, so keep it simple:

* [ ] Add `bold`, `underline` options
* [ ] Add argument `auto_reset=True`
* [ ] Add helper `colored(text, fg=None, bg=None, style=None)`

Optional styles (without breaking existing code):

* [x] style.bold("text")
* [ ] style.error("text")
* [ ] style.warn("text")
* [ ] style.ok("text")

---

## 🔹 **[TODO] 6. Spinner (simple class)**

A smaller version than `Animation`, especially for scripts:

* [x] Choose sets: `|/-\`, `◐◓◑◒`, etc.
* [x] Method `next()` → returns next frame
* [x] Method `reset()`

---

## 🔹 **[TODO] 7. Timer & Stopwatch (very useful for scripts)**

Create a mini module to measure time:

* [x] Class `Stopwatch`:

  * start()
  * stop()
  * reset()
  * elapsed() in seconds or formatted

---

## 🔹 **[TODO] 8. "Pretty Print" Wrapper**

To display neatly in scripts:

* [ ] `pp.dict(d)` – colored dictionary
* [ ] `pp.list(lst)` – styled list
* [ ] `pp.title(text)` – framed title with Pack

Always optional and usable everywhere.

---

## 🔹 **[TODO] 9. Minimal Internal Documentation**

* [ ] Usage example for each class
* [ ] Add an `/examples` folder
* [ ] Add a clear README to your project

---

## 🔹 **[TODO] 10. Lightweight Global Config System**

Optional but powerful:

* [ ] Global config (auto color ON/OFF)
* [ ] “Safe mode” option for Windows
* [ ] “Minimal mode” without animation for CI

---

## 🔹 **[TODO] 11. Quick Tests (without frameworks)**

To keep your module reliable:

* [ ] Test script to check colors
* [ ] Test script to check animations
* [ ] Simple ProgressBar test

---

# 🎯 Expected Outcome of this Roadmap

By the end, you will have:

✔ a simple module  
✔ highly modular  
✔ usable in all your scripts  
✔ with truly handy utilities  
✔ easy to maintain  
✔ with animations, colors, cursor control, and progress bar
