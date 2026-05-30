import yt_dlp

def get_quality_choice():
    """Показывает меню выбора качества и возвращает формат."""
    print("\nВыберите качество:")
    print("1. Лучшее (до 4K)")
    print("2. 1080p (Full HD)")
    print("3. 720p (HD)")
    print("4. 480p")
    print("5. 360p")
    print("6. Только аудио (M4A)")
    
    choice = input("Ваш выбор (1-6): ").strip()
    
    formats = {
        "1": "best",
        "2": "best[height<=1080]",
        "3": "best[height<=720]",
        "4": "best[height<=480]",
        "5": "best[height<=360]",
        "6": "bestaudio[ext=m4a]",
    }
    
    return formats.get(choice, "best")

def main():
    url = input("Вставьте ссылку на YouTube: ").strip()

    if not url:
        print("Ошибка: пустая ссылка!")
        return

    if "youtube.com" not in url and "youtu.be" not in url:
        print("Ошибка: неверная ссылка на YouTube!")
        return

    format_choice = get_quality_choice()

    ydl_opts = {
        'format': format_choice,
        'quiet': True,
        'no_warnings': True,
    }

    print("\nЗагрузка...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Готово! Видео сохранено.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
