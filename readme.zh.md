# sc_dm_dsa

沙漠风暴弹幕版

演示通过星际地图EUD，通过各种直播平台的弹幕操作《沙漠风暴》（Desert Strike）对战的功能

## 使用方法

- 先安装Python 3和```requirements.txt```中的依赖库
- 安装[OBS Studio](https://obsproject.com/download)，直播选项中服务器填rtmp://<你的IP>:1935/live，推流码starcraft
- 安装[smart_rtmpd](https://github.com/superconvert/smart_rtmpd)直播服务器，启用HTTP，Port填8080
- 进入《星际争霸：重制版》，用局域网联机（可以用虚拟机双开）打开```[ZH] DS_StreamComments.scx```并进入OB位（下面那4个位置）
- 在游戏内按V键开启锁定屏幕，然后用鼠标滚轮调整画面至整体可见
- 运行```python server.py```开启服务器
- 回到游戏内，把游戏画面打在公屏上
- 用局域网中其他的电脑进入提示的网站（如```192.168.137.1:1700```）即可观看直播、发送弹幕

## 注意

直播功能仅供演示

真实的应用场景中请查阅相关直播平台的API实现读取平台中弹幕的功能
