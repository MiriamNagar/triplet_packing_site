import logging


# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     # stream=sys.stdout,
#     handlers=[
#         logging.StreamHandler(),  # Log to console
#         logging.FileHandler('algorithm.log', mode='w', encoding="utf-8")  # Log to file
#     ]
# )

# logger = logging.getLogger(__name__)
# logger.info("Logger initialized.")

algo_logger = logging.getLogger("prtpy.packing.triplet_packing")
algo_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("algorithm.log", mode="w", encoding="utf-8")
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))

algo_logger.addHandler(file_handler)
algo_logger.propagate = False  # Optional: prevents double logging via root
