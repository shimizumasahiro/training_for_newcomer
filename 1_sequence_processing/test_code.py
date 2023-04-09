from unittest import TestCase

import code
from numpy.testing import assert_array_almost_equal

class TestCode(TestCase):
  def __init__(self, *args, **kwargs):
    super(TestCode, self).__init__(*args, **kwargs)
    self.fastafile = "data/ATGCCGT.fasta"
  
  def test_base_count(self):
    self.assertEqual(code.base_count(self.fastafile), [1, 2, 2, 2],
                     msg="課題1-1, base_count()の出力が正しくありません。")

  def test_gen_rev_comp_seq(self):
    self.assertEqual(code.gen_rev_comp_seq(self.fastafile), "ACGGCAT",
                     msg="課題1-2, gen_rev_comp_seq()の出力が正しくありません。「逆」「相補」にしていることを確認してください。")

  def test_calc_gc_content(self):
    expected = [0.0, 50.0, 100.0, 100.0, 100.0, 50.0]
    output = code.calc_gc_content(self.fastafile, window=2, step=1)
    self.assertEqual(len(output), len(expected),
                      msg="課題1-3, calc_gc_content()の出力の配列長が異なっています。ループの回数を確認してください。")
    assert_array_almost_equal(output, expected, decimal=2, verbose=True,
                              err_msg="課題1-3, calc_gc_content()の出力が正しくありません。比率をパーセンテージで出力しているかなどを確認してください。")

  def test_search_motif(self):
    expected = set(['R6', 'F5'])
    output = set(code.search_motif(self.fastafile, "CG"))
    self.assertEqual(output, expected,
                     msg="課題1-4, search_motif()の出力が正しくありません。F, Rなどの接頭辞 prefix が間違っていないか確認してください。") 

  def test_translate(self):
    expected = set(['M_', 'MP_', 'MTA_', 'MCR_', 'MRH_', 'MA_', 'MG_'])
    output = set(code.translate(self.fastafile))
    self.assertEqual(output, expected,
                     msg="課題1-5, translate()の出力が正しくありません。コドン表が正しいこと、冒頭と末尾がそれぞれ'M'と','であることを確認してください。")
  
