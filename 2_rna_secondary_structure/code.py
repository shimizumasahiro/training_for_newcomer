from typing import List, Tuple, Union
import numpy.typing as npt
import numpy as np

from Bio import SeqIO
from Bio.Seq import Seq

import itertools

def read_fasta_file(fastapath: str) -> SeqIO.FastaIO:
    sequences = []
    for record in SeqIO.parse(fastapath, "fasta"):
        sequences.append(record)
    return sequences

def enumerate_pairs(fastafile: str) -> List[Tuple[int, int]]:
    # 課題 2-1
    result = []
    #データの読み込み
    sequence = read_fasta_file(fastafile)
    sequence = sequence[0].seq
    a_positions = [i for i, char in enumerate(sequence) if char == "A"]
    u_positions = [i for i, char in enumerate(sequence) if char == "U"]
    g_positions = [i for i, char in enumerate(sequence) if char == "G"]
    c_positions = [i for i, char in enumerate(sequence) if char == "C"]


    for a, b in itertools.product(a_positions, u_positions):
        result.append((min(a+1, b+1), max(a+1, b+1)))
    for a, b in itertools.product(c_positions, g_positions):
        result.append((min(a+1, b+1), max(a+1, b+1)))
    return result

def enumerate_possible_pairs(fastafile: str, min_distance: int=4) -> List[Tuple[int, int]]:
    # 課題 2-2
    pairs = enumerate_pairs(fastafile)
    result = [pair for pair in pairs if pair[1] - pair[0] >= 4]
    return result

def enumerate_continuous_pairs(fastafile: str, min_distance: int=4, min_length: int=2) -> List[Tuple[int, int, int]]:
    # 課題 2-3
    #データの取得
    sequence = read_fasta_file(fastafile)
    sequence = sequence[0].seq

    #結果
    result = []

    # 塩基対の取得
    pairs = enumerate_possible_pairs(fastafile, min_distance=min_distance)
    # 左の要素について昇順にソート
    pairs.sort(key=lambda x: x[0])
    # 連続塩基対の取得
    i = 0
    while i < len(pairs):
        start_1, start_2 = pairs[i]
        length = 1
        i += 1
        while i < len(pairs) and pairs[i][0] == start_1 + length and pairs[i][1] == start_2 - length:
            length += 1
            i += 1
        if length >= min_length:
            result.append((start_1, start_2, length))

    return result

    return result

def create_dotbracket_notation(fastafile: str, min_distance: int=4, min_length: int=2) -> str:
    # 課題 2-4
    #データの取得
    sequence = read_fasta_file(fastafile)
    sequence = sequence[0].seq

    continuous_pairs = enumerate_continuous_pairs(fastafile, min_distance=min_distance, min_length=min_length)

    #結果
    bracket = list(len(sequence) * ".")
    # それぞれの(start1, start2, lenght)について以下を行う
    for (start1, start2, length) in continuous_pairs:
        start1 -= 1
        start2 -= 1
        bracket[start1:start1+length] = ["("] * length
        bracket[start2-length+1:start2+1] = [")"] * length
        #結果の保存
    return "".join(bracket)

if __name__ == "__main__":
    filepath = "data/NM_014495.4.fasta"
    # 課題 2-1
    print(enumerate_pairs(filepath))
    print("課題2-1:done")
    # 課題 2-2
    print(enumerate_possible_pairs(filepath))
    print("課題2-2:done")
    # 課題 2-3
    print(enumerate_continuous_pairs(filepath, 2))
    print("課題2-3:done")
    # 課題 2-4
    print(create_dotbracket_notation(filepath, 2))
    print("課題2-4:done")


