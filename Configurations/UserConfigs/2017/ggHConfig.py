import ROOT 

from Configurations.Weights.CrossSectionWeightingModule.CrossSectionWeight import crossSectionWeight
from Configurations.Weights.MuIDIsoReweightingModule.MuIDIsoWeight import muIDIsoWeight_2017 as muIDIsoWeight
from Configurations.Weights.MuTrackingWeightModule.MuTrackingWeight import muTrackingWeight_2017 as muTrackingWeight
from Configurations.Weights.PileupWeightingModule.PileupWeight import pileupWeight_2017 as pileupWeight
from Configurations.Weights.TauFakeRateWeightModule.TauFakeRateWeight import tauFakeRateWeight_2017 as tauFakeRateWeight
from Configurations.Weights.TauIDModule.TauIDWeight import tauIDWeight_2017 as tauIDWeight
from Configurations.Weights.TriggerSFModule.TriggerWeight import triggerWeight_2017 as triggerWeight
from Configurations.Weights.bTaggingWeightModule.bTaggingWeight import bTaggingWeight_2017
from Configurations.Weights.PrefiringWeightModule.PrefiringWeight import PrefiringWeighting
from Configurations.Weights.HiggsReweightingModule.HiggsPtReweighting import HiggsPtReweighting
from Configurations.Weights.QCDAcceptanceWeights.ggH_QCD_Acceptance import ggHStyleWeight_2017

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import ggHStyleWeight_Differential

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import ggHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyqqHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyVHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggZHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyttHRawQCDScaleAcceptance

from Configurations.Weights.ggHTheoryWeight.ggHTheoryWeight import  ggHTheoryWeight
from Configurations.Weights.ggHTheoryNormalizationWeight.ggHTheoryNormalizationWeight import ggHTheoryNormalizationWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "ggH"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2017_Deep/ggH.root"
crossSectionWeight.sample = 'ggH'
crossSectionWeight.year = '2017'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2017_Deep/ggH.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2017'
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
    bTaggingWeight_2017,
    PrefiringWeighting,
    HiggsPtReweighting,
    ggHStyleWeight_2017,
    ggHStyleWeight_Differential,
    ggHTheoryNormalizationWeight,
    
    ggHRawQCDScaleAcceptance,
    dummyqqHRawQCDScaleAcceptance,
    dummyVHRawQCDScaleAcceptance,
    dummyggZHRawQCDScaleAcceptance,
    dummyttHRawQCDScaleAcceptance,

    ggHTheoryWeight,
]
