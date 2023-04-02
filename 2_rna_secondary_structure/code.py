from typing import List, Tuple, Union
import numpy.typing as npt
import numpy as np

def enumerate_pairs(seq: str) -> List[str]:
    # 課題 2-1
    return []

def enumerate_possible_pairs(seq: str) -> List[Tuple[int, int]]:
    # 課題 2-2
    return []

def enumerate_continuous_pairs(seq: str, min_length: int=2) -> List[Tuple[int, int, int]]:
    # 課題 2-3
    return []

def create_dotbracket_notation(seq: str, min_length: int=2) -> str:
    # 課題 2-4
    return ""

if __name__ == "__main__":
    sequence = "AUCGCCAU"
    # 課題 2-1
    print(enumerate_pairs(sequence))
    # 課題 2-2
    print(enumerate_possible_pairs(sequence))
    # 課題 2-3
    print(enumerate_continuous_pairs(sequence, 2))
    # 課題 2-4
    print(create_dotbracket_notation(sequence, 2))


