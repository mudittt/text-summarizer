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
