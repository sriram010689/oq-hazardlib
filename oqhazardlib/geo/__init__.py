# The Hazard Library
# Copyright (C) 2012 GEM Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Package :mod:`oqhazardlib.geo` contains implementations of different
geographical primitives, such as :class:`~oqhazardlib.geo.point.Point`,
:class:`~oqhazardlib.geo.line.Line`
:class:`~oqhazardlib.geo.polygon.Polygon` and
:class:`~oqhazardlib.geo.mesh.Mesh`, as well as different
:mod:`surface <oqhazardlib.geo.surface>` implementations and utility
class :class:`~oqhazardlib.geo.nodalplane.NodalPlane`.
"""
from oqhazardlib.geo.point import Point
from oqhazardlib.geo.line import Line
from oqhazardlib.geo.polygon import Polygon
from oqhazardlib.geo.mesh import Mesh, RectangularMesh
from oqhazardlib.geo.surface import PlanarSurface
from oqhazardlib.geo.surface import SimpleFaultSurface
from oqhazardlib.geo.surface import ComplexFaultSurface
from oqhazardlib.geo.nodalplane import NodalPlane
from oqhazardlib.geo import surface
