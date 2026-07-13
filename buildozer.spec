[app]
title = Savage Downloader
package.name = savagedownloader
package.domain = org.savage.rip
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,yt-dlp,certifi
orientation = portrait
fullscreen = 0
permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# THIS IS THE FIX: Automatically accept Android SDK licenses
android.accept_sdk_license = True
