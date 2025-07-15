# YouTube to MP3 Converter

A simple Python script to download YouTube videos and convert them to MP3 format.

## Features

- Downloads the best quality audio from a given YouTube video URL.
- Converts the downloaded audio to MP3 format using FFmpeg.
- Saves the final MP3 file in the `downloads/mp3` directory.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ketxa4749/youtube-mp3-converter.git
    cd youtube-mp3-converter
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install yt-dlp
    ```

## Usage

Run the script from your terminal with the YouTube video URL as an argument:

```bash
python youtube_to_mp3.py <youtube_video_url>
```

### Example

```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

The downloaded MP3 file will be saved in the `downloads/mp3` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
