import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2018 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2018 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2018 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.TauFakeRateWeight import tauFakeRateWeight_2018 as tauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2018 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2018 as triggerWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2018
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting
from Configurations.Weights.QCDAcceptanceWeights.ggVH_QCD_Acceptance import ggZHLLTTStyleWeight_2018
from Configurations.Weights.PythiaPS.PartonShowerShapeWeight import partonShowerWeight
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import GGZHLLTTStyleWeight_Differential

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "GGZHLLTT"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/GGZHLLTT.root"
crossSectionWeight.sample = 'GGZHLLTT'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/GGZHLLTT.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2018'
pileupWeight.sample = 'ZH'
pileupWeight.InitPileupWeightings(pileupWeight)
EWKConfiguration.listOfWeights = [
    crossSectionWeight,
    muIDIsoWeight,
    muTrackingWeight,
    pileupWeight,
    tauFakeRateWeight,
    tauIDWeight,
    triggerWeight,
    bTaggingWeight_2018,
    #PrefiringWeighting,
    ggZHLLTTStyleWeight_2018,
    partonShowerWeight,
    GGZHLLTTStyleWeight_Differential,
]
