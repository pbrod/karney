"""
Karney
------

This library provides native Python implementations of a subset of the C++ library, GeographicLib.

When given a combination of scalar and array inputs, the scalar inputs
are automatically expanded to match the shape of the arrays.

Full documentation is available at:
https://geographiclib.sourceforge.io/doc/library.html
https://github.com/geographiclib/geographiclib-octave


References
----------
C. F. F. Karney, "Algorithms for geodesics",
J. Geodesy 87, 43-55 (2013);
https://doi.org/10.1007/s00190-012-0578-z

"""
from importlib.metadata import version
from . import geodesic, util, license
__version__ = version("karney")  # read version from installed package

__doc__ = (__doc__
           + geodesic.__doc__
           + util.__doc__
           + 'License\n-------\n'
           + license.__doc__)



