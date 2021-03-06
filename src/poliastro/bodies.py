# coding: utf-8
"""Bodies of the Solar System.

Contains some predefined bodies of the Solar System:

* Sun (☉)
* Earth (♁)

and a way to define new bodies (:py:class:`~Body` class).

"""
from astropy.constants import R_earth
from astropy import units as u


class Body(object):
    """Class to represent a body of the Solar System.

    """
    @u.quantity_input(k=u.m ** 3 / u.s ** 2, R=u.m)
    def __init__(self, k, name=None, symbol=None, R=0 * u.km):
        """Constructor.

        Parameters
        ----------
        k : Quantity
            Standard gravitational parameter
        name : str, optional
            Name of the body, default to None.
        symbol : str, optional
            Symbol for the body, default to None.
        R : Quantity, optional
            Radius of the body, default to 0 km.

        """
        self.k = k
        self.name = name
        self.symbol = symbol
        self.R = R

    def __str__(self):
        return u"{0} ({1})".format(self.name, self.symbol)

    def _repr_latex_(self):
        """Creates a LaTeX representation.

        Used by the IPython notebook.

        """
        return self.__str__()


Sun = Body(k=132712440018 * u.km ** 3 / u.s ** 2,
           name="Sun", symbol=u"\u2609")
Earth = Body(k=398600 * u.km ** 3 / u.s ** 2,
             name="Earth", symbol=u"\u2641", R=R_earth.to(u.km))
