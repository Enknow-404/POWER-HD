# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))