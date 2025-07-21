# 🚨 Anomaly Detection in Network Traffic using Unsupervised Learning

Uncover potential security breaches and system malfunctions by detecting anomalous patterns in network traffic with **Isolation Forests** and **Autoencoders** — all visualized using **Streamlit**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Unsupervised-orange?style=flat-square" />
</p>

---

## Project Overview

This project uses the **KDD Cup 1999** dataset to detect anomalies in network traffic, which may be early indicators of:

- Unauthorized access attempts  
- System misconfigurations  
- Denial of Service (DoS) attacks

We implemented two unsupervised ML techniques:
- **Isolation Forest**: A tree-based model to isolate anomalies
- **Autoencoder**: A neural network trained to reconstruct only normal data

All results are interactive and visualized in a **Streamlit web app**.

---

##  Dataset

- **Source**: [KDD Cup 1999 Data (Kaggle)](https://www.kaggle.com/datasets/galaxyh/kdd-cup-1999-data)
- **Size**: ~5M rows (used 10% sample for development)
- **Type**: Network connection logs
- **Features**: 41 attributes (protocol, service, flag, src_bytes, dst_bytes, etc.)



## 📁 Project Structure

