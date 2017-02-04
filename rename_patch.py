#!/usr/bin/env python

from sys import argv
from os import path
from struct import pack_into

PATCH_NAME_OFFSET = 217
SCREEN_DISPLAY_CHARS = 16
PACK_FORMAT = 'cccccxcccccccxcccc' # 7 bytes plus 1 byte padding

def rename_patch(filename):
    """ Set the patch name in a Mopho X4 patch file
    to the filename of the sysex file.
    """
    patch_name, _ = path.splitext(filename)
    patch_name = patch_name[0:SCREEN_DISPLAY_CHARS]

    with open(filename, 'r+b') as f:
        bytes = bytearray(f.read(300))

        # Detech if is patch format
        # Support changing patch number

        padded = patch_name.ljust(SCREEN_DISPLAY_CHARS)
        pack_into(PACK_FORMAT, bytes, PATCH_NAME_OFFSET, *padded)

        f.seek(0)
        f.write(bytes)

filename = argv[1]
rename_patch(filename)
