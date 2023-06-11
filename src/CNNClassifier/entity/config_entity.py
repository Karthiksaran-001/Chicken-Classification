from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    aws_access_key: str
    aws_secret_key: str
    bucket_name: str
    bucket_filename: str
    local_data_file: str
    unzip_dir: Path