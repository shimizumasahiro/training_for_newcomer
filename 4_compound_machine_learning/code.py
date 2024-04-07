from typing import List, Union
import numpy.typing as npt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def draw_molecule(csvfile: str) -> None:
    # 課題 4-1
    df = pd.read_csv(csvfile)
    target = df.loc[df["Compound ID"] == "CHEMBL540227"]
    smiles = target["SMILES"].iloc[0]
    mol = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(mol)
    img.save("CHEMBL540227.png")
    pass

def create_2d_descriptors(smiles: str) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 4-2
    mol = Chem.MolFromSmiles(smiles)
    # 記述子の計算関数のリスト
    descriptor_funcs = [func for _, func in Descriptors.descList]
    # 記述子を計算
    descriptors = [func(mol) for func in descriptor_funcs]
    return np.array(descriptors)

def predict_logpapp(csvfile: str) -> Union[npt.NDArray[np.float_], pd.Series, List[float]]:
    # 課題 4-3
    np.random.seed(0) # 出力を固定するためにseedを指定
    rfr = RandomForestRegressor(random_state=0) # 出力を固定するためにrandom_stateを指定

    return 0.0

def grid_search(csvfile: str) -> float:
    # 課題 4-4
    # こちらも出力を固定するためにseedやrandom_stateを指定すること
    np.random.seed(0)

    # # Xは説明変数、yは目的変数
    # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=700, random_state=0)
    # 

    return 0.0

if __name__ == "__main__":
    smiles = "C(=O)(c1ccc(OCCCCCC)cc1)CCNc1cc(Cl)ccc1"
    filepath = "data/fukunishi_data.csv"
    # 課題 4-1
    draw_molecule(filepath)
    # 課題 4-2
    print(create_2d_descriptors(smiles))
    # 課題 4-3
    print(predict_logpapp(filepath))
    # 課題 4-4
    print(grid_search(filepath))
