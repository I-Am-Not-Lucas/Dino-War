from typing import Type
from typing import Union


class _SpecialForm:
    __slots__ = ("_name", "__doc__", "_getitem")

    def __init__(self, getitem):
        self._getitem = getitem
        self._name = getitem.__name__
        self.__doc__ = getitem.__doc__

    def __getitem__(self, parameters):
        return self._getitem(self, parameters)


# Types for type-hinting, they cannot be used in casting
@_SpecialForm
def Computed(self, type_: Type):
    """
    The "Computed" type indicates that a variable is the result of internal computation.
    It is not used by any function and effects no change.
    The variable's value is associated with the function soley for reference.

    Example:

    .. code-block:: python

      from dict_tools import typing


      def function(arg1: typing.Computed[str]):
          ...
    """
    return Union[type_, type(None)]


@_SpecialForm
def Sensitive(self, type_: Type):
    """
    The "Sensitive" type indicates that a variable contains data that should be protected from being displayed to users.

    Example:

    .. code-block:: python

      from dict_tools import typing


      def function(arg1: typing.Sensitive[str]):
          ...
    """
    return Union[type_, type(None)]
