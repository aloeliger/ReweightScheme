import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2017 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2017 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2017 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.TauFakeRateWeight import tauFakeRateWeight_2017 as tauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2017 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2017 as triggerWeight
from Configurations.Weights.ZPTReweightingModule.ZPTWeight import ZPTWeight_2017 as ZPTWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2017
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "EWKZLL"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2017_MCOnly_AntiIso_Deep/EWKZLL.root"
crossSectionWeight.sample = 'EWKZLL'
crossSectionWeight.year = '2017'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2017_MCOnly_AntiIso_Deep/EWKZLL.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2017'
pileupWeight.sample = 'EWK'
pileupWeight.InitPileupWeightings(pileupWeight)
EWKConfiguration.listOfWeights = [
    crossSectionWeight,
    muIDIsoWeight,
    muTrackingWeight,
    pileupWeight,
    tauFakeRateWeight,
    #tauIDWeight,
    triggerWeight,
    ZPTWeight,
    bTaggingWeight_2017,
    PrefiringWeighting,
]
