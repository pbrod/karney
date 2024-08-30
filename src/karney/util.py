"""
Utility module
==============

"""
from __future__ import division, print_function
from collections import namedtuple
import numpy as np
from numpy import rad2deg, deg2rad
from karney._common import test_docstrings, _make_summary

__all__ = ["deg", "rad", "nthroot", "get_ellipsoid",
           "eccentricity2", "polar_radius", "third_flattening"]

FINFO = np.finfo(float)
_tiny_name = "tiny" if np.__version__ < "1.22" else "smallest_normal"
TINY = getattr(FINFO, _tiny_name)
EPS = FINFO.eps  # machine precision (machine epsilon)

Ellipsoid = namedtuple("Ellipsoid", "a f name")


ELLIPSOID = {
    1: Ellipsoid(a=6377563.3960, f=1.0 / 299.3249646, name="Airy 1858"),
    2: Ellipsoid(a=6377340.189, f=1.0 / 299.3249646, name="Airy Modified"),
    3: Ellipsoid(a=6378160.0, f=1.0 / 298.25, name="Australian National"),
    4: Ellipsoid(a=6377397.155, f=1.0 / 299.1528128, name="Bessel 1841"),
    5: Ellipsoid(a=6378249.145, f=1.0 / 293.465, name="Clarke 1880"),
    6: Ellipsoid(a=6377276.345, f=1.0 / 300.8017, name="Everest 1830"),
    7: Ellipsoid(a=6377304.063, f=1.0 / 300.8017, name="Everest Modified"),
    8: Ellipsoid(a=6378166.0, f=1.0 / 298.3, name="Fisher 1960"),
    9: Ellipsoid(a=6378150.0, f=1.0 / 298.3, name="Fisher 1968"),
    10: Ellipsoid(a=6378270.0, f=1.0 / 297, name="Hough 1956"),
    11: Ellipsoid(a=6378388.0, f=1.0 / 297,
                  name="Hayford/International ellipsoid 1924/European Datum 1950/ED50"),
    12: Ellipsoid(a=6378245.0, f=1.0 / 298.3, name="Krassovsky 1938"),
    13: Ellipsoid(a=6378145.0, f=1.0 / 298.25, name="NWL-9D / WGS 66"),
    14: Ellipsoid(a=6378160.0, f=1.0 / 298.25, name="South American 1969 / SAD69"),
    15: Ellipsoid(a=6378136.0, f=1.0 / 298.257, name="Soviet Geod. System 1985"),
    16: Ellipsoid(a=6378135.0, f=1.0 / 298.26, name="WGS 72"),
    17: Ellipsoid(a=6378206.4, f=1.0 / 294.9786982138, name="Clarke 1866 / NAD27"),
    18: Ellipsoid(a=6378137.0, f=1.0 / 298.257223563, name="GRS80 / WGS84 / NAD83"),
    19: Ellipsoid(a=6378137.0, f=298.257222101, name="ETRS89 / EUREF89"),
    20: Ellipsoid(a=6377492.0176, f=1/299.15281285, name="NGO1948")
}
ELLIPSOID_IX = {"airy1858": 1,
                "airymodified": 2,
                "australiannational": 3,
                "bessel": 4,
                "bessel1841": 4,
                "clarke1880": 5,
                "everest1830": 6,
                "everestmodified": 7,
                "fisher1960": 8,
                "fisher1968": 9,
                "hough1956": 10,
                "hough": 10,
                "hayford": 11,
                "international": 11,
                "internationalellipsoid1924": 11,
                "europeandatum1950": 11,
                "ed50": 11,
                "krassovsky": 12,
                "krassovsky1938": 12,
                "nwl-9d": 13,
                "wgs66": 13,
                "southamerican1969": 14,
                "sad69": 14,
                "sovietgeod.system1985": 15,
                "wgs72": 16,
                "clarke1866": 17,
                "nad27": 17,
                "grs80": 18,
                "wgs84": 18,
                "nad83": 18,
                "euref89": 19,
                "etrs89": 19,
                "ngo1948": 20
                }


def eccentricity2(f):
    """Returns the first and second eccentricity squared given the flattening, f.

    Parameters
    ----------
    f : array-like
        Flattening of the ellipsoid

    Notes
    -----
    The (first) eccentricity squared is defined as e2 = f*(2-f).
    The second eccentricity squared is defined as e2m = e2 / (1 - e2).
    """
    e2 = (2.0 - f) * f  # = 1-b**2/a**
    e2m = e2 / (1.0 - e2)
    return e2, e2m


def polar_radius(a, f):
    """Returns the polar radius b given the equatorial radius a and flattening f of the ellipsoid.

    Parameters
    ----------
    a : array-like
        Semi-major half axis or equatorial radius of ellipsoid
    f : array-like
        Flattening of the ellipsoid

    Notes
    -----
    The semi minor half axis (polar radius) is defined as b = (1 - f) * a
    where a is the semi major half axis (equatorial radius) and f is the flattening
    of the ellipsoid.

    """
    b = a * (1.0 - f)
    return b


def third_flattening(f):
    """Returns the third flattening, n, given the flattening, f.

    Parameters
    ----------
    f : array-like
        Flattening of the ellipsoid

    Notes
    -----
    The third flattening is defined as n = f / (2 - f).
    """

    return f / (2.0 - f)


def deg(*rad_angles):
    """
    Converts angle in radians to degrees.

    Parameters
    ----------
    rad_angles:
        angle in radians

    Returns
    -------
    deg_angles:
        angle in degrees

    Examples
    --------
    >>> import numpy as np
    >>> from karney.util import deg
    >>> deg(np.pi/2)
    90.0
    >>> deg(np.pi/2, [0, np.pi])
    (90.0, array([  0., 180.]))

    See also
    --------
    rad
    """
    if len(rad_angles) == 1:
        return rad2deg(rad_angles[0])
    return tuple(rad2deg(angle) for angle in rad_angles)


def rad(*deg_angles):
    """
    Converts angle in degrees to radians.

    Parameters
    ----------
    deg_angles:
        angle in degrees

    Returns
    -------
    rad_angles:
        angle in radians

    Examples
    --------
    >>> import numpy as np
    >>> from karney.util import deg, rad
    >>> deg(rad(90))
    90.0
    >>> deg(*rad(90, [0, 180]))
    (90.0, array([  0., 180.]))

    See also
    --------
    deg
    """
    if len(deg_angles) == 1:
        return deg2rad(deg_angles[0])
    return tuple(deg2rad(angle) for angle in deg_angles)


def nthroot(x, n):
    """
    Returns the n'th root of x to machine precision

    Parameters
    ----------
    x : real scalar or numpy array
    n : scalar integer

    Examples
    --------
    >>> import numpy as np
    >>> from karney.util import nthroot
    >>> np.allclose(nthroot(27.0, 3), 3.0)
    True

    """
    shape = np.shape(x)
    x = np.atleast_1d(x)
    y = x**(1. / n)
    mask = (x != 0) & (EPS * np.abs(x) < 1)
    ym = y[mask]
    y[mask] -= (ym**n - x[mask]) / (n * ym**(n - 1))
    if shape == ():
        return y[()]
    return y


def get_ellipsoid(name):
    """
    Returns semi-major axis (a), flattening (f) and name of reference ellipsoid as a named tuple.

    Parameters
    ----------
    name : string
        name of ellipsoid. Valid options are:
        1) Airy 1858
        2) Airy Modified
        3) Australian National
        4) Bessel 1841
        5) Clarke 1880
        6) Everest 1830
        7) Everest Modified
        8) Fisher 1960
        9) Fisher 1968
        10) Hough 1956
        11) Hayford / International ellipsoid 1924 / European Datum 1950 / ED50
        12) Krassovsky 1938
        13) NWL-9D / WGS 66
        14) South American 1969
        15) Soviet Geod. System 1985
        16) WGS 72
        17) Clarke 1866 / NAD27
        18) GRS80 / WGS84 / NAD83
        19) ETRS89 / EUREF89
        20) NGO1948

    Notes
    -----
    See also:
    https://en.wikipedia.org/wiki/Geodetic_datum
    https://en.wikipedia.org/wiki/Reference_ellipsoid


    Examples
    --------
    >>> from karney.util import get_ellipsoid
    >>> get_ellipsoid(name="wgs84")
    Ellipsoid(a=6378137.0, f=0.0033528106647474805, name="GRS80 / WGS84 / NAD83")
    >>> get_ellipsoid(name="GRS80")
    Ellipsoid(a=6378137.0, f=0.0033528106647474805, name="GRS80 / WGS84 / NAD83")
    >>> get_ellipsoid(name="NAD83")
    Ellipsoid(a=6378137.0, f=0.0033528106647474805, name="GRS80 / WGS84 / NAD83")
    >>> get_ellipsoid(name=18)
    Ellipsoid(a=6378137.0, f=0.0033528106647474805, name="GRS80 / WGS84 / NAD83")

    >>> wgs72 = get_ellipsoid(name="WGS 72")
    >>> wgs72.a == 6378135.0
    True
    >>> wgs72.f == 0.003352779454167505
    True
    >>> wgs72.name
    'WGS 72'
    >>> wgs72 == (6378135.0, 0.003352779454167505, "WGS 72")
    True
    """
    if isinstance(name, str):
        name = name.lower().replace(" ", "").partition("/")[0]
    ellipsoid_id = ELLIPSOID_IX.get(name, name)

    return ELLIPSOID[ellipsoid_id]


_odict = globals()
__doc__ = (__doc__  # @ReservedAssignment
           + _make_summary(dict((n, _odict[n]) for n in __all__)))


if __name__ == "__main__":
    test_docstrings(__file__)
