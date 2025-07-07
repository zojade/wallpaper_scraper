# 🖼️ Wallpaper Scraper

A simple and lightweight Python tool to **search and download high-resolution wallpapers** from [wallhaven.cc](https://wallhaven.cc). Includes both a **GUI** and a **CLI** for convenience.

---

## 🔧 Features

- 🔍 Keyword-based wallpaper search
- 📁 Auto-organized into folders per keyword
- 📦 GUI (`.exe`) and CLI support
- 💡 Skips already-downloaded images
- 🎨 Custom `.ico` icon support for GUI

---

## 🖥️ GUI Usage

1. Navigate to the `dist/` folder.
2. Run `gui.exe`.
3. Enter the **keyword** and **number of wallpapers** you want.
4. Wallpapers will be downloaded to:
   ```
   wallpapers/<your_keyword>/
   ```

> ✅ No need for Python or dependencies to use the `.exe`.

---

## 💻 CLI Usage

If you prefer terminal:

```bash
cd cli
python main.py
```

You’ll be prompted for:
- Keyword(s)
- Number of wallpapers

---

## 📁 Folder Structure

```
wallpaper_scraper/
├── cli/
│   └── main.py
├── dist/
│   └── gui.exe
├── gui.py
├── wallhaven.py
├── utils.py
├── myicon.ico
├── .gitignore
├── README.md
```

---

## 🛠️ Optional: Build EXE Yourself

```bash
pyinstaller --noconsole --onefile --icon=myicon.ico gui.py
```

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Contributions

Open to suggestions, improvements, or PRs. Feel free to fork the repo and build on it!