# Arank - UserBot
# Copyright (C) 2020 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}bored`
    Get some activity to do when you get bored
"""

from . import async_searcher, Arank_cmd


@Arank_cmd(pattern="bored$")
async def bored_cmd(event):
    msg = await event.eor("`Generating an Activity for You!`")
    content = await async_searcher(
        "https://www.boredapi.com/api/activity", re_json=True
    )
    m = f"**Activity:** `{content['activity']}`"
    if content.get("link"):
        m += f"**Read More:** {content['link']}"
    if content.get("participants"):
        m += f"\n**Participants Required:** `{content['participants']}`"
    if content.get("price"):
        m += f"\n**Price:** `{content['price']}`"
    await msg.edit(m)
