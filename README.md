Idle-Manager
=========

Idle Manager API which handles Idle players for Source Python.


OnClientIdle
--------------

Called when a Client is marked as Idle.

```python
from idle_manager import OnClientIdle

@OnClientIdle
def on_client_idle(index):
    print('Index "{:d}" is now marked as Idle.'.format(index))
```


OnClientBack
--------------

Called when a Client is back from being Idle.

```python
from idle_manager import OnClientBack

@OnClientBack
def on_client_back(index):
    print('Index "{:d}" is no longer marked as Idle.'.format(index))
```


is_client_idle(index)
--------------

Returns the Client Idle Status for the given Client Index.

```python
from idle_manager import is_client_idle

from events import Event
from players.helpers import index_from_userid

@Event('player_say')
def player_say(game_event):
    index = index_from_userid(game_event.get_int('userid'))
    print('Idle Status for Index "{:d}": {}'.format(index, is_client_idle(index)))
```


get_client_idle_time(index, timestamp=False)
--------------

Returns the Client Idle Time or Timestamp for the given Client Index.

Returns None if the Client is not Idle.


```python
from idle_manager import get_client_idle_time

from events import Event
from players.helpers import index_from_userid

@Event('player_say')
def player_say(game_event):
    index = index_from_userid(game_event.get_int('userid'))
    print('Idle Time for Index "{:d}": {:d}'.format(index, get_client_idle_time(index)))

@Event('player_jump')
def player_jump(game_event):
    index = index_from_userid(game_event.get_int('userid'))
    print('Idle Timestamp for Index "{:d}": {:d}'.format(index, get_client_idle_time(index, True)))
```
