 
# To decompile an apk

``apktool d -r -s application.apk

# Launch android emul 

``cd C:\Users\marks\AppData\Local\Android\Sdk\emulator

Find the emulator.exe path and go inside then : 

``.\emulator -list-avds``

``.\emulator -avd Pixel_5_API_28 -writable-system



Go to adb path and then 
``cd C:\Users\marks\AppData\Local\Android\Sdk\platform-tools

Inside adb.exe path :
``.\adb shell

Root and send files
``.\adb root
``.\adb remount
``.\adb push *locale file inside adb path* /storage (phone up)

# Launch frida
Go to adb path and then 
``cd C:\Users\marks\AppData\Local\Android\Sdk\platform-tools

``.\adb.exe shell “/data/local/tmp/frida-server &”

``frida -U -f com.nordvpn.android -l .\choose.js
