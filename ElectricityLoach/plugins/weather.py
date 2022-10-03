import random
import time

import requests
from nonebot import on_command, CommandSession

from ElectricityLoach.utils.CoolDownData import reset
from ElectricityLoach.utils.LevelChecker import CanResponse

@on_command('weather', aliases=('天气', '天气预报', '查天气'), only_to_me=False)
async def GetWeather(session: CommandSession):
    if not CanResponse(session, 2):
        return
    Rd = session.current_arg_text.strip().split(" ")
    City = Rd[0]
    Days = 0
    if len(Rd) == 2:
        Days = int(Rd[1])
    # https://api.seniverse.com/v3/weather/daily.json?key=S6JOK9adH4c36m7wx&location=shanghai&language=zh-Hans&unit=c&start=-1&days=5
    WeatherData = requests.get("https://api.seniverse.com/v3/weather/daily.json?key=S6JOK9adH4c36m7wx&location="
                               + City +
                               "&language=zh-Hans&unit=c&start=-1&days=8").json()
    if not reset("Weather"):
        return
    if Days >= 2:
        await session.send("过远的日期")
    try:
        Timezone_Offset = WeatherData["results"][0]["location"]["timezone_offset"]
        TodayWeather = WeatherData["results"][0]["daily"]
        i = TodayWeather[Days]
        Date = i["date"]  # 2022-09-18
        TextDay = i["text_day"]  # 多云
        TextNight = i["text_night"]  # 晴
        MaxTemperature = i["high"]  # 27
        MinTemperature = i["low"]  # 22
        RainFall = i["rainfall"]  # 0.00 降水量
        Precip = i["precip"]  # 0.00 降水概率
        WindDirection = i["wind_direction"]  # 北
        WindSpeed = i["wind_speed"]  # 23.4
        WindScale = i["wind_scale"]  # 4 风力等级
        Humidity = i["humidity"]  # 42 相对湿度
        Result = "泥鳅牌天气预报\n城市:" + City + ",日期:" + Date + "(UTC " + Timezone_Offset + ")\n"
        Result += "白天" + TextDay + ",夜晚" + TextNight + "\n"
        Result += "当日最高温度:" + MaxTemperature + ",最低温度:" + MinTemperature + "\n"
        Result += "当日降水量:" + RainFall + ",降水概率:" + Precip + "\n"
        Result += "风向:" + WindDirection + ",风速:" + WindSpeed + "风速等级:" + WindScale + "\n"
        Result += "湿度:" + Humidity
        time.sleep(random.randint(2, 5))
        await session.send(Result)
    except:
        await session.send("获取失败:api返回值:" + str(WeatherData))
