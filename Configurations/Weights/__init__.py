#quick initialization to help us find our weights
import os
localWeightPath, initFile = os.path.split(os.path.realpath(__file__))
localWeightDataPath = localWeightPath+"/Data/"
b2gWeightPath = localWeightDataPath+'/b2gWeightFiles/'
print("Reading weights from: "+localWeightDataPath)
