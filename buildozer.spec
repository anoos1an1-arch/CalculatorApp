[app]

title = CalculatorApp

package.name = calculatorapp

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


# Android settings
android.api = 33

android.minapi = 23

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True


# Build settings
p4a.bootstrap = sdl2

osx.python_version = 3

android.allow_backup = True
