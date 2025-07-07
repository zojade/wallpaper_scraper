🖼️ Wallpaper Scraper - Wallhaven.cc Image Downloader
====================================================

This tool helps you download high-resolution wallpapers from Wallhaven.cc 
based on keywords or direct image/page URLs.

📁 Folder Structure
--------------------
.
├── dist/
│   └── gui.exe         <- Standalone GUI application (no Python required)
├── cli/
│   └── main.py         <- Optional command-line interface (Python required)
├── README.txt          <- You're reading it!


🎨 GUI Instructions (Recommended)
----------------------------------
1. Go to the `dist/` folder.
2. Double-click `gui.exe`.
3. Enter a wallpaper keyword (e.g., "solo leveling", "nature").
4. Enter how many wallpapers to download.
5. Done!

✅ The GUI shows progress and status.
🖼️ Downloaded images are saved to: `wallpapers/<your-keyword>/`


🖥️ CLI Instructions (Optional, for Python users)
--------------------------------------------------
1. Make sure you have Python 3 installed.
2. Navigate to the `cli/` folder in terminal or PowerShell.
3. Run:
   python main.py
4. Enter a keyword or image/page URL.
5. Enter how many wallpapers to download.

Images will also be saved in the `wallpapers/<your-keyword>/` folder.


📌 Notes
---------
- No installation needed for GUI. Just run `gui.exe`.
- Internet connection is required.
- Works only with public images on [wallhaven.cc](https://wallhaven.cc/).
- Avoid entering the same keyword repeatedly; it skips duplicates.


📦 Credits
-----------
Developed by: [Your Name or GitHub Link]
Built with: Python, BeautifulSoup, Tkinter

Icons used: Custom `.ico` file (for GUI)

