import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

TTTo2L2NuConfig = ReweightConfiguration()
TTTo2L2NuConfig.name = 'TTTo2L2Nu'
TTTo2L2NuConfig.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(TTTo2L2NuConfig.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[TTTo2L2NuConfig.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

TTTo2L2NuConfig.inputFile = jsonInfo[TTTo2L2NuConfig.name]['file']

crossSectionWeight.XS = jsonInfo[TTTo2L2NuConfig.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

TTTo2L2NuConfig.listOfWeights = [
    crossSectionWeight,
]
