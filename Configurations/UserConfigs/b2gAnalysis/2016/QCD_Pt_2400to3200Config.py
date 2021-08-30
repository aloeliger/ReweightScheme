import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

QCD_Pt_2400to3200Config = ReweightConfiguration()
QCD_Pt_2400to3200Config.name = 'QCD_Pt_2400to3200'
QCD_Pt_2400to3200Config.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(QCD_Pt_2400to3200Config.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[QCD_Pt_2400to3200Config.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

QCD_Pt_2400to3200Config.inputFile = jsonInfo[QCD_Pt_2400to3200Config.name]['file']

crossSectionWeight.XS = jsonInfo[QCD_Pt_2400to3200Config.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

QCD_Pt_2400to3200Config.listOfWeights = [
    crossSectionWeight,
]
