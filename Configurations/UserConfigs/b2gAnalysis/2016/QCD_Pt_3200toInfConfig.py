import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

QCD_Pt_3200toInfConfig = ReweightConfiguration()
QCD_Pt_3200toInfConfig.name = 'QCD_Pt_3200toInf'
QCD_Pt_3200toInfConfig.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(QCD_Pt_3200toInfConfig.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[QCD_Pt_3200toInfConfig.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

QCD_Pt_3200toInfConfig.inputFile = jsonInfo[QCD_Pt_3200toInfConfig.name]['file']

crossSectionWeight.XS = jsonInfo[QCD_Pt_3200toInfConfig.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

QCD_Pt_3200toInfConfig.listOfWeights = [
    crossSectionWeight,
]
