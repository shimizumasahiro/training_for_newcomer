from typing import List, Union
import numpy.typing as npt
import numpy as np

def calc_chain_center(pdbfile, chain) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 3-2
    return np.zeros(3)

def calc_residue_center(pdbfile, chain, resname) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 3-3
    return np.zeros(3)

def calc_min_distance(pdbfile, chain, resname) -> float:
    # 課題 3-4
    return 0.0



if __name__ == "__main__":
    # 課題 3-2
    print(calc_chain_center("data/1buw.pdb", "A"))
    # 課題 3-3
    print(calc_residue_center("data/1buw.pdb", "A", "HEM"))
    # 課題 3-4
    print(calc_min_distance("data/1buw.pdb", "A", "HEM"))