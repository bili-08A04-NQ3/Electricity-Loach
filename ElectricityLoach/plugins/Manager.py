import json

from nonebot import on_command, CommandSession


@on_command('group', aliases='群', only_to_me=False)
async def _(session: CommandSession):
    if session.event.user_id != 2796947461:
        await session.send("你不是我的主人,呜呜呜")
        return
    Rd: list = session.current_arg_text.strip().split(" ")
    if Rd[0] == "add":
        if Rd[1] == "help":
            await session.send("""group add <group> <level>, group接受整数,也可以是this
level取值如下
0: 没得回复
1: 关键词回复(默认)
2: 命令回复
3: 群管活动
4: 肆意妄为""")
            return
    # group add <Id> <Level>
    GroupId: str = Rd[1]
    if GroupId == "this":
        GroupId: str = str(session.event.group_id)
    Level: int = int(Rd[2])
    with open("ElectricityLoach/GroupManager.json", "r", encoding="utf-8") as f:
        GroupManager = json.load(f)
        GroupManager[GroupId]["level"] = Level
    with open("ElectricityLoach/GroupManager.json", "w", encoding="utf-8") as f:
        json.dump(GroupManager, f)
        await session.send("添加成功")
