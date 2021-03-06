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
Module :mod:`openquake.hazardlib.scalerel.hb2002` implements :class:`HB2002`.
"""
from math import log10
from openquake.hazardlib.scalerel.base import BaseMSR, BaseASR


class HB2002(BaseMSR, BaseASR):
    """
	   Hank & Bakun (2002 & 2008, Bull. Seism. Soc. Am.)
	Mag = 3.98+log(Area) +- 0.03 (if Area <= 537)
	Mag = 3.07+(4/3)*log(Area) +- 0.04 (if Area > 537)
	These equations are inverted to get Area from Mag
	No uncertainty estimates given
    """
    def get_median_area(self, mag, rake):
        """
        The values are conditional of magnitude value

       
        """
        assert mag is 6.71 < mag or mag <= 6.71
        if mag <= 6.71:
            # Mag = 3.98+log(Area) +- 0.03 (if Area <= 537)
            return 10.0 ** (-3.98 + mag)
        else:
            # Mag = 3.07+(4/3)*log(Area) +- 0.04 (if Area > 537)
            return 10.0 ** (0.75 * (-3.07 +  mag))

    def get_std_dev_area(self, mag):
        """
        Standard deviation for HB2002. Magnitude is ignored.
        """
        assert mag is mag <= 6.71 or 6.71 < mag 
        if mag <= 6.71:
            # Mag = 3.98+log(Area) +- 0.03 (if Area <= 537)
            return 0.03
        else:
            # Mag = 3.07+(4/3)*log(Area) +- 0.04 (if Area > 537)
            return 0.04

    def get_std_dev_mag(self, area):
        """
        Standard deviation on the magnitude for the HB2002 area relation.

	while the WC1994 requires rake as the input, HB2002 requires area... !??!
        """
        assert area is area <= 537 or 537 < area 
        if area <= 537:
            # Mag = 3.98+-0.03 +log(Area) (if Area <= 537)
            return 0.03
        else:
            # Mag = 3.07+-0.04 +(4/3)*log(Area) (if Area > 537)
            return 0.04


    def get_median_mag(self, area, rake):
        """
        Return magnitude (Mw) given the area.

        :param area:
            Area in square km.

        """
        assert area is area <= 537 or 537 < area 
        if area <= 537:
            # Mag = 3.98+log(Area) (if Area <= 537)
            return 3.98 + 1.00 * log10(area)
        else:
            # Mag = 3.07+(4/3)*log(Area) (if Area > 537)
            return 3.07 + (4/3) * log10(area)
