import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2016 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2016 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2016 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.TauFakeRateWeight import tauFakeRateWeight_2016 as tauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2016 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2016 as triggerWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2016
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting
from Configurations.Weights.HiggsReweightingModule.HiggsPtReweighting import HiggsPtReweighting
from Configurations.Weights.QCDAcceptanceWeights.ggH_QCD_Acceptance import ggHStyleWeight_2016

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import ggHStyleWeight_Differential

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import ggHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyqqHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyVHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggZHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyttHRawQCDScaleAcceptance

from Configurations.Weights.ggHTheoryNormalizationWeight.ggHTheoryNormalizationWeight import ggHTheoryNormalizationWeight
from Configurations.Weights.ggHTheoryWeight.ggHTheoryWeight import  ggHTheoryWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "ggH"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2016_Deep/ggH.root"
crossSectionWeight.sample = 'ggH'
crossSectionWeight.year = '2016'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2016_Deep/ggH.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2016'
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
    bTaggingWeight_2016,
    PrefiringWeighting,
    HiggsPtReweighting,
    ggHStyleWeight_2016,
    ggHStyleWeight_Differential,

    ggHRawQCDScaleAcceptance,
    dummyqqHRawQCDScaleAcceptance,
    dummyVHRawQCDScaleAcceptance,
    dummyggZHRawQCDScaleAcceptance,
    dummyttHRawQCDScaleAcceptance,

    ggHTheoryNormalizationWeight,
    ggHTheoryWeight
]
