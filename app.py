import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError


iso_forest = joblib.load("models/isolation_forest_model.pkl")
autoencoder = load_model("models/autoencoder_model.keras")
scaler = joblib.load("models/scaler.pkl")

#Loading the important attributes
@st.cache_data
def load_data():
    col_names = [
        'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent',
        'hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations',
        'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count',
        'serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate',
        'dst_host_count','dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','label'
    ]
    df = pd.read_csv("data/kddcup.data_10_percent_corrected", names=col_names)
    return df

def preprocess(df):
    df = df.copy()
    df = df.drop(columns=["label"])
    df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])
    df_scaled = scaler.transform(df)
    return df_scaled

st.title("Network Anomaly Detection")

raw_df = load_data()
st.write("Sample of Network Traffic Data:")
st.dataframe(raw_df.head())

processed = preprocess(raw_df)

st.header("Choose Anomaly Detection Method")
method = st.selectbox("Method", ["Isolation Forest", "Autoencoder"])

if method == "Isolation Forest":
    preds = iso_forest.predict(processed)
    anomalies = preds == -1
else:
    reconstructions = autoencoder.predict(processed)
    mse = np.mean(np.square(processed - reconstructions), axis=1)
    threshold = np.percentile(mse, 95)
    anomalies = mse > threshold

st.write(f"Number of anomalies detected: {np.sum(anomalies)}")
st.dataframe(raw_df[anomalies].head())
