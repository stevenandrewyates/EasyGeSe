LoadEasyGeSe <- function(INPUT) 
{
text <- 'input is missing, inputs are:\n\"barley\"\n\"bean\"\n\"catfish\"\n\"lentil\"\n"maize\"\n"oyster\"\n"peanut\"\n"pig\"\n"pine\"\n"rice\"\n"soybean\"\n"wheatG\"\n'
if(missing(INPUT)) stop(writeLines(text))
Y <<- read.csv(paste("https://zenodo.org/record/8041805/files/",INPUT,"Y.csv?download=1",sep=""),row.names=1)
X <<- read.csv(paste("https://zenodo.org/record/8041805/files/",INPUT,"X.csv?download=1",sep=""),row.names=1)
head(X)
if(dim(X)[1] == dim(Y)[1])
{writeLines(paste("Loaded ",dim(X)[1], " genotypes",sep=""))
writeLines(paste("Loaded ",dim(Y)[2], " phenotyes",sep=""))
writeLines(paste("Loaded ",dim(X)[2], " markers",sep=""))
writeLines("Please cite:")
if(INPUT == "barley") {writeLines("Gonzalez, Maria Y., et al. \'Genomic prediction models trained with historical records enable populating the German ex situ genebank bio-digital resource center of barley (Hordeum sp.) with information on resistances to soilborne barley mosaic viruses.\' Theoretical and Applied Genetics 134 (2021): 2181-2196.")}

if(INPUT == "bean") {writeLines("Diaz, Santiago, et al. \'Genetic mapping for agronomic traits in a MAGIC population of common bean (Phaseolus vulgaris L.) under drought conditions.\' BMC genomics 21.1 (2020): 1-20.")}

if(INPUT == "pine") {writeLines("\tResende Jr, M. F. R., et al. \'Accuracy of genomic selection methods in a standard data set of loblolly pine (Pinus taeda L.).\' Genetics 190.4 (2012): 1503-1510.")}

if(INPUT == "catfish") {writeLines("Vu, Nguyen Thanh, et al. \'Accuracies of genomic predictions for disease resistance of striped catfish to Edwardsiella ictaluri using artificial intelligence algorithms.\' G3 12.1 (2022): jkab361.")}

if(INPUT == "lentil") {writeLines("Haile, Teketel A., et al. \'Genomic selection for lentil breeding: Empirical evidence.\' The Plant Genome 13.1 (2020): e20002.")}

if(INPUT == "maize") {writeLines("McFarland, Bridget A., et al. \'Maize genomes to fields (G2F): 2014–2017 field seasons: genotype, phenotype, climatic, soil, and inbred ear image datasets.\' BMC research notes 13.1 (2020): 1-6.")}

if(INPUT == "pig") {writeLines("Xie, L., et al. \'Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.\' Animal Genetics 52.5 (2021): 633-644.")}

if(INPUT == "oyster") {writeLines("McCarty, Alexandra J., Standish K. Allen Jr, and Louis V. Plough. \'Genome-wide analysis of acute low salinity tolerance in the eastern oyster Crassostrea virginica and potential of genomic selection for trait improvement.\' G3 12.1 (2022): jkab368.")}

if(INPUT == "pig") {writeLines("Xie, L., et al. \'Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.\' Animal Genetics 52.5 (2021): 633-644.")}


if(INPUT == "rice") {writeLines("Zhao, Keyan, et al. \'Genome-wide association mapping reveals a rich genetic architecture of complex traits in Oryza sativa.\' Nature communications 2.1 (2011): 467.")}


if(INPUT == "soybean") {writeLines("Kaler, Avjinder S., et al. \'Genome-wide association mapping of canopy wilting in diverse soybean genotypes.\' Theoretical and Applied Genetics 130 (2017): 2203-2217.\nKaler, Avjinder S., et al. \'Genome‐wide association mapping of carbon isotope and oxygen isotope ratios in diverse soybean genotypes.\' Crop science 57.6 (2017): 3085-3100.")}


if(INPUT == "wheatG") {writeLines("Gogna, Abhishek, et al. \'Gabi wheat a panel of European elite lines as central stock for wheat genetic research.\' Scientific Data 9.1 (2022): 538.")}

} else {writeLines("Error, number of genotypes do not match")}


}
