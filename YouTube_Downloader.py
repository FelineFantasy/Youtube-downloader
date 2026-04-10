import yt_dlp


ydl_opts = {
    'format': 'best',
    'quiet': True,
    'no_warnings': True,
}

def main():
    url = input("Paste YouTube URL: ").strip()

    if not url:
        print("Error: empty URL!")
        return

    if "youtube.com" not in url and "youtu.be" not in url:
        print("Error: invalid YouTube URL!")
        return

    print("Downloading...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Done! Video saved.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
