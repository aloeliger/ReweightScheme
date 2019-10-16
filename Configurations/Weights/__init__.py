#quick initialization to help us find our weights
import os
localWeightPath, initFile = os.path.split(os.path.realpath(__file__))
localWeightDataPath = localWeightPath+"/Data/"
print("Reading weights from: "+localWeightDataPath)
