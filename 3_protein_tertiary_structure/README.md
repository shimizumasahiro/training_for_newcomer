# 3 タンパク質構造情報処理

タンパク質立体構造データベース Protein Data Bank (PDB) の中にある PDBID `1BUW` はヒトのヘモグロビンであり、4つのタンパク質がくっついた形でデータが登録されている。また、ヘモグロビンはヘムが（非共有）結合している。

一方、1BUWのA鎖 (chain A) のアミノ酸配列は以下の通りである。
```
VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR
```

## 3-1 タンパク質立体構造データのダウンロード

PDBのWebサイト https://www.rcsb.org/ にアクセスし、pdb 形式のタンパク質立体構造データをダウンロードせよ。
ダウンロードしたファイルは、 `data/1buw.pdb` として保存すること。

## 3-2 PyMOLのインストール
PyMOLとは、タンパク質や化合物などをGUIで描画するツールであり、タンパク質の構造などを扱う研究を行う際には必ずと言ってよいほど使う。
Scrapboxに記載されている情報や、 https://qiita.com/Ag_smith/items/58e917710c4eddab46ee などを参考に、PyMOLをPCにインストールせよ。

## 3-3 PyMOLを使ったタンパク質の表示

ダウンロードした `1buw.pdb` について、以下のような2つの画像の描画を行え。

1. **4つのタンパク質は異なる「チェイン」として登録されている。チェインごとに異なる色で表示せよ。**

<img src="https://user-images.githubusercontent.com/6902135/229275018-ebd4d3d9-3972-486c-a8df-065f4c129da0.png" style="width:300px">

2. **Aチェインだけについて、以下の描画を行え。**
  - タンパク質をcartoon表示にする
  - 2次構造に従って色付けする
  - 結合するヘムをstick表示して、原子種ごとに色付けする

<img src="https://user-images.githubusercontent.com/6902135/229275151-7c6fe2d5-b3ec-494c-a007-ca291ab3f878.png" style="width:300px">

## 3-4 ColabFoldを使ったタンパク質立体構造の予測

ColabFoldとは、タンパク質立体構造予測手法であるAlphaFold2をGoogle Colaboratory上で実行可能にしたものである。

https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

前述したヘモグロビンのアミノ酸配列を入力に与えてColabFoldを実行し、その結果のうち最も良いとされた（`rank_001`となっている）pdbファイルをダウンロードし、 `data/cf_pred.pdb` として保管せよ。
- アミノ酸配列以外の設定は（様々興味深いものはあるが）変更しないで実行せよ。

## 3-5 2つの構造間の差の定量化

3-1と3-4で準備した `data/1buw.pdb` の chain A および　`data/cf_pred.pdb` について、RMSDを計算せよ。
- RMSDの計算にはBioPythonやMDAnalysisなどを使ってスクリプトを組むこともできるが、おそらくPyMOLのGUIから構造重ね合わせを行うのが最も簡単ではないかと思われる。
  - 本来は、どの原子に着目してRMSDを計算したのか？という情報も必要なのだが、今回は構造の差異を定量化するという経験をすることが要点なので一旦無視している。
    - もし興味があれば、PyMOLの操作ではどのようなRMSDが出力されているのか、調べてみてほしい。
  - 1BUWはAlphaFold2の学習データに含まれているので、予測精度は極めて良好なはずである。
    - 実際の利用の際には、学習データに含まれていないタンパク質を予測したいはずなので、必ずしもここまで精度は良くならないことに注意してほしい。