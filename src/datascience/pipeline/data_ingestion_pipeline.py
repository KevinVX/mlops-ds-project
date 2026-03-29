
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.config.configuration import ConfiurationManager
from src.datascience import logger

STAGE_NMAE = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfiurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NMAE} started <<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {STAGE_NMAE} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e