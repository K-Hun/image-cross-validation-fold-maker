from folding_utils import *


SOURCE_DATASET = 'bulky-dataset'
FOLDS_OUTPUT_DIR = 'folded'


start = time.time()
make_folds(SOURCE_DATASET, FOLDS_OUTPUT_DIR, CATEGORIES, 10)
print("it took", time.time() - start, "seconds.")