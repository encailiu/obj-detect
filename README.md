# 物体検出デモ（YOLO11）

## 概要

このリポジトリは、YOLO11（Ultralytics YOLO）を用いた画像の物体検出デモです。  
`main.py` を実行することで、サンプル画像（例: `sample000.jpg`）に対して物体検出を行い、検出結果を画像（`output.jpg`）として保存します。

## ファイル構成

- README.md  
  このドキュメント
- [main.py](./main.py)  
  物体検出を実行するメインスクリプト
- [Readme_main.md](./Readme_main.md)  
  main.pyの説明ドキュメント
- [pyproject.toml](./pyproject.toml)  
  依存パッケージの管理ファイル
- [sample000.jpg](./sample000.jpg)  
  サンプル画像
- [test_data](./test_data/)  
  テスト用の画像データフォルダ

プログラムを実行すると、入力画像に対して物体検出を行い、結果を `output.jpg` として保存します。

モデルファイル（`yolo11n.pt`）は、UltralyticsのYOLOv8モデルを使用しています。プログラム実行時に自動でダウンロードされます(要インタネット接続)。

## 使えるモデル

詳細は[Ultralyticsのドキュメント](https://docs.ultralytics.com/ja/tasks/detect/#models)を参照してください。パラメータの数が大きければ大きいほど、精度は高くなりますが、処理速度は遅くなります。

- `yolo11n.pt` は YOLO11 Nano モデルで、軽量で高速な物体検出が可能です。
- `yolo11s.pt` は YOLO11 Small モデルで、精度と速度のバランスが良いです。
- `yolo11m.pt` は YOLO11 Medium モデルで、より高い精度を提供します。
- `yolo11l.pt` は YOLO11 Large モデルで、さらに高い精度を提供しますが、処理速度は遅くなります。
- `yolo11x.pt` は YOLO11 Extra Large モデルで、最高の精度を提供しますが、最も重く、処理速度は最も遅くなります。

## 動作確認環境

- Python 3.13

### 主要依存パッケージ

- ultralytics
- opencv-python
- numpy
- matplotlib

詳細は `pyproject.toml` を参照してください。

## セットアップ

1. 依存パッケージのインストール

    ```sh
    Pip install -r pyproject.toml
    ```

    または

    ```sh
    pip install ultralytics opencv-python numpy matplotlib
    ```

1. サンプル画像（`sample000.jpg`）が同じディレクトリにあることを確認してください。  
   モデルファイル（`yolo11n.pt`）は実行時に自動でダウンロードされます。

## 使い方

1. 物体検出を実行

   ```sh
   python main.py
   ```

2. 結果

   - 検出結果が `output.jpg` として保存されます。
   - ターミナルに検出された物体名・座標・信頼度が表示されます。

## カスタマイズ

- `main.py` 内の `image_path` を変更することで、任意の画像で物体検出が可能です。
-  `main.py`の`cv2.imwrite("output.jpg", img)`の行の`output.jpg`を変えると検出結果を別ファイルに保存することができます。

## ライセンス

- モデルファイル（`yolo11n.pt`）は Ultralytics の AGPL-3.0 ライセンスです。
- その他のコードは MIT ライセンスです。
