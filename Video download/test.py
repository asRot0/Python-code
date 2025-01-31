import yt_dlp


def download_instagram_video(video_url, output_path="downloads/"):
    """
    Downloads an Instagram video using yt-dlp.

    Args:
        video_url (str): The URL of the Instagram video.
        output_path (str): Directory to save the downloaded video.
    """
    options = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Get the best available quality
        'quiet': False
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])


# Example usage
if __name__ == "__main__":
    video_url = 'video url'
    download_instagram_video(video_url)
