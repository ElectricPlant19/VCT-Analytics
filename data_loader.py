import pandas as pd
import os
import streamlit as st
import numpy as np

import kagglehub
import shutil

DATA_DIR = "data"

# Check if data exists, if not download it (for Streamlit Cloud)
if not os.path.exists(DATA_DIR):
    try:
        print("Data directory not found. Downloading from Kaggle...")
        path = kagglehub.dataset_download("ryanluong1/valorant-champion-tour-2021-2023-data")
        # kagglehub downloads to a cache dir, we need to move or symlink, or just point DATA_DIR there
        # For simplicity in this app structure, let's copy/move content to 'data'
        # Actually, simpler: Update DATA_DIR to point to the download path
        # But our code expects 'vct_2021' inside DATA_DIR. The download usually contains these folders.
        
        # Let's try to copy it to local 'data' so standard logic works
        print(f"Dataset downloaded to: {path}")
        shutil.copytree(path, DATA_DIR, dirs_exist_ok=True)
        print("Data moved to local directory.")
        
    except Exception as e:
        st.error(f"Failed to download data: {e}")

YEARS = ["vct_2021", "vct_2022", "vct_2023", "vct_2024", "vct_2025"]

@st.cache_data(show_spinner=False)
def load_and_combine(category, filename):
    """
    Loads a specific CSV file across all year directories and combines them.
    Adds a 'Source_Year' column.
    """
    dfs = []
    # Create progress bar if run from main app context, but fail gracefully if not
    try:
        progress = st.progress(0)
    except:
        progress = None
        
    for i, year in enumerate(YEARS):
        path = os.path.join(DATA_DIR, year, category, filename)
        if os.path.exists(path):
            try:
                # Optimized loading: specify some dtypes to save memory if needed
                df = pd.read_csv(path, low_memory=False) 
                df['Source_Year'] = year
                dfs.append(df)
            except Exception as e:
                print(f"Warning: Could not load {path}: {e}")
        
        if progress:
            progress.progress((i + 1) / len(YEARS))
            
    if progress:
        progress.empty()

    if dfs:
        full_df = pd.concat(dfs, ignore_index=True)
        return clean_data(full_df, filename)
    return pd.DataFrame()

def clean_data(df, filename):
    """
    Applies specific cleaning rules based on the file type.
    """
    if filename == "overview.csv":
        # Matches Overview
        # 1. Clean ACS: Convert to numeric, handle NaN, remove logical outliers
        if 'Average Combat Score' in df.columns:
            df['Average Combat Score'] = pd.to_numeric(df['Average Combat Score'], errors='coerce')
            # Remove ACS > 500 (Outliers identified in analysis)
            df = df[df['Average Combat Score'] <= 500]
            
        # 2. Clean KD
        if 'Kills - Deaths (KD)' in df.columns:
             df['KD'] = pd.to_numeric(df['Kills - Deaths (KD)'], errors='coerce')
             
        # 3. Clean Percentages
        for col in ['Headshot %', 'Kill, Assist, Trade, Survive %']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.rstrip('%').astype(float)
                
    elif filename == "agents_pick_rates.csv":
         if 'Pick Rate' in df.columns:
            df['Pick Rate'] = df['Pick Rate'].astype(str).str.rstrip('%').astype(float)
            
    elif filename == "maps_stats.csv":
        for col in ['Attacker Side Win Percentage', 'Defender Side Win Percentage']:
             if col in df.columns:
                df[col] = df[col].astype(str).str.rstrip('%').astype(float)
                
    return df

@st.cache_data
def get_matches_overview():
    return load_and_combine("matches", "overview.csv")

@st.cache_data
def get_agent_pick_rates():
    return load_and_combine("agents", "agents_pick_rates.csv")

@st.cache_data
def get_map_stats():
    return load_and_combine("agents", "maps_stats.csv")

@st.cache_data
def get_match_scores():
    return load_and_combine("matches", "scores.csv")
