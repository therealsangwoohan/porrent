import sys

from porrent.torrent import Torrent

torrent_file_path = sys.argv[1]
download_path = sys.argv[2]

torrent = Torrent(torrent_file_path)

torrent.download(download_path)
