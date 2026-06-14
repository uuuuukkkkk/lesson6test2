# BMI計算機

## 概要

身長(cm)と体重(kg)を入力することで、BMI（Body Mass Index）と肥満度を判定するシンプルなWebアプリです。

Python標準ライブラリのみを使用して実装しており、外部ライブラリは使用していません。

---

## 機能

- BMIの計算
- 肥満度判定
- 入力値のリセット
- 数値以外の入力を制限
- 0未満の値の入力を制限

---

## 使用技術

- Python 3
- WSGI
- HTML
- CSS
- JavaScript

---

## ファイル構成

```
project/
├── app.py
└── README.md
```

---

## 起動方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/your-name/bmi-app.git
cd bmi-app
```

### 2. アプリを起動

```bash
python app.py
```

または

```bash
python3 app.py
```

### 3. ブラウザでアクセス

```text
http://localhost:8000
```

---

## Renderへのデプロイ

### Build Command

```bash
python --version
```

### Start Command

```bash
python app.py
```

本アプリは環境変数 `PORT` に対応しています。

```python
port = int(os.environ.get("PORT", 8000))
```

そのため Render 上でもそのまま動作します。

---

## BMIの計算式

BMIは以下の計算式で求めます。

```text
BMI = 体重(kg) ÷ 身長(m)^2
```

### 計算例

```text
身長：170cm
体重：65kg

BMI = 65 ÷ 1.7²
    = 22.5
```

---

## 判定基準

| BMI | 判定 |
|------|------|
| 18.5未満 | 低体重（やせ） |
| 18.5以上25未満 | 普通体重 |
| 25以上30未満 | 肥満（1度） |
| 30以上35未満 | 肥満（2度） |
| 35以上40未満 | 肥満（3度） |
| 40以上 | 肥満（4度） |

---

## 作者

学習用サンプルとして作成