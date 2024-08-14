TRAIN_PATH      =  "/data/trainset/"
VALIDATION_PATH = "/data/validationset"
TEST_PATH       = "/data/testset/"
MODELS_PATH     = "./models/"


LANGUAGE   = "tamil"

ARCH = "crnn_vgg16_bn"
EPOCHS     = 100
BATCH_SIZE = 1024


RESUME      = True
RESUME_FILE = MODELS_PATH + ARCH + "_" + "tamil_cont" + ".pt"
