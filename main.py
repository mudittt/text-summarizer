from textsummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.logging import logger 


try:
   logger.info(f"\n\n>>>>>> DATA INGESTION STARTED <<<<<<\n\n") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f"\n\n>>>>>> DATA INGESTION COMPLETED <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e


from textsummarizer.pipeline.data_validation import DataValidationTrainingPipeline

try:
   logger.info(f"\n\n>>>>>> DATA VALIDATION STARTED <<<<<<\n\n") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f"\n\n>>>>>> DATA VALIDATION COMPLETED <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e
