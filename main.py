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


from textsummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline

try:
   logger.info(f"\n\n>>>>>> DATA TRANSFORMATION STARTED <<<<<<\n\n") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f"\n\n>>>>>> DATA TRANSFORMATION COMPLETED <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e


from textsummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline

try:
   logger.info(f"\n\n>>>>>> DATA TRAINER STARTED <<<<<<\n\n") 
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f"\n\n>>>>>> DATA TRAINER COMPLETED <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e



from textsummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

try:
   logger.info(f"\n\n>>>>>> DATA EVALUATION STARTED <<<<<<\n\n") 
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f"\n\n>>>>>> DATA EVALUATION COMPLETED <<<<<<\n\n")
except Exception as e:
        logger.exception(e)
        raise e
