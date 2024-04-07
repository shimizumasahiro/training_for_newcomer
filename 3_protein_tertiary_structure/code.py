from typing import List, Union
import numpy.typing as npt
import numpy as np
import pymol
from pymol import cmd
from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1
pymol.finish_launching(['pymol', '-c'])

def get_amino_acid_sequence(pdb_file, chain_id):
    parser = PDBParser()
    structure = parser.get_structure("PDB_structure", pdb_file)
    for model in structure:
        for chain in model:
            if chain.id == chain_id:
                sequence = ""
                for residue in chain:
                    if residue.id[0] == " ":
                        sequence += seq1(residue.resname)
                return sequence

def calc_chain_center(pdbfile: str, chain: str) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 3-2
    return np.zeros(3)

def calc_residue_center(pdbfile: str, chain: str, resname: str) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 3-3
    return np.zeros(3)

def calc_min_distance(pdbfile: str, chain: str, resname: str) -> float:
    # 課題 3-4
    return 0.0



if __name__ == "__main__":
    filepath = "data/1buw.pdb"
    chain = "A"
    resname = "HEM"
    # # 課題 3-2
    # print(calc_chain_center(filepath, chain))
    # # 課題 3-3
    # print(calc_residue_center(filepath, chain, resname))
    # # 課題 3-4
    # print(calc_min_distance(filepath, chain, resname))

    # 課題 3-3-2
    # cmd.load(filepath, 'hemoglobin_1buw')
    # cmd.hide('everything', 'hemoglobin_1buw')
    # # タンパク質をカートゥーン表示
    # cmd.show('cartoon', 'hemoglobin_1buw and chain A and not hetatm')  # 非ヘテロ原子（タンパク質のみ）をカートゥーン表示

    # cmd.color('green', 'hemoglobin_1buw and chain A and not hetatm')
    # # 二次構造に従って色付け
    # cmd.spectrum("ss", selection='hemoglobin_1buw and chain A and not hetatm')  # 二次構造に基づいて色分け
    # # ヘムをスティック表示して、原子種ごとに色付け
    # cmd.show('sticks', 'hemoglobin_1buw and chain A and resn HEM')  # ヘムをスティック表示
    # cmd.color('red', 'hemoglobin_1buw and chain A and resn HEM and elem O')  # 酸素原子を赤色で表示
    # cmd.color('blue', 'hemoglobin_1buw and chain A and resn HEM and elem N')  # 窒素原子を青色で表示
    # cmd.color('orange', 'hemoglobin_1buw and chain A and resn HEM and elem Fe')  # 鉄原子をオレンジ色で表示
    # cmd.rotate('x', 180, 'hemoglobin_1buw')
    # cmd.zoom('hemoglobin_1buw and chain A', 2)
    # cmd.png('hemoglobin_1buw_3-3-2.png')

    #　課題3-4
    # chain_ids = ["A", "B", "C", "D"]
    # amino_acid_sequences = []
    # for chain_id in chain_ids:
    #     sequence = get_amino_acid_sequence(filepath, chain_id)
    #     amino_acid_sequences.append(sequence)
    # print(amino_acid_sequences)

