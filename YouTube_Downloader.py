import yt_dlp


ydl_opts = {
    'format': 'best',
    'quiet': True,
    'no_warnings': True,
}

def main():
    url = input("Вставь ссылку на видео: ").strip()

    print("Начинаю загрузку...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Готово! Видео сохранено")
    except Exception as error:
        print(f"Что-то пошло не так: {error}")

if __name__ == "__main__":
    main()
yt-dlp
