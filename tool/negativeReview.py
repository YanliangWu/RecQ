### This is a helper script to generate negative dataset
### Input all hyperparams before using the scriipt

FEEDBACK_COLUMN_ID = 2
NEGATIVE_THRESHOLD = 2
DATASET_PATH = '../dataset/filmtrust/ratings.txt'
OUTPUT_PATH =  '../dataset/filmtrust/ratings_n.txt'

def generateNegativeDataset(path, feedback_col_id, negative_threshold, output_path):
    output_file = open(output_path, "a")
    with open(path) as f:
        for line in f:
            record = line.strip().split()
            if float(record[feedback_col_id]) <= negative_threshold:
                    output_file.write(line)


generateNegativeDataset(DATASET_PATH, FEEDBACK_COLUMN_ID, NEGATIVE_THRESHOLD, OUTPUT_PATH)

