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
from Configurations.Weights.QCDAcceptanceWeights.VH_QCD_Acceptance import ZHStyleWeight_2018
from Configurations.Weights.PythiaPS.PartonShowerShapeWeight import partonShowerWeight

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyqqHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyWminusHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyWplusHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import ZHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHLLTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHNNTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHQQTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyttHStyleWeight_Differential

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyqqHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import VHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggZHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyttHRawQCDScaleAcceptance


from Configurations.Weights.ggHTheoryWeight.ggHTheoryWeight import  dummyggHTheoryWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "ZH"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/ZH.root"
crossSectionWeight.sample = 'ZH'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/ZH.root")
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
    ZHStyleWeight_2018,
    partonShowerWeight,

    dummyqqHStyleWeight_Differential,
    dummyWminusHStyleWeight_Differential,
    dummyWplusHStyleWeight_Differential,
    ZHStyleWeight_Differential,
    dummyGGZHLLTTStyleWeight_Differential,
    dummyGGZHNNTTStyleWeight_Differential,
    dummyGGZHQQTTStyleWeight_Differential,
    dummyttHStyleWeight_Differential,

    dummyggHRawQCDScaleAcceptance,
    dummyqqHRawQCDScaleAcceptance,
    VHRawQCDScaleAcceptance,
    dummyggZHRawQCDScaleAcceptance,
    dummyttHRawQCDScaleAcceptance,

    dummyggHTheoryWeight,
]
