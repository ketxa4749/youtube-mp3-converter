
import yt_dlp
import os

def download_video_as_mp3(video_url, output_path):
    """
    Downloads a YouTube video and converts it to MP3 format.

    Args:
        video_url: The URL of the YouTube video.
        output_path: The directory where the MP3 file will be saved.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video successfully downloaded and converted to MP3.")
    except Exception as e:
        print(f"An error occurred: {e}")

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python youtube_to_mp3.py <youtube_video_url>")
        sys.exit(1)

    video_link = sys.argv[1]
    download_directory = "downloads/mp3"
    
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
        
    download_video_as_mp3(video_link, download_directory)
