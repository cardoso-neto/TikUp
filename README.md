TikUp
=====

An auto downloader and uploader for TikTok profiles.

**Requirements**  
[TikTok-Api](https://github.com/davidteather/TikTok-Api) and [internetarchive](https://archive.org/services/docs/api/internetarchive/index.html) on Python 3.

**How to Install**  
Install with `pip install tikup`.

**How to Use**
```
usage: tikup.py [-h] [--no-delete] [--hashtag] [--limit LIMIT]
                [--use-download-archive] [--id] [--liked] [--sort]
                user

An auto downloader and uploader for TikTok videos.

positional arguments:
  user

optional arguments:
  -h, --help            show this help message and exit
  --no-delete           don't delete files when done
  --hashtag             download hashtag instead of username
  --limit LIMIT         set limit on amount of TikToks to download
  --use-download-archive
                        record the video url to the download archive. This
                        will download only videos not listed in the archive
                        file. Record the IDs of all downloaded videos in it.
  --id                  download this video ID
  --liked               download the user's liked posts
  --sort                sort into folders based on TikTok username
```

**Internet Archive upload**

To interact with the Internet Archive, you will first need to [create an IA account](https://archive.org/account/login.createaccount.php).

Confirm your account and note down your email address and password.

Then run `ia configure` and log in.
