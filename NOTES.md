# Architecture Decision Records & System Notes
**Project:** Jordan Agricultural Price Prediction Engine  
**Target Domain:** Price Forecasting via Remote Sensing & Tabular ML  

---

## 1. System Architecture & Component Selection

### 1.1 Data Acquisition (Google Earth Engine - GEE)
* **Context:** High-resolution spatial-temporal vegetation data is required to monitor crop health and yield expectations across agricultural zones in Jordan.
* **Decision:** Utilize Google Earth Engine (GEE) Python API for server-side raster calculations (Sentinel-2 NDVI/EVI).
* **Rationale:** Offloads heavy satellite imagery computation to Google Cloud infrastructure, avoiding high local storage and RAM consumption.

### 1.2 Predictive Core (XGBoost)
* **Context:** Price prediction relies on structured tabular features combining historical market prices, seasonal patterns, and satellite-derived vegetation indices.
* **Decision:** Implement XGBoost (eXtreme Gradient Boosting) as the primary regression engine.
* **Rationale:** Superior performance on tabular time-series data, lower computational latency compared to deep learning, and built-in capability to output feature importance metrics.

---

## 2. Engineering Standards & Security Principles

* **Secrets Management:** Sensitive keys and service account credentials must strictly remain in `.env` and be excluded via `.gitignore`.
* **Reproducibility:** All python dependencies must be pinned in `requirements.txt` to enforce consistent execution environments.
* **Data Continuity:** Time-series gaps must be handled using linear interpolation rather than row deletion to preserve sequence alignment.