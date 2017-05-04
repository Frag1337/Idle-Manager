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
        pass
```


OnClientBack
--------------

Called when a client is back from being idle.

```python

    from idle_manager import OnClientBack

    @OnClientBack
    def on_client_back(index):
        pass
```


IsClientValid
--------------

Returns the Client Idle Status for the given Client Index.

```python

    from idle_manager import IsClientValid

    from events import Event
    from players.helpers import index_from_userid

    @Event('player_jump')
    def player_jump(game_event):
        index = index_from_userid(game_event.get_int('userid'))
        print('Idle Status for Index "{:d}": {}'.format(IsClientValid(index)))

```
