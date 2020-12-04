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
from Configurations.Weights.QCDAcceptanceWeights.qqH_QCD_Acceptance import VBFStyleWeight_2018
from Configurations.Weights.PythiaPS.PartonShowerShapeWeight import partonShowerWeight
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import qqHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import qqHRawQCDScaleAcceptance

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "VBF"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/VBF.root"
crossSectionWeight.sample = 'VBF'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/VBF.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2018'
pileupWeight.sample = 'VBF'
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
    VBFStyleWeight_2018,
    partonShowerWeight,
    qqHStyleWeight_Differential,
    qqHRawQCDScaleAcceptance,
]
