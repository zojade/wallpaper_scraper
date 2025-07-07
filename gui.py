import tkinter as tk
from tkinter import ttk, messagebox
import threading
import wallhaven
import os


def start_scrape():
    keywords = keyword_entry.get()
    count = count_entry.get()

    if not keywords.strip():
        messagebox.showerror("Input Error", "Please enter at least one keyword.")
        return

    try:
        limit = int(count.strip())
    except:
        messagebox.showerror("Input Error", "Please enter a valid number for count.")
        return

    scrape_button.config(state="disabled")
    progress["value"] = 0
    status_label.config(text="Starting download...")

    # run scraper in separate thread to prevent freezing GUI
    threading.Thread(target=scrape_wallpapers, args=(keywords, limit)).start()


def scrape_wallpapers(keywords, limit):
    keyword_list = [k.strip() for k in keywords.split(",")]
    total = len(keyword_list)
    done = 0

    for keyword in keyword_list:
        status_label.config(text=f"Downloading for: {keyword}")
        wallhaven.scrape_wallhaven(keyword, limit)
        done += 1
        progress["value"] = int((done / total) * 100)

    status_label.config(text="Done!")
    scrape_button.config(state="normal")


# GUI setup
root = tk.Tk()
root.title("Wallpaper Scraper")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter keywords (comma-separated):").pack(pady=(10, 0))
keyword_entry = tk.Entry(root, width=40)
keyword_entry.pack(pady=5)

tk.Label(root, text="Number of wallpapers per keyword:").pack(pady=(10, 0))
count_entry = tk.Entry(root, width=10)
count_entry.insert(0, "5")
count_entry.pack(pady=5)

scrape_button = tk.Button(root, text="Download Wallpapers", command=start_scrape)
scrape_button.pack(pady=15)

progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
