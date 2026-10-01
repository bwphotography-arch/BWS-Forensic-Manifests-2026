"""
BWS Data Solutions - Enterprise Dataset Loader
Includes direct API routing for Mozilla Data Collective (MDC)
"""

def load_hitch_hiker_robotics_data_mdc():
    """
    Downloads the full, commercial 425-asset Hitch Hiker dataset via MDC API.
    Requires MDC API Key and approved access to dataset ID: cmuppz5bm01s5mg067qo2b8x3
    """
    try:
        from datacollective import download_dataset
        print("Authenticating with Mozilla Data Collective...")
        dataset_path = download_dataset("cmuppz5bm01s5mg067qo2b8x3")
        return dataset_path
    except ImportError:
        print("Please install the datacollective python library: pip install datacollective")

def load_hitch_hiker_preview_hf():
    """
    Loads the 12-image preview/sandbox dataset from Hugging Face.
    """
    try:
        from datasets import load_dataset
        print("Loading BWS Hitch Hiker preview from Hugging Face...")
        dataset = load_dataset("BWS-Data-Solutions/BWS-Hitch-Hiker-Cyberpunk-Physics")
        return dataset
    except ImportError:
         print("Please install the datasets library: pip install datasets")

if __name__ == "__main__":
    print("BWS Data Solutions Loader Initialized.")
    # Uncomment to test loading the preview:
    # preview_data = load_hitch_hiker_preview_hf()
    # print(preview_data)
