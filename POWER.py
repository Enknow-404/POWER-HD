# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))