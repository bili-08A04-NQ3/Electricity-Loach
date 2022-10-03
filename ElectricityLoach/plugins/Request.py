from nonebot import on_request, RequestSession
from ElectricityLoach.utils.LevelChecker import CanResponse

@on_request('group')
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    if not CanResponse(session, 3):
        return
    if "泥鳅" in session.event.comment:
        # 验证信息正确，同意入群
        await session.approve()
        return
    # 验证信息错误，拒绝入群
    await session.reject('这不对吧')
