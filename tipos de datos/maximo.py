# region [valido en vscode]
import sys
import struct

print(sys.maxsize)
print(float("-inf"))
# (2**size-1)-1
print(2**(struct.Struct('i').size*8-1)-1)

# endregion
