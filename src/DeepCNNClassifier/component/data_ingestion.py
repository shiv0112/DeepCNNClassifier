import os
import urllib.request as request
from zipfile import ZipFile
from DeepCNNClassifier.entity import DataIngestionConfig
from DeepCNNClassifier import logger
from DeepCNNClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File of size: {get_size(Path(self.config.local_data_file))} KB already exists")
    
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf:ZipFile, f:str, working_dir:str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            logger.info("Removing unwanted files")
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            logger.info("Removing empty files")
            os.remove(target_filepath)


    def unzip_and_clean(self):
        logger.info("unzipping files")
        with ZipFile(file=self.config.local_data_file,mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for file in tqdm(updated_list_of_files):
                self._preprocess(zf, file, self.config.unzip_dir)

    def create_test_data(self):
        """
        separte 30% of data into test data
        """
        pass