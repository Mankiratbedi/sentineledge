import streamlit as st
import time
import pandas as pd
import numpy as np
from modules.mockagent import SentinelAgent

# Page Config (Tactical Dark Mode)
st.set_page_config(
    page_title="SentinelEdge AI | Tactical Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "Military/Cyber" aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #00FF00;
    }
    .metric-card {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #6366f1;
    }
    .alert-box {
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Agent
agent = SentinelAgent()

# --- SIDEBAR: MISSION CONTROL ---
st.sidebar.image("https://img.icons8.com/color/96/000000/military-shield.png", width=80)
st.sidebar.title("SentinelEdge AI")
st.sidebar.caption("v1.0.0 | Offline Mode")

st.sidebar.markdown("---")
device_status = st.sidebar.empty()
st.sidebar.markdown("**System Stats:**")
st.sidebar.code("CPU Load: 12%\nRAM Usage: 450MB\nNPU: Active")

mission_toggle = st.sidebar.checkbox("ARM AGENT (Start Monitoring)", value=False)

# --- MAIN DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📡 Live Tactical Feed")
    # Placeholder for Video Feed
    video_placeholder = st.empty()
    video_placeholder.image("https://media.istockphoto.com/id/1199346614/video/digital-interface-with-data-on-dark-background.jpg?s=640x640&k=20&c=K5i-uDszK6-mXQgwlq2Fk8sZt9-1e3R3Q5q_R1b6z4s=", caption="Waiting for Input Stream...")

with col2:
    st.header("🧠 Agent Diagnostics")
    
    # Real-time Metrics
    status_text = st.empty()
    risk_meter = st.empty()
    log_feed = st.container()

    st.markdown("### Decision Logic")
    chart_placeholder = st.empty()

# --- MAIN LOOP (THE SIMULATION) ---
if mission_toggle:
    device_status.success("● SYSTEM ONLINE")
    
    # Create a dummy dataframe for the live chart
    chart_data = pd.DataFrame(columns=['Time', 'Risk Score'])
    
    for i in range(100):
        # 1. Run Agent Logic
        agent.observe()
        status_text.markdown(f"**Status:** `{agent.status}`")
        time.sleep(0.1) 
        
        agent.orient()
        
        risk = agent.decide()
        alert = agent.act(risk)

        # 2. Update UI Components
        video_placeholder.image("https://media.istockphoto.com/id/1321462048/video/cctv-camera-scan-on-street.jpg?s=640x640&k=20&c=Xj5yPqj1g_K_k_k_k_k_k_k_k_k_k_k_k_k_k_k_k_k=", caption="Analyzing Source: Body_Cam_04")
        
        # Risk Meter Color Logic
        if risk > 0.75:
            risk_meter.markdown(f'<div class="alert-box" style="background-color: #7f1d1d; color: white;">🛑 THREAT LEVEL: {risk:.2f}</div>', unsafe_allow_html=True)
        elif risk > 0.4:
            risk_meter.markdown(f'<div class="alert-box" style="background-color: #78350f; color: white;">⚠️ THREAT LEVEL: {risk:.2f}</div>', unsafe_allow_html=True)
        else:
            risk_meter.markdown(f'<div class="alert-box" style="background-color: #14532d; color: white;">✅ THREAT LEVEL: {risk:.2f}</div>', unsafe_allow_html=True)

        # 3. Update Chart
        new_row = pd.DataFrame({'Time': [i], 'Risk Score': [risk]})
        chart_data = pd.concat([chart_data, new_row]).tail(30) # Keep last 30 frames
        chart_placeholder.line_chart(chart_data.set_index('Time'))

        # 4. Log Output
        with log_feed:
            st.code(f"[{time.strftime('%H:%M:%S')}] {alert}")

        time.sleep(0.5) # Loop speed
else:
    device_status.warning("○ SYSTEM OFFLINE")