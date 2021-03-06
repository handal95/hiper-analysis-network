import argparse

# from model.run import run
from model.utils.logger import Logger, init_logger
from model.data.prepare import prepare_data
from model.loader import DataLoader
from model.analyzer import DataAnalyzer
from model.model import ModelGenerator
from model.preprocessor import PreProcessor


argparser = argparse.ArgumentParser(description="cli command")

argparser.add_argument("-t", "--type", help="type of target dataset")

argparser.add_argument("-s", "--skip", help="skipped process")


def _main_(args):
    init_logger()
    logger = Logger()

    logger.log("Step 0 >> Setting ")

    logger.log("Step 1 >> Data Preparation")
    logger.log("- 1 : Data Collection ", level=1)
    loader = DataLoader(config_path="./config.json")

    logger.log("- 2 : Data Analization ", level=1)
    analyzer = DataAnalyzer(
        config_path="./config.json",
        dataset=loader.dataset,
        metaset=loader.metaset,
    )
    analyzer.analize()

    logger.log("Step 3 >> Model Generation")
    model_generator = ModelGenerator(config_path="./config.json")
    models = model_generator.models

    logger.log("Step 4 >> Data Preprocess")
    preprocessor = PreProcessor(
        config_path="./config.json",
        dataset=analyzer.dataset,
        metaset=analyzer.metaset,
    )

    # (x_value, x_label), (y_value, y_label) = preprocessor.label_split()

    logger.log("Step 5 >> Model Evaluation")
    models = model_generator.fit_model(
        dataset=analyzer.dataset,
        metaset=analyzer.metaset,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    opt = parser.parse_args()
    _main_(opt)
