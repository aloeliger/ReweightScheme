import ROOT
import os
import json

from Configurations.ConfigDefinition import ReweightConfiguration
from Configurations.Weights.b2gAnalysisWeights.crossSectionWeighting.crossSectionWeight import crossSectionWeight as crossSectionWeight

QCD_Pt_170to300Config = ReweightConfiguration()
QCD_Pt_170to300Config.name = 'QCD_Pt_170to300'
QCD_Pt_170to300Config.jsonSampleFile = os.environ['CMSSW_BASE']+'/src/bbtautauAnalysisScripts/analysisCore/config/samples/2016_Samples.json'

with open(QCD_Pt_170to300Config.jsonSampleFile,'r') as jsonFile:
    jsonInfo = json.load(jsonFile)
theFile = ROOT.TFile(jsonInfo[QCD_Pt_170to300Config.name]['file'])
totalNumberOfEvents = theFile.cutflow.GetBinContent(1)
theFile.Close()

QCD_Pt_170to300Config.inputFile = jsonInfo[QCD_Pt_170to300Config.name]['file']

crossSectionWeight.XS = jsonInfo[QCD_Pt_170to300Config.name]['XS'] * 1e-12 #XS in pb
crossSectionWeight.timePeriod = '2016'
crossSectionWeight.totalNumberOfEvents = totalNumberOfEvents

QCD_Pt_170to300Config.listOfWeights = [
    crossSectionWeight,
]
