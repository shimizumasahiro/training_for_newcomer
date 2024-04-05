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
    for index, (a, b) in enumerate(pairs):
        start_1 = a
        start_2 = b
        length = 1
        for i in range(index+1, len(pairs)):
            target_a, target_b = pairs[i]
            if (target_a-1 == start_1) and (target_b+1 == start_2):
                length += 1
                start_1 = target_a
                start_2 = target_b
        if length >= min_length:
            result.append((a, b, length))

    return result

def create_dotbracket_notation(fastafile: str, min_distance: int=4, min_length: int=2) -> str:
    # 課題 2-4
    return ""

if __name__ == "__main__":
    filepath = "data/AUCGCCAU.fasta"
    # 課題 2-1
    print(enumerate_pairs(filepath))
    # 課題 2-2
    print(enumerate_possible_pairs(filepath))
    # 課題 2-3
    print(enumerate_continuous_pairs(filepath, 2))
    # 課題 2-4
    print(create_dotbracket_notation(filepath, 2))


