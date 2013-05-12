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
import unittest

from openquake.hazardlib.scalerel.peer import PeerMSR
from openquake.hazardlib.scalerel.wc1994 import WC1994
from openquake.hazardlib.scalerel.hb2002 import HB2002
from openquake.hazardlib.scalerel.el2003b import EL2003B

class BaseMSRTestCase(unittest.TestCase):
    MSR_CLASS = None

    def setUp(self):
        super(BaseMSRTestCase, self).setUp()
        self.msr = self.MSR_CLASS()

    def _test_get_median_area(self, mag, rake, expected_value):
        self.assertAlmostEqual(self.msr.get_median_area(mag, rake),
                               expected_value)

    def _test_get_area(self, mag, rake, epsilon, expected_value):
        self.assertAlmostEqual(self.msr.get_area(mag, rake, epsilon),
                               expected_value)


class PeerMSRMSRTestCase(BaseMSRTestCase):
    MSR_CLASS = PeerMSR

    def test_median_area(self):
        self._test_get_median_area(4.3, None, 1.9952623)
        self._test_get_median_area(5.1, 0, 12.5892541)

    def test_get_area(self):
        self._test_get_area(4.8, None, -0.5, 4.7315126)
        self._test_get_area(3.4, 0, 0.2, 0.2818383)


class WC1994MSRTestCase(BaseMSRTestCase):
    MSR_CLASS = WC1994

    def test_median_area_all(self):
        self._test_get_median_area(2.2, None, 0.0325087)
        self._test_get_median_area(1.3, None, 0.0049317)

    def test_median_area_strike_slip(self):
        self._test_get_median_area(3.9, -28.22, 1.2302688)
        self._test_get_median_area(3.9, -45, 1.2302688)
        self._test_get_median_area(3.9, 0, 1.2302688)
        self._test_get_median_area(3.9, 45, 1.2302688)

    def test_median_area_thrust(self):
        self._test_get_median_area(4.1, 50, 1.0665961)
        self._test_get_median_area(4.1, 95, 1.0665961)

    def test_median_area_normal(self):
        self._test_get_median_area(5.9, -59, 92.8966387)
        self._test_get_median_area(5.9, -125, 92.8966387)

    def test_get_std_dev_area(self):
        self.assertEqual(self.msr.get_std_dev_area(None, None), 0.24)
        self.assertEqual(self.msr.get_std_dev_area(20, 4), 0.22)
        self.assertEqual(self.msr.get_std_dev_area(None, 138), 0.22)
        self.assertEqual(self.msr.get_std_dev_area(None, -136), 0.22)
        self.assertEqual(self.msr.get_std_dev_area(None, 50), 0.26)
        self.assertEqual(self.msr.get_std_dev_area(None, -130), 0.22)

    def test_get_area(self):
        self._test_get_area(4.8, 50, 0.3, 6.1944108)
        self._test_get_area(5.6, 138, 1.3, 80.5378441)

class HB2002MSRTestCase(BaseMSRTestCase):
    MSR_CLASS = HB2002

    def test_median_area_lesser_mag(self):
        self._test_get_median_area(6.71, 537.03179637)
        self._test_get_median_area(2.31, 0.021379621)

    def test_median_area_greater_mag(self):
        self._test_get_median_area(7.89, 4120.975190973)
        self._test_get_median_area(6.72, 546.386549882)

    def test_get_std_dev_area_lesser_mag(self):
        self.assertEqual(self.msr.get_std_dev_area(6.71), 0.03)
        self.assertEqual(self.msr.get_std_dev_area(5.6), 0.03)
        self.assertEqual(self.msr.get_std_dev_area(4.3), 0.03)
       
    def test_get_std_dev_area_greater_mag(self):
        self.assertEqual(self.msr.get_std_dev_area(6.72), 0.04)
        self.assertEqual(self.msr.get_std_dev_area(7.6), 0.04)
        self.assertEqual(self.msr.get_std_dev_area(7.3), 0.04)

class EL2003BMSRTestCase(BaseMSRTestCase):
    MSR_CLASS = EL2003B

    def test_median_area(self):
        self._test_get_median_area(6.71, 323.59365693)
        self._test_get_median_area(2.31, 0.012882496)

    def test_get_std_dev_area(self):
        self.assertEqual(self.msr.get_std_dev_area(6.71), 0.0)
        self.assertEqual(self.msr.get_std_dev_area(5.6), 0.0)
        self.assertEqual(self.msr.get_std_dev_area(4.3), 0.0)


