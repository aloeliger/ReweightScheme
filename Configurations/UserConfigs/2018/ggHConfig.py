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
from Configurations.Weights.HiggsReweightingModule.HiggsPtReweighting import HiggsPtReweighting
from Configurations.Weights.QCDAcceptanceWeights.ggH_QCD_Acceptance import ggHStyleWeight_2018
from Configurations.Weights.PythiaPS.PartonShowerShapeWeight import partonShowerWeight
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import ggHStyleWeight_Differential
from Configurations.Weights.ggHTheoryNormalizationWeight.ggHTheoryNormalizationWeight import ggHTheoryNormalizationWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "ggH"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/ggH.root"
crossSectionWeight.sample = 'ggH'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/ggH.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2018'
pileupWeight.sample = 'ggH'
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
    HiggsPtReweighting,
    ggHStyleWeight_2018,
    partonShowerWeight,
    ggHStyleWeight_Differential,
    ggHTheoryNormalizationWeight,
]
