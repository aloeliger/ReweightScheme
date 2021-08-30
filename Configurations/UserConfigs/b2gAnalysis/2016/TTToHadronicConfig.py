import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

TTToHadronicConfig = ReweightConfiguration()
TTToHadronicConfig.name = 'TTToHadronic'
TTToHadronicConfig.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(TTToHadronicConfig.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[TTToHadronicConfig.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

TTToHadronicConfig.inputFile = jsonInfo[TTToHadronicConfig.name]['file']

crossSectionWeight.XS = jsonInfo[TTToHadronicConfig.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

TTToHadronicConfig.listOfWeights = [
    crossSectionWeight,
]
