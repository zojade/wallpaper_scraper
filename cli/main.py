# main.py
from wallhaven import scrape_wallhaven
from utils import download_image_from_url, extract_wallhaven_page


def main():
    user_input = input("Enter keywords (comma-separated) or image/page URL: ").strip()

    # If the user enters a direct URL
    if user_input.startswith("http"):
        if user_input.endswith((".jpg", ".jpeg", ".png", ".webp")):
            download_image_from_url(user_input)
        elif "wallhaven.cc/w/" in user_input:
            extract_wallhaven_page(user_input)
        else:
            print("[-] Unsupported URL format.")
        return  # exit after processing single URL

    # Ask for download limit
    try:
        limit = int(input("How many wallpapers for each keyword? (e.g., 5): ").strip())
    except:
        limit = 5

    # Split multiple keywords
    keywords = [k.strip() for k in user_input.split(",") if k.strip()]
    for keyword in keywords:
        print(f"\n[🔍] Searching wallpapers for: {keyword}")
        scrape_wallhaven(keyword, limit=limit)


if __name__ == "__main__":
    main()
