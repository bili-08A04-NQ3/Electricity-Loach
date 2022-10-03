import random
import time
import json
from ElectricityLoach.utils.LevelChecker import CanResponse
from ElectricityLoach.utils.CoolDownData import reset
from nonebot import on_natural_language, NLPSession

with open("ElectricityLoach/CompleteReplyWords.json", encoding="utf-8") as f:
    CompleteReplyWords: dict = json.load(f)

with open("ElectricityLoach/MatchReplyWords.json", encoding="utf-8") as f:
    MatchReplyWords: dict = json.load(f)


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    if not CanResponse(session, 1):
        return
    s: str = session.msg
    # 模糊匹配
    try:
        KeyWords = MatchReplyWords.keys()
        for i in KeyWords:
            if s.find(i) == 0:
                if not reset("MatchReplyWord" + i):
                    return
                MatchReplyWord = MatchReplyWords[random.randint(0, len(MatchReplyWords) - 1)]
                time.sleep(random.randint(2, 4))
                await session.send(MatchReplyWord)
                return

        # 完全匹配
        CompleteReply: list = CompleteReplyWords[s]
        Word: str = CompleteReply[random.randint(0, len(CompleteReply) - 1)]
        if not reset("CompleteReply" + s):
            return
        time.sleep(random.randint(2, 4))
        await session.send(Word)
    except:
        pass