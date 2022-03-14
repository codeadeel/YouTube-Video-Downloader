# YouTube Video Downloader

* [**Introduction**](#introduction)  
* [**Setup**](#setup)  
* [**Basic Usage**](#bu)  
* [**Arguments**](#arguments)  
    * [-h, --help](#help)  
    * [-l, --link](#link)  
    * [-qc, --quality_check](#qc)  
    * [-q , --quality](#q)  
    * [-s , --save](#s)  
    * [-fr , --frame_rate](#fr)  
    * [-fmpg , --ffmpeg](#fmpg)  
    * [-ytdl , --youtube_dl](#ytdl)

## <a name="introduction">Introduction

The subject code is responsible for downloading videos from YouTube including regular ones & livestreams. The Python script named [***downloader.py***][downloader.py link] is based on [***FFMPEG***][FFMPEG link] & [***YouTube-dl***][YouTube-dl link]. This script can be executed through Command Line Interface. The input arguments for [***downloader.py***][downloader.py link] can be check by executing `downloader.py -h` in the terminal.

```bash
usage: downloader.py [-h] -l  [-qc] [-q] [-s] [-fr] [-fmpg] [-ytdl]

YouTube Video Downloader.

optional arguments:
  -h, --help            show this help message and exit
  -l , --link           YouTube Link to Download Livestream from
  -qc, --quality_check  Check Available Qualities
  -q , --quality        Set Video Download Quality
  -s , --save           Absolute Address to Save Downloaded Video
  -fr , --frame_rate    Frame Rate to Save the Downloaded Video
  -fmpg , --ffmpeg      Absolute Address to Standalone FFMPEG File
  -ytdl , --youtube_dl  Absolute Address to Standalone youtube-dl File
```
## <a name="setup">Setup
Before cloning the repository, please setup environment as following:

```bash
sudo apt-get install git-lfs
sudo ln -s /usr/bin/python3 /usr/bin/python
```

## <a name="bu">Basic Usage

The following command can be used to quickly download video from YouTube, subject to default available quality & settings.

```bash
downloader.py -l [Link to YouTube Page]
```
When the desired downloaded duration is acheived, than by pressing `Ctrl+C` ***only one time***, we can terminate the script. After termination, downloaded video will automatically saved to address given at `-s , --save` in `downloader.py`. The documentation for `-s , --save` in `downloader.py`, is given [here](#s).

## <a name="arguments"></a>Arguments

Following are the details of input arguments to the [***downloader.py***][downloader.py link] script.

##### <a name="help"></a>-h, --help
Displays the help message including input arguments by executing `downloader.py -h` on the terminal.

##### <a name="link"></a>-l, --link
HTTPS link to YouTube video page. Highlighted example is also given below:

![YouTube Link Example][YouTube HTTP Example]

##### <a name="qc"></a>-qc, --quality_check
Its a boolean flag. If this flag is active, the script only shows the available qualities or resolutions of the video to download, without downloading the video itself. From viewing flags manually, we can capture quality ID which than can be given to `-q , --quality` argument of `downloader.py`. For example, execution of following command:

```bash
downloader.py -l https://www.youtube.com/watch?v=ZmYkXyhfnVQ -qc
```

Results in following output:

```bash
[youtube] ZmYkXyhfnVQ: Downloading webpage
[youtube] ZmYkXyhfnVQ: Downloading m3u8 information
[youtube] ZmYkXyhfnVQ: Downloading MPD manifest
[info] Available formats for ZmYkXyhfnVQ:
format code  extension  resolution note
91           mp4        256x144     290k , avc1.42c00b, 15.0fps, mp4a.40.5
92           mp4        426x240     546k , avc1.4d4015, 30.0fps, mp4a.40.5
93           mp4        640x360    1209k , avc1.4d401e, 30.0fps, mp4a.40.2
94           mp4        854x480    1568k , avc1.4d401f, 30.0fps, mp4a.40.2
95           mp4        1280x720   2969k , avc1.4d401f, 30.0fps, mp4a.40.2
96           mp4        1920x1080  5420k , avc1.640028, 30.0fps, mp4a.40.2 (best)
```

Where in the above output, `format code` denotes quality ID or `-q , --quality` for `downloader.py`.

##### <a name="q"></a>-q , --quality
Quality ID or resolution ID of the video subject to download. Its a numeric number that can be manually checked by `-qc, --quality_check` flag in `downloader.py`. The default quality ID is set to `94`. The documentation for finding quality ID is given [here](#qc).

##### <a name="s"></a>-s , --save
Absolute address to save downloaded video. When desired downloaded time is reached, by pressing `Ctrl+C` ***only one time***, we can terminate the script. After termination, downloaded video will automatically saved to address given at `-s , --save` in `downloader.py`. Default saving address is set to `./Downloaded_Video.mp4`.

##### <a name="fr"></a>-fr , --frame_rate
This represents the framerate to which the downloaded will save. It solely depends on [***FFMPEG***][FFMPEG link], as it represents saving framerate, instead of downloading framerate. The default video saving framerate is set to `30` Frame Per Second. Downloading framerate can be choosed from quality ID. The documentation for finding quality ID is given [here](#qc).

##### <a name="fmpg"></a>-fmpg , --ffmpeg
Address to [***FFMPEG***][FFMPEG link] file. This is responsible for get the link and save the video file.

##### <a name="ytdl"></a>-ytdl , --youtube_dl
Address to [***YouTube-dl***][YouTube-dl link] file. This is responsible for get the link from YouTube & create a forward Pipe to [***FFMPEG***][FFMPEG link].

[downloader.py link]: ./downloader.py
[FFMPEG link]: ./ffmpeg
[YouTube-dl link]: ./youtube-dl
[YouTube HTTP Example]: ./MarkDown-Data/link-example.png
