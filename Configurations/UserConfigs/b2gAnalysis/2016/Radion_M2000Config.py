import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

Radion_M2000Config = ReweightConfiguration()
Radion_M2000Config.name = 'Radion_M2000'
Radion_M2000Config.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(Radion_M2000Config.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[Radion_M2000Config.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

Radion_M2000Config.inputFile = jsonInfo[Radion_M2000Config.name]['file']

crossSectionWeight.XS = jsonInfo[Radion_M2000Config.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

Radion_M2000Config.listOfWeights = [
    crossSectionWeight,
]
