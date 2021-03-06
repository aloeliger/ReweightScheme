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
from Configurations.Weights.TopPtReweightingModule.TopPtWeight import topPtWeight

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyqqHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyWminusHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyWplusHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyZHStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHLLTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHNNTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import dummyGGZHQQTTStyleWeight_Differential
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.DifferentialQCDAcceptanceWeight import ttHStyleWeight_Differential

from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyqqHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyVHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import dummyggZHRawQCDScaleAcceptance
from Configurations.Weights.QCDAcceptanceWeights.DifferentialQCDAcceptanceWeights.RawDifferentialQCDAcceptanceWeight import ttHRawQCDScaleAcceptance


from Configurations.Weights.ggHTheoryWeight.ggHTheoryWeight import  dummyggHTheoryWeight

from Configurations.ConfigDefinition import ReweightConfiguration

EWKConfiguration = ReweightConfiguration()
EWKConfiguration.name = "ttHtoNonbb"
EWKConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2017_Deep/ttH.root"
crossSectionWeight.sample = 'ttHtoNonbb'
crossSectionWeight.year = '2017'
totalEventsFile = ROOT.TFile.Open("/data/aloeliger/SMHTT_Selected_2017_Deep/VBF.root")
crossSectionWeight.totalEvents = totalEventsFile.eventCount.GetBinContent(2)
totalEventsFile.Close()
pileupWeight.year = '2017'
pileupWeight.sample = 'ttHtoNonbb'
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
    topPtWeight,
    PrefiringWeighting,

    dummyqqHStyleWeight_Differential,
    dummyWminusHStyleWeight_Differential,
    dummyWplusHStyleWeight_Differential,
    dummyZHStyleWeight_Differential,
    dummyGGZHLLTTStyleWeight_Differential,
    dummyGGZHNNTTStyleWeight_Differential,
    dummyGGZHQQTTStyleWeight_Differential,
    ttHStyleWeight_Differential,

    dummyggHRawQCDScaleAcceptance,
    dummyqqHRawQCDScaleAcceptance,
    dummyVHRawQCDScaleAcceptance,
    dummyggZHRawQCDScaleAcceptance,
    ttHRawQCDScaleAcceptance,

    dummyggHTheoryWeight,
]
