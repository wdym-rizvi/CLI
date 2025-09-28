# 📂 Configs

This folder stores configuration files for the CLI APP.

## Files

* **`config.json`**
  Stores user-specific data such as the saved username.
  Example:

  ```json
  {
    "name": "UserXYZ"
  }
  ```

* **`music.json`**
  Controls background music preferences.
  Example:

  ```json
  {
    "music_enabled": true
  }
  ```

## Notes

* Both files are created automatically on the first run if they don’t exist.
* You can manually edit them with a text editor, or use the **Settings** option in the CLI APP to update values.
* Deleting either file will reset its settings and prompt the app to re-create it on the next run.
