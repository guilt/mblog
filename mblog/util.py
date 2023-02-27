import os


def getFullUserName():
    osName = os.name.lower()
    if osName == 'nt' or 'win' in osName:
        import ctypes

        GetUserNameExW = ctypes.windll.secur32.GetUserNameExW
        nameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameExW(nameDisplay, None, size)

        displayNameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameExW(nameDisplay, displayNameBuffer, size)
        return displayNameBuffer.value
    else:
        import pwd

        unixDisplayName = ( entry[4] for entry in pwd.getpwall() if entry[2] == os.geteuid() )
        return unixDisplayName.__next__()
