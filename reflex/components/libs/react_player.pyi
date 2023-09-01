"""Stub file for react_player.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.component import NoSSRComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class ReactPlayerComponent(NoSSRComponent):
    @overload
    @classmethod
    def create(cls, *children, url: Optional[Union[Var[str], str]] = None, playing: Optional[Union[Var[str], str]] = None, loop: Optional[Union[Var[bool], bool]] = None, controls: Optional[Union[Var[bool], bool]] = None, light: Optional[Union[Var[bool], bool]] = None, volume: Optional[Union[Var[float], float]] = None, muted: Optional[Union[Var[bool], bool]] = None, width: Optional[Union[Var[str], str]] = None, height: Optional[Union[Var[str], str]] = None, **props) -> "ReactPlayerComponent": ...  # type: ignore