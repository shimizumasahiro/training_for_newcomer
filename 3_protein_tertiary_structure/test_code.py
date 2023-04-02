from unittest import TestCase

import code
from numpy.testing import assert_array_almost_equal

class TestCode(TestCase):
  def __init__(self, *args, **kwargs):
    super(TestCode, self).__init__(*args, **kwargs)
    self.filepath = "data/1buw.pdb"
    self.chain = "A"
    self.resname = "HEM"

  def test_calc_chain_center(self):
    expected = [47.02584, 33.32251, 35.561733]
    output = code.calc_chain_center(self.filepath, self.chain)
    assert_array_almost_equal(output, expected, decimal=2)

  def test_calc_residue_center(self):
    expected = [48.400906, 26.63, 30.698982]
    output = code.calc_residue_center(self.filepath, self.chain, self.resname)
    assert_array_almost_equal(output, expected, decimal=2)

  def test_calc_min_distance(self):
    expected = 2.262587668358037
    output = code.calc_min_distance(self.filepath, self.chain, self.resname)
    self.assertAlmostEqual(output, expected, places=2)