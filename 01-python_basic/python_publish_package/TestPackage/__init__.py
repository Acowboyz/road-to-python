# can use import TestPackage from sendmsg: sendmsg.sendmsg()
__all__ = ["sendmsg"]

# can use import TestPackage : TestPackage.sendmsg.sendmsg()
from . import sendmsg
