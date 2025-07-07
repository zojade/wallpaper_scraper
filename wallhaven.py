# wallhaven.py
import requests
from bs4 import BeautifulSoup
import os
import time
from utils import sanitize_filename


def scrape_wallhaven(keyword, limit=5):
    headers = {"User-Agent": "Mozilla/5.0"}
    base_path = os.path.join("wallpapers", sanitize_filename(keyword))
    os.makedirs(base_path, exist_ok=True)

    count = 0
    page = 1

    while count < limit:
        search_url = f"https://wallhaven.cc/search?q={keyword}&page={page}"
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            print(f"[-] Failed to load page {page}: Status {response.status_code}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        thumbs = soup.select("figure.thumb a.preview")

        if not thumbs:
            print(f"[!] No more wallpapers found on page {page}.")
            break

        for a in thumbs:
            if count >= limit:
                break

            page_url = a["href"]
            wallpaper_id = page_url.split("/")[-1]
            prefix = wallpaper_id[:2]
            full_url = (
                f"https://w.wallhaven.cc/full/{prefix}/wallhaven-{wallpaper_id}.jpg"
            )
            filename = sanitize_filename(f"wallhaven-{wallpaper_id}.jpg")
            filepath = os.path.join(base_path, filename)

            if os.path.exists(filepath):
                print(f"[!] Already exists, skipping: {filename}")
                continue

            try:
                img_data = requests.get(full_url, headers=headers)
                if img_data.status_code == 200 and img_data.headers[
                    "Content-Type"
                ].startswith("image"):
                    with open(filepath, "wb") as f:
                        f.write(img_data.content)
                    print(f"[+] Downloaded: {filename}")
                    count += 1
                else:
                    print(f"[-] Skipped (image not found): {full_url}")
            except Exception as e:
                print(f"[-] Error downloading {full_url}: {e}")

            time.sleep(1)  # Respect the server

        page += 1  # go to the next page
