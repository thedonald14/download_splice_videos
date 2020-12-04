# download_splice_videos
This program downloads videos from the internet, and splices sections out of them.

You can use the tool to download a full video like this :

python3 splicevideo.py https://www.youtube.com/watch?v=Wibk3QsT7-M

Or you can choose to extract clips from the video url like this :

python3 splicevideo.py https://www.youtube.com/watch?v=Wibk3QsT7-M 0:14 0:16

The program requires :
moviepy &
typer
