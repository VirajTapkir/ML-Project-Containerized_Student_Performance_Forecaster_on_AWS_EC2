import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    try:
        logging.info("Execution of the training pipeline has started")

        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Train path: {train_data_path}, Test path: {test_data_path}")

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logging.info("Data Transformation completed")

        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
        logging.info("Model Training completed")

    except Exception as e:
        logging.info("Exception occured in the training pipeline")
        raise CustomException(e, sys)