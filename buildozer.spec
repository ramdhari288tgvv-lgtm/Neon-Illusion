[app]

title = Neon Illusion
package.name = neonillusion
package.domain = org.ankush

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions =

android.archs = arm64-v8a,armeabi-v7a

android.debug_artifact = apk
android.release_artifact = apk


[buildozer]

log_level = 2
warn_on_root = 1
