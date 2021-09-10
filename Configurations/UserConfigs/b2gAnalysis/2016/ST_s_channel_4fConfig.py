import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight
from Configurations.Weights.b2gAnalysisWeights.pileupWeightingModule.pileupWeight import pileupWeight_2016


STConfig = ReweightConfiguration()
STConfig.name = 'ST_s-channel_4f'
STConfig.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(STConfig.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[STConfig.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

STConfig.inputFile = jsonInfo[STConfig.name]['file']

crossSectionWeight.XS = jsonInfo[STConfig.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents
try:
    crossSectionWeight.forcedGenWeight = jsonInfo[STConfig.name]['forcedGenWeight']
except KeyError:
    crossSectionWeight.forcedGenWeight = None


STConfig.listOfWeights = [
    crossSectionWeight,
    pileupWeight_2016,
]
