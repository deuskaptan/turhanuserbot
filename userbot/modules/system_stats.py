# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# turhan UserBot - Yusuf Usta


""" Sunucu hakkında bilgi veren UserBot modülüdür. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import uname
from shutil import which
from os import remove

import random
from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = uname().node
# ============================================

ALIVE_MESAJ = ["Turhan geldi yolu açın!", "Turhan, bize ordan bi menemen 2 çay", "Turhan ordusu toplandı !"]



@register(outgoing=True, pattern="^.alive$")
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(f"`{random.choice(ALIVE_MESAJ)}  Turhan çalışıyor.`")


CMD_HELP.update(
    {"sysd": ".sysd\
    \nKullanım: Neofetch modülünü kullanarak sistem bilgisi gösterir."})
CMD_HELP.update({"botver": ".botver\
    \nKullanım: Userbot sürümünü gösterir."})
CMD_HELP.update(
    {"pip": ".pip <module(s)>\
    \nKullanım: Pip modüllerinde arama yapar."})
CMD_HELP.update({
    "alive": ".alive\
    \nKullanım: Turhan botunun çalışıp çalışmadığını kontrol etmek için kullanılır."
})
