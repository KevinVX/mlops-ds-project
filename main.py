from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline


logger.info("Welcome to the Data Science Project")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

