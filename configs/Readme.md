# ⚙️ Configs Directory

This folder contains configuration files used by **CLI_APP**.
All settings are stored in JSON format so they can be easily edited without modifying the source code.

---

## 📂 Files

### 1. `config.json`

* Stores user-related settings.
* Example:

  ```json
  {
    "name": "Burhan"
  }
  ```
* You can change the `name` value to update your username in the app.

---

### 2. `music.json`

* Stores whether startup music/sounds are enabled.
* Example:

  ```json
  {
    "music_enabled": true
  }
  ```
* Set `"music_enabled": false` to disable music.
* Takes effect **the next time you run the app**.

---

### 3. `music_list.json`

* Defines the list of music files available to the app.
* Example:

  ```json
  {
    "MUSIC_FILES": [
      "music/aura-song.mp3",
      "music/montagem-bandido.mp3",
      "music/ladrao",
      "music/montagem-xonada.mp3",
      "music/nada-nada.mp3",
      "vem-no-piquie.mp3"
    ]
  }
  ```
* Add or remove tracks here to customize the app’s playlist.
* Paths should be relative to the project root (e.g. `"music/filename.mp3"`).

---

## 🛠️ Notes

* All JSON files must be **valid JSON** (use quotes for strings, commas between items, etc.).
* Incorrect formatting will cause the app to fail when reading configs.
* Always restart the app after making changes.
