Current Structure:

my_sdk/
|
├─ Teams/
│ ├─ **init**.py
│ | └─ teams.py (uses the functions inside resources. ex. - resources/api_web/teams.py via resources/**init**.py)
|
├─ Players/
│ ├─ **init**.py
│ | └─ players.py
|
├─ resources/
│ ├─ **init**.py
| |
│ ├─ api_web/
│ | ├─ teams.py
│ | └─ players.py
| |
│ ├─ api_stats/
│ | ├─ teams.py
| | └─ players.py
|
├─ client.py # NHLClient
└─ **init**.py # exposes NHLClient
