# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))