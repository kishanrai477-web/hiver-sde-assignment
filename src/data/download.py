"""Download data from sources"""

import os
import requests
from pathlib import Path


def download_dataset(url: str, output_path: str) -> None:
    """
    Download dataset from URL.
    
    Args:
        url: URL to download from
        output_path: Path to save the downloaded file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    
    print(f"Downloaded dataset to {output_path}")
