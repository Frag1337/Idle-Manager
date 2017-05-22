# ../idle_manager/idle_manager.py

"""Custom Package that detects idle players."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from time import time as timestamp

# Source.Python
from players.dictionary import PlayerDictionary
from config.manager import ConfigManager
from listeners import OnClientActive
from listeners import OnButtonStateChanged
from commands.say import SayFilter
from commands.client import ClientCommandFilter
from commands.server import ServerCommand
from filters.players import PlayerIter
from players.entity import Player
from listeners import ListenerManager
from listeners import ListenerManagerDecorator


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store all timers
_timers = PlayerDictionary(lambda index: None)

# Store all players
_players = PlayerDictionary(lambda index: None)


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
    # Initiate Player
    _players[index] = {'status': False, 'timestamp': None}

    # Set Idle Timer
    reset_client_idle_timer(index)


@OnButtonStateChanged
def on_button_state_changed(player, old_buttons, new_buttons):
    # Reset Idle Timer
    reset_client_idle_timer(player.index)


@SayFilter
def say_filter(command, index, team_only):
    # Reset Idle Timer
    reset_client_idle_timer(index)


@ClientCommandFilter
def client_command_filter(command, index):
    # Reset Idle Timer
    reset_client_idle_timer(index)


def reset_client_idle_timer(index):
    # Reset Idle Timers
    if index in _timers and _timers[index].running:
        _timers[index].cancel()

    if index in _players and _players[index]['status']:
        # Client is back from being Idle
        _players[index] = {'status': False, 'timestamp': None}

        # Notify
        OnClientBack.manager.notify(index)

    _timers[index] = Player(index).delay(idle_time.get_int(), set_client_idle, (index,))


def set_client_idle(index):
    # Client is now Idle
    _players[index] = {'status': True, 'timestamp': timestamp()}

    # Notify
    OnClientIdle.manager.notify(index)


def is_client_idle(index):
    """
    Returns the Client Idle Status for the given Client Index.

    :param int index: The Client Index to check for.
    :rtype: bool
    """
    if index in _players:
        return bool(_players[index]['status'])
    else:
        raise ValueError('Invalid Client Index. (:d)'.format(index))


def get_client_idle_time(index, timestamp=False):
    """
    Returns the Client Idle Time for the given Client Index.

    :param int index: The Client Index to check for.
    :param bool timestamp: Bool if the Idle Timestamp should be returned.
    :rtype: float
    """
    if index in _players:
        if _players[index]['status']:
            if timestamp:
                return float(_players[index]['timestamp'])
            else:
                return float(timestamp() - _players[index]['timestamp'])
        else:
            return None
    else:
        raise ValueError('Invalid Client Index. (:d)'.format(index))
