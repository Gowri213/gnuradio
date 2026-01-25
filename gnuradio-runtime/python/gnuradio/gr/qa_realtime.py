#!/usr/bin/env python
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Portions of this file are derived from work by Brett Gottula.

from gnuradio import gr, gr_unittest


class test_realtime(gr_unittest.TestCase):
    def test_000_enable_realtime(self):
        """Ensure this function is callable."""
        try:
            gr.enable_realtime_scheduling()
        except RuntimeError as e:
            self.skipTest(f"Realtime scheduling not permitted: {e}")
            


if __name__ == "__main__":
    gr_unittest.run(test_realtime)
