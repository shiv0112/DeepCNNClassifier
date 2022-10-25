from DeepCNNClassifier.config import ConfigurationManager
from DeepCNNClassifier.component import DataIngestion
from DeepCNNClassifier import logger 


STAGE_NAME ="Data Ingestion"


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> Stage: {STAGE_NAME} ended <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e