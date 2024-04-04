from typing import List, Union
import numpy.typing as npt
import numpy as np
from Bio import SeqIO
import inspect

def read_fasta_file(fastapath: str) -> SeqIO.FastaIO:
    sequences = []
    for record in SeqIO.parse(fastapath, "fasta"):
        sequences.append(record)
    return sequences

def base_count(fastafile: str) -> List[int]:
    # データの読み込み
    file_data = read_fasta_file(fastafile)
    sequences = file_data[0].seq

    # 課題 1-1
    return [sequences.count("A"), sequences.count("T"), sequences.count("G"), sequences.count("C")] # A, T, G, C

def gen_rev_comp_seq(fastafile: str) -> str:
    # 課題 1-2
    return ""

def calc_gc_content(fastafile: str, window: int=1000, step: int=300) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 1-3
    # 値を出力するところまで。matplotlibを使う部分は別途実装してください。
    return []

def search_motif(fastafile: str, motif: str) -> List[str]:
    # 課題 1-4
    return []

def translate(fastafile: str) -> List[str]:
    # 課題 1-5
    return []

if __name__ == "__main__":
    filepath = "data/NT_113952.1.fasta"
    # 課題 1-1
    print(base_count(filepath))
    # # 課題 1-2
    # print(gen_rev_comp_seq(filepath))
    # # 課題 1-3
    # print(calc_gc_content(filepath))
    # # 課題 1-4
    # print(search_motif(filepath, "ATG"))
    # # 課題 1-5
    # print(translate(filepath))
