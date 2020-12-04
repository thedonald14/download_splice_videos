"""This Program downloads a Video from the Internet , and splices it
Copyright (C) 2020  -- Author : chr21328

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
          
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA."""
        

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import subprocess
from urllib.parse import urlparse
import typer
from typing import Optional
import os
import re
    
app = typer.Typer()

@app.command()
def splicevideo(videourl : str, start : str ,stop : str,
                outputname : Optional[str] = typer.Argument(None)):
    '''
       This Function first downloads a video, and then Splices out a Section based on timestamp minutes:seconds entered.
       
       Paramaters :
       videourl : Full URL String of Video URL from sites such as YouTube,Bitchute, or Twitter.

       start : mm:ss of Video to Splice. examples -- 0:22 or 1:35  
       
       stop  : mm:ss of Video to Splice. examples -- 0:36 or 1:48

       [Optional] outputname : Name to save downloaded file as , DO NOT INCLUDE filetype at end
    '''

    if not outputname:
        if urlparse(videourl).query:
            outputname = re.sub('[\W_]+','',urlparse(videourl).query)
        else:
            outputname = re.sub('[\W_]+', '', videourl).replace('www','').replace('https','').replace('com','')

    targetname = f"{outputname}_{start}_to_{stop}.mp4".replace(':','')
    
    if not os.path.exists(f"{outputname}.mp4"):
        subprocess.call(f"yes Y | you-get -O {outputname} {videourl}",shell=True)

    start = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(start.split(':'))))
    stop = sum(x * int(t) for x, t in zip([1, 60, 3600], reversed(stop.split(':'))))

    ffmpeg_extract_subclip(f"{outputname}.mp4", start, stop, targetname=targetname)

    #TODO Add ability to Accept multiple Clip entries.
    #TODO Add ability to combine all Spliced Clips into single Video.

if __name__ == "__main__":
    typer.run(splicevideo)


# https://pyscenedetect.readthedocs.io/en/latest/examples/usage-example/
# https://pypi.org/project/youtube-transcript-api/
# https://github.com/senko/python-video-converter
