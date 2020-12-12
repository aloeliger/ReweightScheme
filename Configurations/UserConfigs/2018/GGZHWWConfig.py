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

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyqqHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyVHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import ggZHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyttHRawQCDScaleAcceptance


from Configurations.Weights.ggHTheoryWeight.ggHTheoryWeight import  dummyggHTheoryWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "GGZHWW"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/GGZHWW.root"
crossSectionWeight.sample = 'GGZHWW'
crossSectionWeight.year = '2018'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2018_Deep/GGZHWW.root")
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

    dummyggHRawQCDScaleAcceptance,
    dummyqqHRawQCDScaleAcceptance,
    dummyVHRawQCDScaleAcceptance,
    ggZHRawQCDScaleAcceptance,
    dummyttHRawQCDScaleAcceptance,

    dummyggHTheoryWeight,
]
