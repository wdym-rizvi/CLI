# CLI APP - Command Line Interface Application

A powerful and interactive command-line toolkit built with Python.
It features utilities for networking, system monitoring, file management, and more — all wrapped in a stylish, animated CLI with sound and music support.

---

## ✨ Features

* **Networking Tools**

  * Public IP lookup
  * Local IP lookup
  * Port scanning
  * DNS Lookup
  * WHOIS Lookup
  * Traceroute
  * SSL Info

* **System Utilities**

  * System Info
  * CPU Usage
  * RAM Info
  * Kill Process
  * Hostname
  * Current Time

* **File & Media**

  * Screenshot
  * Website Screenshot
  * Zip Folder

* **Interactive CLI**

  * Fake boot sequence for fun start-up
  * Gradient ASCII banners
  * Animated loaders & marquee text
  * Sound effects + optional background Phonk music 🎵

---

```
CLI_APP/
│── run.py                  # Main entry point
|── app.py                  # Mian App Logic
|── requirements.txt
|── app.ico                 # Icon for .exe
│── creds/
|   └── credentials.json    # Encrypted Credentials
|   └── fernet.key          # Key For decrypting Credentials 
│── configs/
│   └── config.json           # Stores user data (e.g. name)
│   └── music.json            # Stores music settings
│── music/
│   ├── startup.wav           # Startup sound
│   ├── aura-song.mp3
│   ├── montagem-bandido.mp3
│   ├── montagem-xonada.mp3
│   └── nada-nada.mp3
│── Functions/
│   ├── get_public_ip.py
│   ├── get_local_ip.py
│   ├── system_info.py
│   ├── cpu_usage.py
│   ├── ram_info.py
│   ├── screenshot.py
│   ├── website_screenshot.py
│   ├── hostname.py
│   ├── current_time.py
│   ├── port_scan.py
│   ├── ssl_info.py
│   ├── kill_process.py
│   ├── traceroute.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   └── zip_folder.py
│── UpgradedBuiltins/         # Custom input/output enhancements
│   ├── __init__.py
│   ├── ascii_art.py
│   ├── ascii_to_lst.py
│   ├── box_print.py
│   ├── clear.py
│   ├── coin_flip.py
│   ├── confirm.py
│   ├── countdown.py
│   ├── dots_loading.py
│   ├── int_input.py
│   ├── marquee.py
│   ├── matrix_rain.py
│   ├── percent_loader.py
│   ├── print.py
│   ├── progress.py
│   ├── rainbow_print.py
│   ├── roll_dice.py
│   ├── spinner.py
│   └── str_input.py
```


---

## ⚡ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wdym-rizvi/CLI.git
   cd CLI
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is missing, you can generate it using:
   >
   > ```bash
   > pipreqs . --force
   > ```

---

## ▶️ Usage

Run the main app:

```bash
python run.py
```

### Credentials

* Username: `voldermot`
* password:  `harrypotter`
* These are encrypted using python libray cryptography (saved in `creds/credentials.json`)
* These are decrypted using Fernet key (saved in `creds/fernet.key`)

### First Run

* Asks for your name (saved in `configs/config.json`).
* Asks if you want background music (saved in `configs/music.json`).

### Menu Example

```
[01] Public IP           [09] Current Time
[02] Local IP            [10] Port Scan
[03] System Info         [11] SSL Info
[04] CPU Usage           [12] Kill Process
[05] RAM Info            [13] Traceroute
[06] Screenshot          [14] DNS Lookup
[07] Website Screenshot  [15] WHOIS Lookup
[08] Hostname            [16] Zip Folder

[99] About         [00] Exit
```

---

## 🎵 Music & Sound

* Plays a **startup sound** at launch.
* Background Phonk music can be enabled/disabled on first run.
* Music settings stored in `configs/music.json`.

---

## 🔧 Requirements

* Python 3.8+
* External Libraries:

  * `rich`
  * `pygame`

These will auto-install if missing.

---

## 📜 License

All rights reserved © 2025
Coded by **Rizvi**

---

## 🌐 Links

* Visit: [CLI APP CrackServer](https://crackserver.doraemonh413.workers.dev)

  * Username & Pass: **CrackServer**
