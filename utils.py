# utils.py
import os
import re
import requests
from bs4 import BeautifulSoup

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def download_image_from_url(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    filename = sanitize_filename(url.split("/")[-1])
    os.makedirs("wallpapers", exist_ok=True)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and response.headers['Content-Type'].startswith("image"):
            with open(f"wallpapers/{filename}", "wb") as f:
                f.write(response.content)
            print(f"[+] Downloaded direct image: {filename}")
        else:
            print(f"[-] Failed to fetch image. Status: {response.status_code}")
    except Exception as e:
        print(f"[-] Error downloading image: {e}")

def extract_wallhaven_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"[-] Page request failed: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        img_tag = soup.find("img", id="wallpaper")
        if not img_tag or not img_tag.get("src"):
            print("[-] Full image not found on page.")
            return

        image_url = img_tag["src"]
        download_image_from_url(image_url)

    except Exception as e:
        print(f"[-] Error extracting Wallhaven page: {e}")
