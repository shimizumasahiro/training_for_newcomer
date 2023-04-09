from unittest import TestCase
import code
import warnings
from numpy.testing import assert_array_almost_equal
from Bio.PDB.PDBExceptions import PDBConstructionWarning

class TestCode(TestCase):
  def __init__(self, *args, **kwargs):
    warnings.simplefilter("ignore", PDBConstructionWarning) # PDBファイルの読み込みで発生する警告を無視する
    super(TestCode, self).__init__(*args, **kwargs)
    self.filepath = "data/1buw.pdb"
    self.chain = "A"
    self.resname = "HEM"

  def __del__(self):
    warnings.resetwarnings()

  def test_calc_chain_center(self):
    expected = [47.02584, 33.32251, 35.561733]
    output = code.calc_chain_center(self.filepath, self.chain)
    assert_array_almost_equal(output, expected, decimal=2,
                              err_msg="課題3-1, calc_chain_center()の出力が正しくありません。水素原子も含めた「中心」を計算してください。（重心ではありません。）")

  def test_calc_residue_center(self):
    expected = [48.400906, 26.63, 30.698982]
    output = code.calc_residue_center(self.filepath, self.chain, self.resname)
    assert_array_almost_equal(output, expected, decimal=2,
                              err_msg="課題3-2, calc_residue_center()の出力が正しくありません。HEMの原子数は43個です。")

  def test_calc_min_distance(self):
    expected = 2.262587668358037
    output = code.calc_min_distance(self.filepath, self.chain, self.resname)
    self.assertAlmostEqual(output, expected, places=2,
                           msg="課題3-3, calc_min_distance()の出力が正しくありません。")