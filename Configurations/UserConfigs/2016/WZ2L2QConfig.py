import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2016 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2016 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2016 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.eTauFakeRateWeight import eTauFakeRateWeight_2016 as eTauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2016 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2016 as triggerWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2016
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "WZ2L2Q"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2016_Deep/WZ2L2Q.root"
crossSectionWeight.sample = 'WZ2L2Q'
crossSectionWeight.year = '2016'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2016_Deep/WZ2L2Q.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2016'
pileupWeight.sample = 'WZ'
pileupWeight.InitPileupWeightings(pileupWeight)
EWKConfiguration.listOfWeights = [
    crossSectionWeight,
    muIDIsoWeight,
    muTrackingWeight,
    pileupWeight,
    eTauFakeRateWeight,
    tauIDWeight,
    triggerWeight,
    bTaggingWeight_2016,
    PrefiringWeighting
]
