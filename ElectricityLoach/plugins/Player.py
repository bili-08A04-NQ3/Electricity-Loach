import requests
from nonebot import on_natural_language, NLPSession
from ElectricityLoach.utils.LevelChecker import CanResponse


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    if not CanResponse(session, 2):
        return
    s: str = session.msg
    a: str = "\n\\/{}[] "
    c: list = list(a)
    for b in c:
        s = s.replace(b, "")
    if s.find("玩家") == 0:
        Player: str = "".join(i for i in s if ord(i) < 256)
        try:
            UUID: str = requests.get("https://api.mojang.com/users/profiles/minecraft/" + Player).json()["id"]
            HistoryName = requests.get("https://api.mojang.com/user/profiles/" + UUID + "/names").json()
            Names: str = ""
            for i in HistoryName:
                Name = i["name"]
                Names += (Name + ",")
            await session.send("玩家信息:" + Player + "\nUUID: " + UUID + "\n历史名称: " + Names)
        except:
            pass
        finally:
            pass
