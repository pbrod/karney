"""
Karney
------
This library provides native Python implementations of a subset of the C++
library, GeographicLib.

When given a combination of scalar and array inputs, scalar inputs are
automatically expanded to match the array shape.

Documentation:
https://geographiclib.sourceforge.io/doc/library.html
https://github.com/geographiclib/geographiclib-octave


References
----------
C. F. F. Karney, "Algorithms for geodesics",
J. Geodesy 87, 43-55 (2013);
https://doi.org/10.1007/s00190-012-0578-z
"""

from . import _license, geodesic, util

__version__ = "1.1.1"

__all__ = ["__version__", "geodesic", "license", "util"]


if __doc__ is not None:
    sections = [
        __doc__,
        geodesic.__doc__,
        util.__doc__,
        f"License\n-------\n{_license.__doc__}",
    ]
    __doc__ = "\n\n".join(part for part in sections if part is not None)
