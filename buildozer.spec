[app]
source.dir = .

# (str) Title of your application
title = ShizukuPwne

# (str) Package name
package.name = shizukupwne

# (str) Package domain (needed for android packaging)
package.domain = org.shizuku

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to not exclude anything)
source.exclude_exts = spec

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Permissions
#android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) List of service to declare
#services = 

#
# Android specific
#

# (bool) Export application on Android
android.api = 33

# (int) Target Android API, should be as high as possible.
android.min_api = 21

# (str) Android NDK version to use
#android.ndk_version = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

# (CNS) Android app icon
#icon.filename = %(source.dir)s/data/icon.png

# (str) The Android arch to build for,, choices are: armeabi-v7a, arm64-v8a, x86, x86_64
# default is armeabi-v7a.
