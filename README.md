# 🏆 VCT Analytics Dashboard (2021-2025)

A professional-grade esports analytics dashboard for the **Valorant Champions Tour**, built with **Streamlit** and **Plotly**. This application visualizes over 1.1 million records of match data to provide deep insights for analysts, coaches, and competitive fans.

🔗 **Live Demo**: [Deploy on Streamlit Cloud](https://vct-analytics-apascdr5fkh7mxwzufyrgu.streamlit.app/)



## ✨ Key Features

*   **🌐 Command Center**: High-level KPIs, Meta Evolution "River" charts, and Global heatmaps.
*   **👤 Player Analytics**: Deep-dive into player performance with Spider Charts (ACS, K/D, KAST), Trend lines, and Agent Mastery profiles.
*   **🛡️ Team Analytics**: Win rates, active roster snapshots, and map pool strength visualization.
*   **🤖 Agent Meta**: Track "S-Tier" agents, pick rate trends across 5 years, and historical meta shifts (Jett Era -> Chamber Era -> Omen Era).
*   **🗺️ Map Balance**: Interactive side-balance analysis (Attacker vs Defender win rates) for every map in the pool.
*   **📜 Tournament History**: Browse historical data from VCT 2021 through 2025.

## 🛠️ Tech Stack

*   **Framework**: [Streamlit](https://streamlit.io/) (Python)
*   **Visualization**: [Plotly Express](https://plotly.com/python/) (High-performance interactive charts)
*   **Data Processing**: Pandas & NumPy
*   **Design**: Custom CSS for "Premium Esports" aesthetic (Dark Mode, Glassmorphism, Inter/JetBrains Mono fonts).

## 🚀 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/ElectricPlant19/VCT-Analytics.git
    cd VCT-Analytics
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run app.py
    ```

> **Note**: The app includes an **Auto-Downloader**. On the first run, it will automatically download the 1GB+ dataset from Kaggle using `kagglehub`. No manual data setup required!

## ☁️ Deployment (Streamlit Cloud)

This repo is **Cloud-Ready**. To deploy:

1.  Push this code to your GitHub.
2.  Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3.  Connect your repo and select `app.py` as the entry point.
4.  **Deploy!** The app will handle the data download automatically during the build process.

## 📚 Data Source

Data provided by **Ryan Luong** via Kaggle:
[Valorant Champion Tour 2021-2023 Data](https://www.kaggle.com/datasets/ryanluong1/valorant-champion-tour-2021-2023-data)

---

*Built with ❤️ for the Valorant Community.*
