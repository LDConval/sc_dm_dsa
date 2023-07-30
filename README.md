# sc_dm_dsa

[中文说明](readme.zh.md) | [한국어 지침](readme.ko.md)

Desert Strike: Livestream Version

This repository demonstrates an EUD map designed to stream a Desert Strike tournament while controlled with live comments.

## Usage

- Install Python 3 and the dependencies in ```requirements.txt```
- Enter _Starcraft: Remastered_, start the map ([EN] DS_StreamComments.scx) in LAN and go to an observer slot
- You can use a virtual machine to join the game as human player
- Press ```V``` to lock the camera in game, then adjust the zoom via mouse wheel until the full area is visible
- Run ```python server.py``` to start the server
- Return to StarCraft to continue streaming the game
- Enter the served website (e.g. ```192.168.137.1:1700```) to view the stream and send comments

## Notes

The livestream hosted in this demo is generated with ```pyautogui```'s screenshots, which is inefficient for actual streaming.

Please use an actual streaming software like OBS in production, and refer to APIs of streaming platforms for accessing live comments.
