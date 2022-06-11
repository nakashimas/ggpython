# -*- coding: utf-8 -*-
# =============================================================================>
# ##############################################################################
# ## 
# ## core.py
# ## 
# ##############################################################################
# =============================================================================>
# Definition

SILENCE_MODE = False

# =============================================================================>
# imports default
import warnings
import inspect

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
    NOGAME = "no_game"
    FORTNITE = "fortnite"
    VALORANT = "valorant"
    APEX_LEGENDS = "apex_legends"
    DESTINY_TWO = "distiny_2"
    CALL_OF_DUTY = "call_of_duty"
    RAINBOW_SIX = "rainbow_6"
    LEAGUE_OF_LEGENDS = "league_of_legends"
    HALO_INFINITE = "halo_infinite"


class GGTrackerError(Exception):
    pass


class GGTrackerAPI:
    """GGTrackerAPI
    """
    # =========================================================================>
    # Default
    def __init__(self, game = GAME.NOGAME):
        """ __init__ """
        self._print_info("Initialize " + str(self), mode = "i")
        self.game = game
        self.tracker = None
        self._init_tracker()
    
    def __enter__(self):
        """ __enter__ """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ __exit__ """
        self._print_info("Quit GGTrackerAPI", mode = "i")
        try:
            self.tracker.quit()
        except Exception as e:
            print("_____", "close error")
    
    def __str__(self):
        """ __str__ """
        if self.tracker is None:
            return "GGTrackerAPI"
        else:
            return "GGTrackerAPI with " + str(self.tracker)
    
    def __getattr__(self, name):
        """__getattr__

        Discription:
            Wrapping tracker object
        
        Args:
            name (str): attribute name

        Returns:
            obj: attribute
        """
        if (not name.startswith("_")) and (not name.startswith("game")) and (not name.startswith("tracker")):
            attr_value = getattr(self.tracker, name)
            if callable(attr_value):
                self._print_info("Touch " + str(self.tracker) + " info", mode = "i")
                return attr_value
    
    # =========================================================================>
    # Class Method
    @classmethod
    def _print_info(cls, message, mode = "i"):
        """_print_info

        Args:
            message (str): printing message
            mode (str, optional): 'i' or 'w' or 'e'. Defaults to "i".

        Raises:
            GGTrackerError: some of error
        """
        if not SILENCE_MODE:
            if mode == "i":
                message = "INFO: " + message
                print(message)
            elif mode == "w":
                message = "WARN: " + message
                print(message)
                warnings.warn("", FutureWarning, stacklevel=4)
            elif mode == "e":
                message = "ERRR: " + message
                print(message)
                raise GGTrackerError()

    # =========================================================================>
    # SetGet
    @property
    def tracker(self):
        """ get tracker """
        return self.__tracker
    
    @tracker.setter
    def tracker(self, t):
        """ set tracker """
        self.__tracker = t
    
    @property
    def game(self):
        """ get game """
        return self.__game
    
    @game.setter
    def game(self, g):
        """ set game """
        self.__game = g
    
    # =========================================================================>
    # Utils
    def _init_tracker(self):
        """ _init_tracker """
        if self.game == GAME.NOGAME:
            self.tracker = WebsiteAPI()
        elif self.game == GAME.VALORANT:
            self.tracker = ValorantTrackerWebsiteAPI()
        else:
            self._print_info("this game tracker is not working in now version", mode = "w")
            self.tracker = WebsiteAPI() # not yet


if __name__ == "__main__":
    pass