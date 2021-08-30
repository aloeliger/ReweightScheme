import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

TTToSemiLeptonicConfig = ReweightConfiguration()
TTToSemiLeptonicConfig.name = 'TTToSemiLeptonic'
TTToSemiLeptonicConfig.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(TTToSemiLeptonicConfig.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[TTToSemiLeptonicConfig.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

TTToSemiLeptonicConfig.inputFile = jsonInfo[TTToSemiLeptonicConfig.name]['file']

crossSectionWeight.XS = jsonInfo[TTToSemiLeptonicConfig.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

TTToSemiLeptonicConfig.listOfWeights = [
    crossSectionWeight,
]
