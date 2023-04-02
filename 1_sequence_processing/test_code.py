from unittest import TestCase

import code
from numpy.testing import assert_array_almost_equal

class TestCode(TestCase):
  def __init__(self, *args, **kwargs):
    super(TestCode, self).__init__(*args, **kwargs)
    self.fastafile = "data/ATGCCGT.fasta"
  
  def test_base_count(self):
    self.assertEqual(code.base_count(self.fastafile), [1, 2, 2, 2])

  def test_gen_rev_comp_seq(self):
    self.assertEqual(code.gen_rev_comp_seq(self.fastafile), "ACGGCAT")

  def test_calc_gc_content(self):
    expected = [0.0, 50.0, 100.0, 100.0, 100.0, 50.0]
    output = code.calc_gc_content(self.fastafile, window=2, step=1)
    assert_array_almost_equal(output, expected, decimal=2)

  def test_search_motif(self):
    expected = set(['R6', 'F5'])
    output = set(code.search_motif(self.fastafile, "CG"))
    self.assertEqual(output, expected)

  def test_translate(self):
    expected = set(['M_', 'MP_', 'MTA_', 'MCR_', 'MRH_', 'MA_', 'MG_'])
    output = set(code.translate(self.fastafile))
    self.assertEqual(output, expected)
  
