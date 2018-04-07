import re

s = """
=?utf-8?B?W0lUIERhdGEgUmVxdWVzdCBTeXN0ZW1dIFRoZSBkb2N1bWVudCBpcyByZWFz?==?utf-8?B?c2lnbiA+PiDoq4vkv67mraMg5aGr5ZauIOe/kuaFoywgICAgICgqKiBTZWN1?==?utf-8?B?cml0eSBDKiop?=
"""

result = re.findall(r"\?utf-8\?B\?(.*?)\?=", s)
print("".join(result))
