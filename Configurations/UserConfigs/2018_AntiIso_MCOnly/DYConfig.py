import ROOT

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2018 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2018 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2018 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.TauFakeRateWeight import tauFakeRateWeight_2018 as tauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2018 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2018 as triggerWeight
from Configurations.Weights.ZPTReweightingModule.ZPTWeight import ZPTWeight_2018 as ZPTWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2018
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting

from Configurations.ConfigDefinition import ReweightConfiguration

DYConfiguration = ReweightConfiguration()
DYConfiguration.name = 'DY'
DYConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_MCOnly_AntiIso_Deep/DY.root"
#Do set-up
crossSectionWeight.sample = 'DY'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open(DYConfiguration.inputFile)
crossSectionWeight.totalEvents=totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2018'
pileupWeight.sample = 'DY'
pileupWeight.InitPileupWeightings(pileupWeight)
DYConfiguration.listOfWeights = [
    crossSectionWeight,
    muIDIsoWeight,
    muTrackingWeight,
    pileupWeight,
    tauFakeRateWeight,
    #tauIDWeight,
    triggerWeight,
    ZPTWeight,
    bTaggingWeight_2018,
    #PrefiringWeighting,
    ]
