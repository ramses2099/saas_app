from pathlib import Path

import requests


def download_to_local(url: str, out_path: str, parent_mkdir:bool=True) -> str:
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib Path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading file from {url}: {e}")
        return False
    