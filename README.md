# Introduction to Karney

[![PyPI version](https://badge.fury.io/py/karney.svg)](https://badge.fury.io/py/karney)
[![Documentation](https://readthedocs.org/projects/karney/badge/?svg=true "documentation")](https://karney.readthedocs.io/en/latest/)
[![CI-tests](https://github.com/pbrod/karney/actions/workflows/CI-CD.yml/badge.svg)](https://github.com/pbrod/karney/actions/workflows/CI-CD.yml)


The `karney` library provides native Python implementations of a subset of the C++ library, GeographicLib.
Currently the following operations are implemented:

* Calculate the surface distance between two geographical positions.

* Find the destination point given start point, azimuth/bearing and distance.


All the functions are vectorized and offer speeds comparable to compiled C++ code when operating on arrays.

Some common features of these functions:

Angles (latitude, longitude, azimuth) are measured in degrees or radians.
Distances are measured in meters.
The ellipsoid is specified as [a, f], where a = equatorial radius and f = flattening.
Keep |f| <= 1/50 for full double precision accuracy.


## Installation

```bash
$ pip install karney
```


## Usage

Below the solution to two geodesic problems are given.

### Surface distance
Find the surface distance sAB (i.e. great circle distance) between two
positions A and B. The heights of A and B are ignored, i.e. if they don't have
zero height, we seek the distance between the points that are at the surface of
the Earth, directly above/below A and B.  Use Earth radius 6371e3 m.
Compare the results with exact calculations for the WGS-84 ellipsoid.

In geodesy this is known as "The second geodetic problem" or
"The inverse geodetic problem" for a sphere/ellipsoid.


Solution for a sphere:

    >>> import numpy as np
    >>> from karney.geodesic import rad, sphere_distance_rad, distance

    >>> latlon_a = (88, 0)
    >>> latlon_b = (89, -170)
    >>> latlons = latlon_a + latlon_b
    >>> r_Earth = 6371e3  # m, mean Earth radius
    >>> s_AB = sphere_distance_rad(*rad(latlons))[0]*r_Earth
    >>> s_AB = distance(*latlons, a=r_Earth, f=0, degrees=True)[0] # or alternatively

    >>> 'Ex5: Great circle = {:5.2f} km'.format(s_AB / 1000)
    'Ex5: Great circle = 332.46 km'

Exact solution for the WGS84 ellipsoid:

    >>> s_12, azi1, azi2 = distance(*latlons, degrees=True)
    >>> 'Ellipsoidal distance = {:5.2f} km'.format(s_12 / 1000)
    'Ellipsoidal distance = 333.95 km'

See also
    [Example 5 at www.navlab.net](http://www.navlab.net/nvector/#example_5)


### A and azimuth/distance to B

We have an initial position A, direction of travel given as an azimuth
(bearing) relative to north (clockwise), and finally the
distance to travel along a great circle given as sAB.
Use Earth radius 6371e3 m to find the destination point B.

In geodesy this is known as "The first geodetic problem" or
"The direct geodetic problem" for a sphere.


    >>> import numpy as np
    >>> from karney.geodesic import reckon
    >>> lat, lon = 80, -90
    >>> msg = 'Ex8, Destination: lat, lon = {:4.4f} deg, {:4.4f} deg'

Greatcircle solution:

    >>> lat2, lon2, azi_b = reckon(lat, lon, distance=1000, azimuth=200, a=6371e3, f=0, degrees=True)

    >>> msg.format(lat2, lon2)
    'Ex8, Destination: lat, lon = 79.9915 deg, -90.0177 deg'

    >>> np.allclose(azi_b, -160.0174292682187)
    True

Exact solution:

    >>> lat_b, lon_b, azi_b = reckon(lat, lon, distance=1000, azimuth=200, degrees=True)
    >>> msg.format(lat_b, lon_b)
    'Ex8, Destination: lat, lon = 79.9916 deg, -90.0176 deg'

    >>> np.allclose(azi_b, -160.01742926820506)
    True


See also
    [Example 8 at www.navlab.net](http://www.navlab.net/nvector/#example_8)

	

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`karney` was created by Per A. Brodtkorb and is licensed under the terms of the MIT/X11 license.


## Acknowledgements

The [`karney` package](http://pypi.python.org/pypi/karney/) for
[Python](https://www.python.org/) was written by Per A. Brodtkorb at
[FFI (The Norwegian Defence Research Establishment)](http://www.ffi.no/en>)
based on the [Geographic toolbox](https://github.com/geographiclib/geographiclib-octave)
written by Charles Karney for [Matlab](http://www.mathworks.com) and [GNU Octave](https://octave.org>).
The karney.geodesic module is a vectorized reimplementation of the Matlab/Octave GeographicLib toolbox.

The content is based on the article by [Karney, 2013](https://doi.org/10.1007/s00190-012-0578-z).
Thus this article should be cited in publications using the software.



The `karney` package structure was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
