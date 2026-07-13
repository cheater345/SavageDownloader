[app]
title = Savage Downloader
package.name = savagedownloader
package.domain = org.savage.rip
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy==2.3.0,yt-dlp,certifi,requests
orientation = portrait
fullscreen = 0
permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 31
android.min_api = 21
android.accept_sdk_license = True
