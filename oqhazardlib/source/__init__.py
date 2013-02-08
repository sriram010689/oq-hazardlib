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
Package :mod:`oqhazardlib.source` deals with various types
of seismic sources.
"""
from oqhazardlib.source.rupture import Rupture, ProbabilisticRupture
from oqhazardlib.source.point import PointSource
from oqhazardlib.source.area import AreaSource
from oqhazardlib.source.simple_fault import SimpleFaultSource
from oqhazardlib.source.complex_fault import ComplexFaultSource
