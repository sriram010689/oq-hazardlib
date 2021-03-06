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

from openquake.hazardlib.scalerel.wc1994 import WC1994
from openquake.hazardlib.scalerel.hb2002 import HB2002
from openquake.hazardlib.scalerel.el2003b import EL2003B


class WC1994ASRTestCase(unittest.TestCase):

    def setUp(self):
        self.asr = WC1994()

    def test_get_std_dev_mag(self):
        self.assertEqual(self.asr.get_std_dev_mag(None), 0.24)
        self.assertEqual(self.asr.get_std_dev_mag(20), 0.23)
        self.assertEqual(self.asr.get_std_dev_mag(138), 0.23)
        self.assertEqual(self.asr.get_std_dev_mag(-136), 0.23)
        self.assertEqual(self.asr.get_std_dev_mag(50), 0.25)
        self.assertEqual(self.asr.get_std_dev_mag(-130), 0.25)

    def test_get_median_mag(self):
        self.assertAlmostEqual(self.asr.get_median_mag(50, None), 5.7349906)
        self.assertAlmostEqual(self.asr.get_median_mag(500, 20), 6.7329494)
        self.assertAlmostEqual(self.asr.get_median_mag(500, 138), 6.7329494)
        self.assertAlmostEqual(self.asr.get_median_mag(500, -136), 6.7329494)
        self.assertAlmostEqual(self.asr.get_median_mag(700, 50), 6.8905882)
        self.assertAlmostEqual(self.asr.get_median_mag(800, -130), 6.8911518)

    def test_get_mag(self):
        self.assertAlmostEqual(self.asr.get_mag(100, 45, 0.4), 6.1120000)
        self.assertAlmostEqual(self.asr.get_mag(500, None, 1.3), 7.0269906)

class HB2002ASRTestCase(unittest.TestCase):

    def setUp(self):
        self.asr = HB2002()

    def test_get_std_dev_mag(self):
        self.assertEqual(self.asr.get_std_dev_mag(100), 0.03)
        self.assertEqual(self.asr.get_std_dev_mag(200), 0.03)
        self.assertEqual(self.asr.get_std_dev_mag(300), 0.03)
        self.assertEqual(self.asr.get_std_dev_mag(537), 0.03)
        self.assertEqual(self.asr.get_std_dev_mag(600), 0.04)
        self.assertEqual(self.asr.get_std_dev_mag(700), 0.04)

    def test_get_median_mag(self):
        self.assertAlmostEqual(self.asr.get_median_mag(100, 90), 5.98)
        self.assertAlmostEqual(self.asr.get_median_mag(200, 180), 6.281029996)
        self.assertAlmostEqual(self.asr.get_median_mag(300, -90), 6.457121255)
        self.assertAlmostEqual(self.asr.get_median_mag(537, 30), 6.709974286)
        self.assertAlmostEqual(self.asr.get_median_mag(600, 45), 6.774201667)
        self.assertAlmostEqual(self.asr.get_median_mag(700, 50), 6.863464053)

class EL2003BASRTestCase(unittest.TestCase):

    def setUp(self):
        self.asr = EL2003B()

    def test_get_std_dev_mag(self):
        self.assertEqual(self.asr.get_std_dev_mag(100), 0.1)
        self.assertEqual(self.asr.get_std_dev_mag(200), 0.1)
        self.assertEqual(self.asr.get_std_dev_mag(300), 0.1)
        self.assertEqual(self.asr.get_std_dev_mag(537), 0.1)
        self.assertEqual(self.asr.get_std_dev_mag(600), 0.1)
        self.assertEqual(self.asr.get_std_dev_mag(700), 0.1)

    def test_get_median_mag(self):
        self.assertAlmostEqual(self.asr.get_median_mag(100, 10), 6.2)
        self.assertAlmostEqual(self.asr.get_median_mag(200, 20), 6.501029996)
        self.assertAlmostEqual(self.asr.get_median_mag(300, 50), 6.677121255)
        self.assertAlmostEqual(self.asr.get_median_mag(537, -50), 6.929974286)
        self.assertAlmostEqual(self.asr.get_median_mag(600, -60), 6.97815125)
        self.assertAlmostEqual(self.asr.get_median_mag(700, -90), 7.04509804)
