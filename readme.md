# YouTube Video Downloader 🎥

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A simple utility for downloading videos from YouTube, written in Python. Paste a link — get the video!

## 📋 Table of Contents
- [Description](#description)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Example Usage](#example-usage)
- [Project Files](#project-files)
- [Requirements](#requirements)
- [Future Plans](#future-plans)
- [Author](#author)

## 📝 Description

**YouTube Video Downloader** is a simple console program for downloading videos from YouTube. It uses the powerful `yt-dlp` library and automatically saves videos in the best available quality.

### Features:
- 🚀 **Simplicity** — Paste a link and get the video
- 📦 **Compact** — Just a few lines of code
- ⚡ **Speed** — Downloads videos in maximum quality
- 🛡️ **Safety** — Error handling during download

## 🎮 How to Use

1. Run the program
2. Paste a YouTube video link
3. Press Enter
4. Wait for the download completion message

The video will be saved in the same folder as the program.

## ⚙️ Installation

### Option 1: Download ZIP
1. Click the green **"Code"** button on this page
2. Select **"Download ZIP"**
3. Extract the archive
4. Install dependencies: `pip install -r requirements.txt`
5. Run the program: `python YouTube_Downloader.py`

### Option 2: Clone repository
```bash
git clone https://github.com/FelineFantasy/Youtube_downloader.git
cd Youtube_downloader
pip install -r requirements.txt
python YouTube_Downloader.py
```

## 💻 Example Usage

```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading...
Download complete!
```

## 📁 Project Files

```
Youtube_downloader/
├── YouTube_Downloader.py  # Main program file
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## 📋 Requirements

- Python 3.x
- yt-dlp

## 🔮 Future Plans

- [ ] Add support for playlists
- [ ] Audio-only download option
- [ ] Progress bar during download

## 👤 Author

**FelineFantasy**

License: MIT
