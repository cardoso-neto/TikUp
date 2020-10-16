from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="An auto downloader and uploader for TikTok videos.")
    parser.add_argument("user")
    parser.add_argument(
        "--no-delete", action="store_false", help="don't delete files when done"
    )
    parser.add_argument(
        "--hashtag", action="store_true", help="download hashtag instead of username"
    )
    parser.add_argument(
        "--limit", help="set limit on amount of TikToks to download"
    )
    parser.add_argument(
        "--use-download-archive",
        action="store_true",
        help=(
            "record the video url to the download archive. "
            "This will download only videos not listed in the archive file. "
            "Record the IDs of all downloaded videos in it."
        ),
    )
    parser.add_argument(
        "--id", action="store_true", help="download this video ID"
    )
    parser.add_argument(
        "--liked", action="store_true", help="download the user's liked posts"
    )
    args = parser.parse_args()
    return args
