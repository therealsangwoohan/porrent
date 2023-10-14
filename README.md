Porrent is a BitTorrent client written in Python.

To torrent, first download a .torrent file. For example,

we can download Debian CD images with BitTorrent: https://www.debian.org/CD/torrent-cd/

Example command:

```
$ python run.py ~/debian-12.0.0-amd64-netinst.iso.torrent ~/Downloads/debian.iso
```

This downloads using ~/debian-12.0.0-amd64-netinst.iso.torrent to ~/Downloads/debian.iso