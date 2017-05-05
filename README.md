Idle-Manager
=========

Idle Manager API which handles Idle players for Source Python.


OnClientIdle
--------------

Called when a client is marked as idle.

```python
from idle_manager import OnClientIdle

@OnClientIdle
def on_client_idle(index):
    print("Index '{:d}' is now marked as Idle.".format(index))
```


OnClientBack
--------------

Called when a client is back from being idle.

```python
from idle_manager import OnClientBack

@OnClientBack
def on_client_back(index):
    print("Index '{:d}' is no longer marked as Idle.".format(index))
```


OnClientIdle
--------------

Returns the Client Idle Status for the given Client Index.

```python
from idle_manager import OnClientIdle

from events import Event
from players.helpers import index_from_userid

@Event('player_say')
def player_say(game_event):
    index = index_from_userid(game_event.get_int('userid'))
    print('Idle Status for Index "{:d}": {}'.format(index, IsClientIdle(index)))
```
