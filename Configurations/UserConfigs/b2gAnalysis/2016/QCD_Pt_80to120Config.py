import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

QCD_Pt_80to120Config = ReweightConfiguration()
QCD_Pt_80to120Config.name = 'QCD_Pt_80to120'
QCD_Pt_80to120Config.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(QCD_Pt_80to120Config.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[QCD_Pt_80to120Config.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

QCD_Pt_80to120Config.inputFile = jsonInfo[QCD_Pt_80to120Config.name]['file']

crossSectionWeight.XS = jsonInfo[QCD_Pt_80to120Config.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

QCD_Pt_80to120Config.listOfWeights = [
    crossSectionWeight,
]
