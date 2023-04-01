from typing import List, Union
import numpy.typing as npt
import numpy as np

def base_count(fastafile) -> int:
    # 課題 1-1
    return 0

def gen_rev_comp_seq(fastafile) -> str:
    # 課題 1-2
    return ""

def calc_gc_content(fastafile, window=1000, step=300) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 1-3
    # 値を出力するところまで。matplotlibを使う部分は別途実装してください。
    return []

def search_motif(fastafile, motif) -> List[str]:
    # 課題 1-4
    return []

def translate(fastafile) -> List[str]:
    # 課題 1-5
    return []

if __name__ == "__main__":
    # 課題 1-1
    print(base_count("data/NT_113952.1.fasta"))
    # 課題 1-2
    print(gen_rev_comp_seq("data/NT_113952.1.fasta"))
    # 課題 1-3
    print(calc_gc_content("data/NT_113952.1.fasta"))
    # 課題 1-4
    print(search_motif("data/NT_113952.1.fasta", "ATG"))
    # 課題 1-5
    print(translate("data/NT_113952.1.fasta"))