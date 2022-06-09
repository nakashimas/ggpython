# -*- coding: utf-8 -*-
# =============================================================================>
# ##############################################################################
# ## 
# ## core.py
# ## 
# ##############################################################################
# =============================================================================>
# imports default

# =============================================================================>
# imports third party

# =============================================================================>
# imports local
try:
    from .tracker import *
    from .utils import *
except Exception as _:
    from tracker import *
    from utils import *

# =============================================================================>
# GGAPI class

class _const:
    """_const

    It is super class of ConstantClass 

    Raises:
        self.ConstError: If you edit a uneditable variable.
    """
    class ConstError(TypeError):
        def __init__(self, name):
            super().__init__("Can't rebind const (%s)" % name)
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError(name)
        else:
            self.__dict__[name] = value


class GAME(_const):
    """GAME
    Args:
        _const (_type_): _description_
    """
    FORTNITE = None
    VALORANT = ValorantTrackerWebsiteAPI
    APEX_LEGENDS = None
    DESTINY_TWO = None
    CALL_OF_DUTY = None
    RAINBOW_SIX = None
    LEAGUE_OF_LEGENDS = None
    HALO_INFINITE = None


class GGTrackerAPI:
    """GGTrackerAPI
    """
    def __init__(self, game):
        """ __init__ """
        if isinstance(game, WebsiteAPI):
            self.tracker = self._get_tracker_api_object(game)
    
    @classmethod
    def _get_tracker_api_class(cls, game):
        pass


if __name__ == "__main__":
    pass