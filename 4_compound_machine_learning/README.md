# 4 創薬情報処理・機械学習

論文 [Y Fukunishi, ***et al.***, ***Molecular Informatics***, **38**: 190071, 2019.](https://doi.org/10.1002/minf.201900071) の Supporting Information Table S1 に公開されている 795 個の化合物の細胞膜透過率 (Membrane Permeability) を使って以下の実装を行え。

なお、当該のデータには間違いがあったため、 `data/fukunishi_data.csv` を利用すること。

## 4-0 目的変数「細胞膜透過率」を知る
この論文では、細胞膜透過率 `LogP app` を機械学習で予測している。
なぜ予測が必要なのか、高精度な予測を実現するとどういうメリットが得られるのか調査せよ。

（2023年現在、細胞膜透過率予測は秋山研中分子グループの中心的なテーマである）

## 4-1 RDKitによる化合物構造式の描画

CSVファイルの中に含まれる `CHEMBL540227` のSMILES式を読み込み構造式を描画せよ。以下に別ツールで描画した構造式を示す。

![mol](https://user-images.githubusercontent.com/6902135/229276218-2581661d-cc33-4a49-b568-dde076cec897.svg)

## 4-2 2D記述子の作成（自動テスト対象）

所望の化合物に対し、RDKitによって2D記述子 (descriptor) を全て計算し、それらを並べたベクトルを構成せよ。

例
```
入力：化合物のSMILES式 "C(=O)(c1ccc(OCCCCCC)cc1)CCNc1cc(Cl)ccc1"
出力：実数値列 [12.24, 0.11, 12.24, 0.11, 0.40, ...]
```

## 4-3 2D記述子に基づく回帰予測（自動テスト対象）

説明変数（特徴量）を2D記述子、 目的変数を `LogP app` とした、回帰予測を実施せよ。学習器は Random Forest をデフォルトパラメータのまま用いよ。

なお、794件の化合物データは以下のコードに従って訓練データ 700件、テストデータ94件に分割し、訓練データのみを使って予測モデルを構築、テストデータに対する予測値を列挙すること。

```py
from sklearn.model_selection import train_test_split

# Xは説明変数、yは目的変数
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=700, random_state=0)
```

## 4-4 グリッドサーチに基づくRandom Forestのハイパーパラメータ探索（自動テスト対象）
訓練データに対する 4-fold Cross Validation (CV) に基づいて、RMSE が最も低くなるパラメータをグリッドサーチで探索せよ。
ただし、グリッドサーチのパラメータは以下のようにせよ。

| パラメータ | 探索を行う値 |
|------|------|
| n_estimators | 100, 200, 400 |
| max_depth | 5, 10, 15 |

得られた予測モデルをテストデータの予測に利用し、予測値の RMSE を算出せよ。

# 補足情報

- この課題の実行のために役立つと思われるリンク集
  - https://github.com/Mishima-syk/py4chemoinformatics
  - https://www.rdkit.org/docs_jp/Getting_Started_with_RDKit_in_Python_jp.html
  - https://www.rdkit.org/docs/index.html
  - https://future-chem.com/
  - https://scikit-learn.org/stable/
  - https://blog.amedama.jp/entry/2018/05/01/081842