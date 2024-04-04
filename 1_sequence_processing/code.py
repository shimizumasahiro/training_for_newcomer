from typing import List, Union
import numpy.typing as npt
import numpy as np
from Bio import SeqIO
import inspect
import matplotlib.pyplot as plt

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
    # データの読み込み
    file_data = read_fasta_file(fastafile)
    sequences = file_data[0].seq
    reverse_seq = sequences.reverse_complement()
    return f"{reverse_seq}"

def calc_gc_content(fastafile: str, window: int=1000, step: int=300) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 1-3
    # データの読み込み
    file_data = read_fasta_file(fastafile)
    sequences = file_data[0].seq

    # 処理
    gc_contents = []
    index_list = []
    for i in range(0, len(sequences) - window + 1, step):
        subseq = sequences[i:i+window]
        gc_count = subseq.count("G") + subseq.count("C")
        gc_content = (gc_count / window) * 100
        gc_contents.append(gc_content)
        #index_list.append(i)
    # 値を出力するところまで。matplotlibを使う部分は別途実装してください。
    return np.round(gc_contents, 2)#, index_list

def search_motif(fastafile: str, motif: str) -> List[str]:
    # 課題 1-4
    # データ読み込み
    file_data = read_fasta_file(fastafile)
    sequences = file_data[0].seq

    #結果
    result = []
    #逆相補鎖の取得
    reverse_seq = sequences.reverse_complement()
    #全長の取得
    size = len(sequences)
    #検索
    for index, sub in sequences.search([motif]):
        result.append(f"F{index+1}")
    
    for index, sub in reverse_seq.search([motif]):
        result.append(f"R{size-index}")
    return result

def translate(fastafile: str) -> List[str]:
    # 課題 1-5
    return []

if __name__ == "__main__":
    filepath = "data/NT_113952.1.fasta"
    # 課題 1-1
    print(base_count(filepath))
    # 課題 1-2
    print(gen_rev_comp_seq(filepath))
    # 課題 1-3
    print(calc_gc_content(filepath))
    # plt.plot(index, result)
    # plt.savefig("課題1-3.pdf")

    # 課題 1-4
    print(search_motif(filepath, "ATG"))
    # # 課題 1-5
    # print(translate(filepath))
