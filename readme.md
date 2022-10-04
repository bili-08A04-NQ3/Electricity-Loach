# \电子泥鳅/
## 基于[nonebot](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的qq机器人
## 命令列表
### Player
- 命令: 玩家 <Name\>
- 返回: 玩家名称的一些信息
### Manager
- 命令: group add <id\> <level\>
- 配置群等级,id为群号,level取值如下
0: 没得回复
1: 关键词回复(默认)
2: 命令回复
3: 群管活动
4: 肆意妄为
### weather
- 命令: 天气 城市
- 返回: 城市当天的天气预报
## ElectricityLoach目录下,有几个配置文件
### CompleteReplyWords.json
- 完全匹配回复
- key: str
- value: list
### MatchReplyWords.json
- 模糊匹配回复
- key: str
- value: list
###GroupManager.json
- 群等级的管理数据储存,不用管
