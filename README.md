# firebase-addr2line-util
This tool can help to decode native stacktrace frames when Firebase Crashlytics (or other services) can't do it automatically.

# Install
- install python
- find the location of NDK inside the Unity folder. The version of Unity must be equal to your project's version. I noticed executable file can crash when the path contains a space symbol, so I made a local copy into my drive root
- modify script:
  - set `ADDR2LINE_BINARY` with path to addr2line executable according to platform of your machine (I used `NDK\\toolchains\\x86-4.9\\prebuilt\\windows-x86_64\\bin\\i686-linux-android-addr2line.exe` on my Windows machine)
  - add the full path to `LIBS` dictionary, for example:
  ```
  LIBS = {
    'libil2cpp.so': 'arm64-v8a\\libil2cpp.sym.so',
    'libunity.so': 'arm64-v8a\\libunity.sym.so'
  }
  ```
  - keep in mind that Unity can build both armeabi-v7a and arm64-v8a native libs, so you should modify this dictionary according to CPU architecture of your stacktraces you need to inspect
  
# Usaage
- start the script
- paste stacktrace
- press ENTER button twice

# Stacktrace formats
Currently, I found two formats Firebase shows the stacktrace, and both of them supported
something like that:
```
#00 pc 0x711b0 libc.so 
#01 pc 0x8e4c55 libunity.so 
#02 pc 0x8e2daf libunity.so 
#03 pc 0x8e122 libc.so 
#04 pc 0x8e4d47 libunity.so 
```
and something like that:
```
libunity.0x74314d
libunity.0x18b6e1
libunity.0x1c84c1
libunity.0x1c9221
```
