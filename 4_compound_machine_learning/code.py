from typing import List, Union
import numpy.typing as npt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def draw_molecule(csvfile: str) -> None:
    # 課題 4-1
    pass

def create_2d_descriptors(csvfile: str) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 4-2
    return []

def predict_logpapp(csvfile: str) -> Union[npt.NDArray[np.float_], pd.Series, List[float]]:
    # 課題 4-3
    np.random.seed(0)

    return 0.0

def grid_search(csvfile: str) -> float:
    # 課題 4-4
    np.random.seed(0)

    # # Xは説明変数、yは目的変数
    # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=700, random_state=0)

    return 0.0

if __name__ == "__main__":
    filepath = "data/fukunishi_data.csv"
    # 課題 4-1
    draw_molecule(filepath)
    # 課題 4-2
    print(create_2d_descriptors(filepath))
    # 課題 4-3
    print(predict_logpapp(filepath))
    # 課題 4-4
    print(grid_search(filepath))
