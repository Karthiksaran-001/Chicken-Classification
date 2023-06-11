from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier import logger
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n")
except Exception as e:
    logger.exception(e)
    raise e





