# Tire Price Prediction

簡介
--
本專案使用機器學習模型來預測輪胎價格（tire price prediction）。提供已訓練的模型與標準化器，以及範例資料與程式，方便快速進行推論或二次開發。

檔案說明
--
- `df_tires.csv` - 原始資料集範例（特徵與目標價格）。
- `Tire_price_prediction_model.ipynb` - Jupyter Notebook，包含資料探索、特徵工程與模型訓練流程。
- `Tire_price_prediction.py` - 簡易命令列腳本，用已訓練模型進行單筆或批次預測。
- `Tire_Price_model.joblib` - 訓練完成的模型權重（joblib 格式）。
- `Tire_Price_scaler.joblib` - 特徵標準化器（用於資料前處理）。
- `requirements.txt` - 專案相依套件清單。

快速開始
--
1. 建議使用 Python 3.8+，先建立虛擬環境並安裝相依套件：

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. 如果想在 Notebook 中重跑或檢視訓練流程，啟動 Jupyter 並開啟 `Tire_price_prediction_model.ipynb`。

3. 使用已訓練模型做預測（範例）：

```bash
# 執行腳本（視 `Tire_price_prediction.py` 支援的參數而定）
python Tire_price_prediction.py
```

註：`Tire_price_prediction.py` 會載入 `Tire_Price_scaler.joblib` 做前處理，並使用 `Tire_Price_model.joblib` 產生預測結果；如需批次預測，請參考程式內的使用說明或在 Notebook 中建立輸入範例。

開發與實驗
--
- 若要重新訓練模型，可參考 Notebook 中的資料前處理與模型訓練步驟，並產出新的 `.joblib` 檔案供推論使用。
- 如需加入更多特徵或調整模型，建議先在 Notebook 進行探索式實驗，再把穩定流程封裝至 `.py` 腳本。

聯絡
--
如需協助或有回饋，請在專案中建立 Issue 或直接聯絡專案維護者。

---
最後更新：2025-12-28

