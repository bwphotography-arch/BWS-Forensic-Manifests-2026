"""
BWS Forensic Manifests Loader
Example script to load and explore BWS Data Solutions manifests
"""

import pandas as pd
from pathlib import Path
import glob

def load_manifest(csv_path: str) -> pd.DataFrame:
    """Load a single manifest CSV with proper data types."""
    df = pd.read_csv(
        csv_path,
        dtype={
            'filename': 'string',
            'file_hash_md5': 'string',
            'file_size_mb': 'float64',
            'capture_date': 'string',
            'clear_act_status': 'string',
            'rights_holder': 'string'
        }
    )
    print(f"✅ Loaded {len(df):,} records from {Path(csv_path).name}")
    return df


def load_all_manifests(directory: str = "."):
    """Load all individual manifest CSVs in the folder."""
    manifests = {}
    for file in sorted(glob.glob(f"{directory}/*Manifest.csv")):
        name = Path(file).stem
        manifests[name] = load_manifest(file)
    
    print(f"\n📊 Loaded {len(manifests)} individual manifests")
    return manifests


def explore_master_manifest(master_path: str = "BWS_CLEAR_MASTER_MANIFEST_2026.csv"):
    """Load and summarize the master inventory."""
    df = load_manifest(master_path)
    
    print("\n" + "="*60)
    print("🔍 MASTER MANIFEST SUMMARY")
    print("="*60)
    print(f"Total Assets: {len(df):,}")
    print(f"Unique Capture Dates: {df['capture_date'].nunique()}")
    
    if 'clear_act_status' in df.columns:
        print("\nCLEAR Act Status Distribution:")
        print(df['clear_act_status'].value_counts())
    
    if 'file_size_mb' in df.columns:
        total_size = df['file_size_mb'].sum()
        print(f"\nTotal Size: {total_size:.2f} MB ({total_size/1024:.2f} GB)")
    
    return df


# ====================== USAGE EXAMPLES ======================

if __name__ == "__main__":
    print("🚀 BWS Data Solutions Manifest Loader\n")
    
    # Load one specific set
    fashion_df = load_manifest("01_Studio_Fashion_60_JPEGs_Manifest.csv")
    print(f"Sample filenames:\n{fashion_df['filename'].head(5).tolist()}\n")
    
    # Load everything
    all_manifests = load_all_manifests()
    
    # Load Master
    master_df = explore_master_manifest()
    
    # Example: Filter for specific status
    # federal = master_df[master_df['clear_act_status'] == 'Federal']
