# ../idle_manager/idle_manager.py

"""Package that detects idle players."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from config.manager import ConfigManager
from listeners import OnClientActive
from listeners import OnClientDisconnect
from listeners import OnButtonStateChanged
from listeners import OnClientSettingsChanged
from commands.say import SayFilter
from commands.client import ClientCommandFilter
from commands.server import ServerCommand
from filters.players import PlayerIter
from listeners.tick import Delay
from listeners import ListenerManager
from listeners import ListenerManagerDecorator


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store all timers
_timers = dict()

# Store all players
_players = dict()


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
class OnClientIdle(ListenerManagerDecorator):
    """Register/unregister a ClientIdle listener."""
 
    manager = ListenerManager()


class OnClientBack(ListenerManagerDecorator):
    """Register/unregister a ClientBack listener."""

    manager = ListenerManager()


# =============================================================================
# >> CONFIGURATION
# =============================================================================
# Create the config file
with ConfigManager('idle_manager', 'idle_') as config:

    # Create the time convar
    idle_time = config.cvar(name='time', 
                            default=60.0, 
                            description='The Time before a Client is marked as Idle.'
                            )


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def load():
    # Late Loading
    for player in PlayerIter():
        on_client_active(player.index)


@OnClientActive
def on_client_active(index):
    _players[index] = False

    ResetIdleTimer(index)


@OnClientDisconnect
def on_client_disconnect(index):
    if index in _timers:
        if _timers[index].running:
            _timers[index].cancel()
        del _timers[index]

    if index in _players:
        del _players[index]


@OnButtonStateChanged
def on_button_state_changed(player, old_buttons, new_buttons):
    ResetIdleTimer(player.index)


@OnClientSettingsChanged
def on_client_settings_changed(index):
    ResetIdleTimer(index)


@SayFilter
def say_filter(command, index, team_only):
    ResetIdleTimer(index)


@ClientCommandFilter
def client_command_filter(command, index):
    ResetIdleTimer(index)


def ResetIdleTimer(index):
    # Reset Idle Timers
    if index in _timers and _timers[index].running:
        _timers[index].cancel()

    if _players[index]:
        # Client is back from being idle
        _players[index] = False

        # Notify
        OnClientBack.manager.notify(index)

    _timers[index] = Delay(idle_time.get_int(), SetIdle, (index,))


def SetIdle(index):
    # Client is now idle
    _players[index] = True

    # Notify
    OnClientIdle.manager.notify(index)


def IsClientIdle(index):
    """
    Returns the Client Idle Status for the given Client Index.

    :param int index: The Client Index to check for.
    :rtype: bool
    """
    if index in _players:
        return bool(_players[index])
    else:
        raise ValueError('Invalid Client Index. (:d)'.format(index))
