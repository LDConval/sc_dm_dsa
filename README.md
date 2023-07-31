# sc_dm_dsa

[中文说明](readme.zh.md) | [한국어 지침](readme.ko.md)

Desert Strike: Livestream Version

This repository demonstrates an EUD map designed to stream a Desert Strike tournament controlled by live comments.

## Usage

- Install Python 3 and the dependencies in ```requirements.txt```
- Install [OBS Studio](https://obsproject.com/download) and [smart_rtmpd](https://github.com/superconvert/smart_rtmpd) to setup streaming for Starcraft (HTTP Port 8080)
- Please set ```server = rtmp://<your ip>:1935/live``` and ```stream_key = starcraft``` in OBS
- Enter __Starcraft: Remastered__, start the map ([EN] DS_StreamComments.scx) in LAN and go to an observer slot
- You can use a virtual machine to join the game as human player
- Press ```V``` to lock the camera in game, then adjust the zoom via mouse wheel until the full area is visible
- Run ```python server.py``` to start the server
- Return to StarCraft to continue streaming the game
- Enter the served website (e.g. ```192.168.137.1:1700```) to view the stream and send comments

## Notes

The livestreaming service here is only for demonstration purposes.

For use in real streaming platforms, please refer to corresponding API for accessing live comments.
