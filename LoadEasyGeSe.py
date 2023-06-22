def LoadEasyGeSeData(SPECIES=1):
	import numpy as np
	if SPECIES == 1:
		print('input is missing, inputs are:\n\"barley\"\n\"bean\"\n\"catfish\"\n\"lentil\"\n"maize\"\n"oyster\"\n"peanut\"\n"pig\"\n"pine\"\n"rice\"\n"soybean\"\n"wheatG\"\n')
		exit(1)
	XFILE = "https://zenodo.org/record/8041805/files/" + SPECIES + "X.csv?download=1"
	X = np.loadtxt(XFILE,delimiter=",",dtype=str,skiprows=1)
	YFILE = "https://zenodo.org/record/8041805/files/" + SPECIES + "Y.csv?download=1"
	Y = np.loadtxt(YFILE,delimiter=",",dtype=str,skiprows=1)
	if X.shape[0] == Y.shape[0]:
		print("Loaded " + str(X.shape[0]) + " genotypes")
		print("Loaded " + str(Y.shape[1]) + " phenotyes")
		print("Loaded " + str(X.shape[1]) + " markers")
		print("Please cite:")
	if SPECIES == "barley":
		print("Gonzalez, Maria Y., et al. \'Genomic prediction models trained with historical records enable populating the German ex situ genebank bio-digital resource center of barley (Hordeum sp.) with information on resistances to soilborne barley mosaic viruses.\' Theoretical and Applied Genetics 134 (2021): 2181-2196.")
	if SPECIES == "bean":
			print("Diaz, Santiago, et al. \'Genetic mapping for agronomic traits in a MAGIC population of common bean (Phaseolus vulgaris L.) under drought conditions.\' BMC genomics 21.1 (2020): 1-20.")
	if SPECIES == "pine":
		print("\tResende Jr, M. F. R., et al. \'Accuracy of genomic selection methods in a standard data set of loblolly pine (Pinus taeda L.).\' Genetics 190.4 (2012): 1503-1510.")
	if SPECIES == "catfish":
			print("Vu, Nguyen Thanh, et al. \'Accuracies of genomic predictions for disease resistance of striped catfish to Edwardsiella ictaluri using artificial intelligence algorithms.\' G3 12.1 (2022): jkab361.")
	if SPECIES == "lentil":
		print("Haile, Teketel A., et al. \'Genomic selection for lentil breeding: Empirical evidence.\' The Plant Genome 13.1 (2020): e20002.")
	if SPECIES == "maize":
		print("McFarland, Bridget A., et al. \'Maize genomes to fields (G2F): 2014–2017 field seasons: genotype, phenotype, climatic, soil, and inbred ear image datasets.\' BMC research notes 13.1 (2020): 1-6.")
	if SPECIES == "pig":
			print("Xie, L., et al. \'Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.\' Animal Genetics 52.5 (2021): 633-644.")
	if SPECIES == "oyster":
			print("McCarty, Alexandra J., Standish K. Allen Jr, and Louis V. Plough. \'Genome-wide analysis of acute low salinity tolerance in the eastern oyster Crassostrea virginica and potential of genomic selection for trait improvement.\' G3 12.1 (2022): jkab368.")
	if SPECIES == "pig":
			print("Xie, L., et al. \'Accurate prediction and genome‐wide association analysis of digital intramuscular fat content in longissimus muscle of pigs.\' Animal Genetics 52.5 (2021): 633-644.")
	if SPECIES == "rice":
			print("Zhao, Keyan, et al. \'Genome-wide association mapping reveals a rich genetic architecture of complex traits in Oryza sativa.\' Nature communications 2.1 (2011): 467.")
	if SPECIES == "soybean":
			print("Kaler, Avjinder S., et al. \'Genome-wide association mapping of canopy wilting in diverse soybean genotypes.\' Theoretical and Applied Genetics 130 (2017): 2203-2217.\nKaler, Avjinder S., et al. \'Genome‐wide association mapping of carbon isotope and oxygen isotope ratios in diverse soybean genotypes.\' Crop science 57.6 (2017): 3085-3100.")
	if SPECIES == "wheatG":
			print("Gogna, Abhishek, et al. \'Gabi wheat a panel of European elite lines as central stock for wheat genetic research.\' Scientific Data 9.1 (2022): 538.")
	return X, Y
            

