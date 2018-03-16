import enum
from typing import Tuple
MAP_EVENT_ACTIONS = {
    'MOVE UP': False,
    'MOVE DOWN': False,
    'MOVE RIGHT': False,
    'MOVE LEFT': False,
    'USE': False
}
class MapEventActions(enum.Enum):
    MOVE_UP=1
    MOVE_DOWN=1
    MOVE_RIGHT=1
    MOVE_LEFT=1

    # about the Use thing i'm not sure how to handle cleanly here (and I wouldn't, more like would do it as a
    # sepearate part of the state-action transition function
    # )

