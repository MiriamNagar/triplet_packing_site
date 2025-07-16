import logging

# Algorithm logger definition
algo_logger = logging.getLogger("prtpy")
algo_logger.setLevel(logging.INFO)
algo_logger.propagate = False  # Prevent duplicate logs if needed
