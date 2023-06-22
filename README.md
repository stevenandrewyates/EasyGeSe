# EasyGeSe

![](https://github.com/stevenandrewyates/EasyGeSe/blob/main/EasyGeSe.png)

EasyGeSe is a comprehensive [database](https://zenodo.org/record/8041805) for genomic selection with data records from diverse species such as [barley](https://link.springer.com/article/10.1007/s00122-021-03815-0), [common bean](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-020-07213-6), [catfish](https://academic.oup.com/g3journal/article/12/1/jkab361/6408442),  [lentil](https://doi.org/10.1002/tpg2.20002), [loblolly pine](https://academic.oup.com/genetics/article/190/4/1503/6064084), [Eastern oyster](https://doi.org/10.1093/g3journal/jkab368), [maize](https://doi.org/10.1186/s13104-020-4922-8), [pig](https://doi.org/10.1111/age.13121), [rice](https://www.nature.com/articles/ncomms1467), [soybean](https://doi.org/10.1007/s00122-017-2951-z) and [wheat](https://doi.org/10.1038/s41597-022-01651-5). 

The data are formatted, filtered and arranged in easy to use formats; with functions in R and Python for easy loading

# Code
Find out out to use EasyGeSe with your favourite programs below
## R
An example how to load the data into R and use [BGLR](https://cran.r-project.org/web/packages/BGLR/index.html) to make predictions
```
library(BGLR)    # load the BGLR package
source("LoadEasyGeSe.R") # load EasyGeSe R code for downloading data
LoadEasyGeSe("lentil") # load the lentil data
y <- Y[,1]	# extract the first trait
tst <- sample(1:length(y),size=(round(length(y)/5)))    # make a subset of 20% testing data
y[tst] <- NA    # remove the testing data phenotypes
ETA <- list(MRK = list(X = X, model = "BL"))    # prepare the training model
fmBL <- BGLR(y = y, ETA = ETA, nIter = 5000, burnIn = 1000, saveAt = "BL_")    # run the model
cor(Y[tst,1],fmBL$yHat[tst]);    # check the R-squared 
# 0.8104526
sqrt(mean((Y[tst,1] - fmBL$yHat[tst])^2))    # check RMSE
# 2.041484
```

## Python

Use [sklearn](https://scikit-learn.org/stable/) to make predictions using EasyGeSe

```
from sklearn.model_selection import train_test_split    # load the train test split function
from sklearn.svm import SVR # load the support vector regressor
import numpy as np    # load numpy
from LoadEasyGeSe import * # load the EasyGeSe function
X, Y = LoadEasyGeSeData(‘lentil’) # download the lentil dataset
x_train, x_test, y_train, y_test = train_test_split(X[:,1:], Y[:,1].astype(‘float64’), test_size=0.2, random_state=0) # split the data and select the first trait
regressor = SVR().fit(x_train, y_train)     # run the model
np.corrcoef(regressor.predict(x_test), y_test)[1,0]    # check the R-squared
# 0.669798536408507
np.sqrt(np.mean((regressor.predict(x_test) - y_test)**2))    # check RMSE
# 2.23977261800874072
```
## Terminal
Use [CropGBM](https://ibreeding.github.io/) to make predictions from the terminal with some helper scripts.
```
python DownloadEasyGeSe.py lentil 1 1 # use the script here to download the 'lentil' data and use 20% for testing and 80% for training (split using sklearn). You also specify the which trait (column, 1) and which "random_state" to use. This will download four files the training data "lentil_xtrain_1.txt" (genotypic) and "lentil_ytrain_1.txt" (phenotypic), and for the testing data "lentil_xtest_1.txt" (genotypic) and "lentil_ytest_1.txt" (phenotypic)
mkdir cropgbm_results # make a directory for the output
cropgbm -o cropgbm_results/ -e -t --traingeno lentil_xtrain_1.txt --trainphe lentil_ytrain_1.txt # run CropGBM to estimate marker effects
cropgbm -o cropgbm_results/ -e -p --testgeno lentil_xtest_1.txt --modelfile-path cropgbm_results/engine/lentil_xtrain_1.lgb_model # use CropGBM to predict the phenotype of the testing data
python predict PredictEasyGeSe.py lentil_ytest_1.txt cropgbm_results/engine/lentil_xtest_1.predict # finally use a python script here to measure the correlation and root-mean-square (RMSE) between the observed (testing) and predicted phenotype
 

```
For all tools the options are:

| Option | Reference |
| ------ | ------ |
| "barley" | Gonzalez, Maria Y., et al. \'Genomic prediction models trained with historical records enable populating the German ex situ genebank bio-digital resource center of barley (Hordeum sp.) with information on resistances to soilborne barley mosaic viruses.\' Theoretical and Applied Genetics 134 (2021): 2181-2196. |
| "bean" | Diaz, Santiago, et al. \'Genetic mapping for agronomic traits in a MAGIC population of common bean (Phaseolus vulgaris L.) under drought conditions.\' BMC genomics 21.1 (2020): 1-20. |
| "pine" | Resende Jr, M. F. R., et al. \'Accuracy of genomic selection methods in a standard data set of loblolly pine (Pinus taeda L.).\' Genetics 190.4 (2012): 1503-1510. |
| "catfish" | Vu, Nguyen Thanh, et al. \'Accuracies of genomic predictions for disease resistance of striped catfish to Edwardsiella ictaluri using artificial intelligence algorithms.\' G3 12.1 (2022): jkab361. |
| "lentil" | Haile, Teketel A., et al. \'Genomic selection for lentil breeding: Empirical evidence.\' The Plant Genome 13.1 (2020): e20002. |
| "maize" | McFarland, Bridget A., et al. \'Maize genomes to fields (G2F): 2014–2017 field seasons: genotype, phenotype, climatic, soil, and inbred ear image datasets.’ BMC research notes 13.1 (2020): 1-6. |
| "pig" | Xie, L., et al. ‘Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.’ Animal Genetics 52.5 (2021): 633-644. |
| "oyster" | McCarty, Alexandra J., Standish K. Allen Jr, and Louis V. Plough. ‘Genome-wide analysis of acute low salinity tolerance in the eastern oyster Crassostrea virginica and potential of genomic selection for trait improvement.’ G3 12.1 (2022): jkab368. |
| "pig" | Xie, L., et al. ‘Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.’ Animal Genetics 52.5 (2021): 633-644. |
|  "rice" | Zhao, Keyan, et al. ‘Genome-wide association mapping reveals a rich genetic architecture of complex traits in Oryza sativa.’ Nature communications 2.1 (2011): 467. |
| "soybean" | Kaler, Avjinder S., et al. ‘Genome-wide association mapping of canopy wilting in diverse soybean genotypes.’ Theoretical and Applied Genetics 130 (2017): 2203-2217.\nKaler, Avjinder S., et al. ‘Genome‐wide association mapping of carbon isotope and oxygen isotope ratios in diverse soybean genotypes.’ Crop science 57.6 (2017): 3085-3100. |
| "wheatG" | Gogna, Abhishek, et al. ‘Gabi wheat a panel of European elite lines as central stock for wheat genetic research.’ Scientific Data 9.1 (2022): 538. |

