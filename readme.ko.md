# sc_dm_dsa

데저트 스트라이크 라이브 스트림 버전

이 저장소는 라이브 코멘트로 제어되는 동안 Desert Strike 토너먼트를 스트리밍하도록 설계된 EUD 맵을 보여줍니다.

## 사용 방법

- 먼저 Python 3과 ```requirements.txt```에 종속성을 설치합니다.
- [OBS Studio](https://obsproject.com/download)와 [smart_rtmpd](https://github.com/superconvert/smart_rtmpd)를 설치하여 스타크래프트 스트리밍을 설정합니다(HTTP 포트 8080).
- OBS에서 ```server = rtmp://<귀하의 IP>:1935/live``` 및 ```stream_key = starcraft```를 설정하세요.
- 스타크래프트에 들어가 LAN에서 지도([EN] DS_StreamComments.scx)를 시작하고 관찰자 슬롯으로 이동합니다.
- ```V```를 눌러 게임에서 카메라를 잠근 다음 전체 영역이 보일 때까지 마우스 휠을 통해 확대/축소를 조정합니다.
- ```python server.py```를 실행하여 서버를 시작합니다.
- 스타크래프트로 돌아가 게임 스트리밍을 계속하세요
- 제공된 웹 사이트(예: ```192.168.137.1:1700```)를 다른 클라이언트와 함께 입력하여 스트림을 보고 댓글을 보냅니다.

## 메모

여기의 라이브 스트리밍 서비스는 데모용으로만 사용됩니다.

스트리밍 플랫폼에서 사용하려면 라이브 댓글에 액세스하기 위해 해당 API를 참조하십시오.
