import argparse
import subprocess
from config import *

parser = argparse.ArgumentParser(description="Test run", formatter_class=argparse.ArgumentDefaultsHelpFormatter,)
parser.add_argument("--data", type=str, dest='data', default=TEST_PATH + LANGUAGE + "/", help="path to the input data file")
parser.add_argument("--lang", type=str, dest='lang', default=LANGUAGE, help="language of images")
parser.add_argument("--model", type=str, dest='model', default=RESUME_FILE, help="path to the trained model")
args = parser.parse_args()


command = ["python", "./doctr/references/recognition/train_pytorch.py", ARCH, "--train_path", TRAIN_PATH + LANGUAGE + "/", "--val_path", args.data, "--epochs", str(1), "--device", str(0), "--vocab", args.lang, "-b", str(1), "--test-only", "--resume", args.model]


# command = ["python", "./doctr/references/recognition/evaluate_pytorch.py", ARCH , "--dataset", TEST_PATH + LANGUAGE + '/', "--device", str(1), "--vocab", LANGUAGE, "-b", str(BATCH_SIZE), "--resume", RESUME_FILE ]

subprocess.run(command)
