# main.py の解説資料

以下は、`main.py` のコードを1行ずつ解説した資料です。

| 行番号 | プログラム | 説明 |
|--------|------------|------|
| 1      | `from ultralytics import YOLO` | YOLOという物体検出ライブラリをインポートします。YOLOは「You Only Look Once」の略で、画像内の物体を高速に検出するためのツールです。 |
| 2      | `import cv2` | OpenCVという画像処理ライブラリをインポートします。画像の読み込みや加工に使います。 |
| 3      | `import numpy as np` | NumPyという数値計算ライブラリをインポートします。画像データの操作に便利です。 |
| 4      | `import matplotlib.pyplot as plt` | Matplotlibというグラフ描画ライブラリをインポートします。画像を表示するために使います。 |
| 6-8    | `def load_yolo_model(model_path="yolo11n.pt"):`<br>`model = YOLO(model_path)`<br>`return model` | YOLOモデルを読み込む関数を定義しています。`model_path`で指定されたファイルからモデルをロードします。 |
| 10-12  | `def detect_objects_in_image(model, image_path):`<br>`results = model(image_path)`<br>`return results` | 指定された画像に対して物体検出を行う関数です。YOLOモデルを使って画像内の物体を検出し、その結果を返します。 |
| 14-36  | `def visualize_results(image_path, results):`<br>`img = cv2.imread(image_path)`<br>`...` | 検出結果を画像に描画し、ターミナルに出力する関数です。OpenCVを使って画像を読み込み、検出した物体の情報を描画します。 |
| 38     | `model = load_yolo_model()` | YOLOモデルを読み込みます。このとき、デフォルトのモデルファイル`yolo11n.pt`が使われます。 |
| 40     | `model.info()` | モデルの情報を表示します。例えば、モデルの構造やパラメータ数などが出力されます。 |
| 42     | `image_path = "./test_data/sandwich_1.jpg"` | 検出対象の画像ファイルのパスを指定します。この例では、`test_data`フォルダ内の`sandwich_1.jpg`を使用しています。 |
| 44     | `results = detect_objects_in_image(model, image_path)` | 指定した画像に対して物体検出を実行し、結果を`results`に保存します。 |
| 45     | `results[0].show()` | 検出結果を簡易的に表示します。YOLOライブラリの機能を使っています。 |
| 46     | `print(f"\nthe number of detection {len(results[0].boxes)}")` | 検出された物体の数をターミナルに出力します。`len(results[0].boxes)`で検出された物体の数を取得します。 |
| 48     | `visualize_results(image_path, results)` | 検出結果を画像に描画し、保存します。また、ターミナルに詳細な情報を出力します。 |

## 追加参考資料

- [YOLO公式ドキュメント](https://docs.ultralytics.com/)：YOLOの使い方や詳細な設定について学べます。
- [OpenCV公式ドキュメント](https://docs.opencv.org/)：画像処理の基本を学ぶのに役立ちます。
- [Matplotlib公式ドキュメント](https://matplotlib.org/stable/contents.html)：グラフや画像の描画方法を学べます。
- [NumPy公式ドキュメント](https://numpy.org/doc/stable/)：数値計算や配列操作の基本を学べます。

## main.py に定義されている関数の詳しい説明

### load_yolo_model(model_path="yolo11n.pt")

この関数はYOLOモデルを読み込むために使用されます。

- **引数**: `model_path` (文字列) - モデルのファイルパスを指定します。デフォルト値は`yolo11n.pt`です。

- **戻り値**: YOLOモデルオブジェクト。

- **詳細**: YOLOライブラリの`YOLO`クラスを使用して、指定されたパスからモデルをロードします。このモデルは物体検出に使用されます。

### detect_objects_in_image(model, image_path)

この関数は画像内の物体を検出します。

- **引数**:
  - `model` (YOLOモデルオブジェクト) - 物体検出に使用するモデル。
  - `image_path` (文字列) - 検出対象の画像ファイルのパス。

- **戻り値**: 検出結果オブジェクト。

- **詳細**: YOLOモデルを使用して、指定された画像内の物体を検出します。検出結果には、物体の位置やクラス情報が含まれます。

### visualize_results(image_path, results)

この関数は検出結果を画像に描画し、ターミナルに詳細情報を出力します。

- **引数**:
  - `image_path` (文字列) - 検出対象の画像ファイルのパス。
  - `results` (検出結果オブジェクト) - YOLOモデルによる検出結果。

- **戻り値**: なし。

- **詳細**:
  - OpenCVを使用して画像を読み込みます。
  - 検出された物体のバウンディングボックスやクラス名を画像に描画します。
  - 検出結果をターミナルに出力します（例: オブジェクト名、座標、信頼度）。
  - 処理後の画像を`output.jpg`として保存し、Matplotlibを使用して表示します。
