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


# Android
android.api = 33
android.minapi = 23
android.ndk = 25c

android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = INTERNET


# Build
p4a.bootstrap = sdl2

[buildozer]

log_level = 2

warn_on_root = 1
