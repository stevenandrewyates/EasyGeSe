import sys
import numpy as np
from LoadEasyGeSe import *
from sklearn.model_selection import train_test_split

SPECIES = "Unknown"
PHENO = "Unknown"
RANDOMSTATE = "Unknown"

SPECIES = sys.argv[1]
PHENO = int(sys.argv[2])
RANDOMSTATE = int(sys.argv[3])


X, Y = LoadEasyGeSeData(SPECIES)

x_train, x_test, y_train, y_test = train_test_split(X, Y[:,[0,PHENO]], test_size=0.2,random_state=RANDOMSTATE)
print("")
XTRAINFILE = SPECIES + "_xtrain_" + str(RANDOMSTATE) + ".txt"
np.savetxt(XTRAINFILE, x_train, fmt='%s',delimiter=",")
print("Saved genetic training data to:\t" +XTRAINFILE )

YTRAINFILE = SPECIES + "_ytrain_" + str(RANDOMSTATE) + ".txt"
np.savetxt(YTRAINFILE, y_train, fmt='%s',delimiter=",")
print("Saved trait training data to:\t" +YTRAINFILE )

XTESTFILE = SPECIES + "_xtest_" + str(RANDOMSTATE) + ".txt"
np.savetxt(XTESTFILE, x_test, fmt='%s',delimiter=",")
print("Saved genetic testing data to:\t" +XTESTFILE )

YTESTFILE = SPECIES + "_ytest_" + str(RANDOMSTATE) + ".txt"
np.savetxt(YTESTFILE, y_test, fmt='%s',delimiter=",")
print("Saved trait testing data to:\t" +YTESTFILE )
print("")
print("If you want to run CropGBM use:")
print("mkdir cropgbm_results")
print("cropgbm -o cropgbm_results/ -e -t --traingeno " + XTRAINFILE +" --trainphe " +YTRAINFILE)

MODEL = XTRAINFILE.replace(".txt","")
PREDICT = XTESTFILE.replace(".txt",".predict")
print("cropgbm -o cropgbm_results/ -e -p --testgeno " + XTESTFILE + " --modelfile-path cropgbm_results/engine/" +MODEL +".lgb_model")
print("python PredictEasyGeSe.py " + YTESTFILE + " cropgbm_results/engine/" + PREDICT)
print("")
print("Cite CropGBM using:")
print("Xu, Yuetong, John D. Laurie, and Xiangfeng Wang. 'CropGBM: An ultra-efficient machine learning toolbox for genomic selection-assisted breeding in crops.' Accelerated Breeding of Cereal Crops (2022): 133-150.")
