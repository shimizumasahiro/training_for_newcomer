from typing import List, Union
import numpy.typing as npt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer, mean_squared_error

def rmse_score(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

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
    descriptor_funcs = [func for name, func in Descriptors.descList if name not in ["AvgIpc", "SPS"]] 

    # 記述子を計算
    descriptors = [func(mol) for func in descriptor_funcs]
    return np.array(descriptors)

def predict_logpapp(csvfile: str) -> Union[npt.NDArray[np.float_], pd.Series, List[float]]:
    # 課題 4-3
    np.random.seed(0) # 出力を固定するためにseedを指定
    rfr = RandomForestRegressor(random_state=0) # 出力を固定するためにrandom_stateを指定

    #データの取得
    df = pd.read_csv(csvfile)
    #random forest用のデータを作成
    X = df['SMILES'].apply(create_2d_descriptors).tolist()
    y = df['LogP app']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=700, random_state=0)
    rfr.fit(X_train, y_train)
    pred = rfr.predict(X_test)
    return pred

def grid_search(csvfile: str) -> float:
    # 課題 4-4
    # np.random.seed(0)
    # #データセットの取得
    # df = pd.read_csv(csvfile)
    # X = df['SMILES'].apply(create_2d_descriptors).tolist()
    # y = df['LogP app']
    # # 探索パラメータ
    # n_estimators_list = [100, 200, 400]
    # max_depth_list = [5, 10, 15]

    # # 最適化したい評価値RMSE
    # rmse_scorer = make_scorer(rmse_score, greater_is_better=False)
    # best_score = float('inf')
    # for n_estimators in n_estimators_list:
    #     for max_depth in max_depth_list:
    #         rfr = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=0)
    #         rmse_scores = -cross_val_score(rfr, X, y, cv=4, scoring=rmse_scorer)
    #         evaluation_score = np.mean(rmse_scores)
    #         print(f"rmse: {evaluation_score}, n_estimators: {n_estimators}, max_depth: {max_depth}")
    #         if evaluation_score < best_score:
    #             best_score = evaluation_score
    #             best_params = {'n_estimators': n_estimators, 'max_depth': max_depth}

    # return best_params, best_score

    np.random.seed(0)
    #データセットの取得
    df = pd.read_csv(csvfile)
    X = df['SMILES'].apply(create_2d_descriptors).tolist()
    y = df['LogP app']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=700, random_state=0)
    search_params = {
        "n_estimators": [100, 200, 400],
        "max_depth": [5, 10, 15]
    }
    gscv = GridSearchCV(
        RandomForestRegressor(random_state=0),
        search_params,
        cv=4,
        scoring=make_scorer(rmse_score, greater_is_better=False)
        )
    gscv.fit(X_train, y_train)
    y_pred = gscv.predict(X_test)
    return rmse_score(y_test, y_pred)



if __name__ == "__main__":
    smiles = "C(=O)(c1ccc(OCCCCCC)cc1)CCNc1cc(Cl)ccc1"
    filepath = "data/fukunishi_data.csv"
    # 課題 4-1
    draw_molecule(filepath)
    # 課題 4-2
    print(create_2d_descriptors(smiles))
    # # 課題 4-3
    print(predict_logpapp(filepath))
    # 課題 4-4
    print(grid_search(filepath))
