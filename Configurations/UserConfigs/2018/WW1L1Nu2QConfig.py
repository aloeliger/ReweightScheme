import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2018 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2018 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2018 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.eTauFakeRateWeight import eTauFakeRateWeight_2018 as eTauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2018 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2018 as triggerWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "WW1L1Nu2Q"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/WW1L1Nu2Q.root"
crossSectionWeight.sample = 'WW1L1Nu2Q'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/WW1L1Nu2Q.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2018'
pileupWeight.sample = 'WW'
pileupWeight.InitPileupWeightings(pileupWeight)
EWKConfiguration.listOfWeights = [
    crossSectionWeight,
    muIDIsoWeight,
    muTrackingWeight,
    pileupWeight,
    eTauFakeRateWeight,
    tauIDWeight,
    triggerWeight,
    bTaggingWeight,
    #PrefiringWeighting,
]
