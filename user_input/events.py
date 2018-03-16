import enum
from typing import Tuple
MAP_EVENT_ACTIONS = {
    'MOVE UP': False,
    'MOVE DOWN': False,
    'MOVE RIGHT': False,
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
def change_position(action: MapEventActions, x: int, y: int)-> Tuple[int,int]:
    if action==MapEventActions.MOVE_UP:
        return (x+1,y)
    if action==MapEventActions.MOVE_DOWN:
        return (x-1,y)
    if action==MapEventActions.MOVE_LEFT:
        return (x,y-1)
    if action==MapEventActions.MOVE_RIGHT:
        return (x,y+1)




