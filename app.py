import streamlit as st
import pytube
from io import BytesIO

def download_youtube_video():
    # Get the YouTube video URL from the user
    url = st.text_input("Enter the YouTube video URL:", "")

    if url:
        try:
            # Create a YouTube object
            yt = pytube.YouTube(url)

            # Get the highest resolution video stream
            st.write(yt.title)
            st.image(yt.thumbnail_url)

            # Get the available video stream resolutions
            resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]

            # Allow the user to select the desired resolution

            selected_resolution = st.selectbox("Select the video resolution", resolutions, index=None)
            if selected_resolution:
                selected_stream = yt.streams.filter(progressive=True, resolution=selected_resolution).first()
                # Download the video stream to a BytesIO object
                video_bytes = BytesIO()
                selected_stream.stream_to_buffer(video_bytes)
                video_bytes.seek(0)

                # Provide the video file for download
                st.download_button(
                    label="Download Video",
                    data=video_bytes,
                    file_name=selected_stream.default_filename,
                    mime="video/mp4",
                )
        except Exception as e:
            st.error(f"Error downloading the video: {e}")

def main():
    st.title("YouTube Video Downloader")
    download_youtube_video()

if __name__ == "__main__":
    main()