import ROOT

from Configurations.Weights.EmbeddedReweightingModule.EmbeddedWeight import embeddedWeight_2018 as embeddedWeight
from Configurations.Weights.EmbeddedReweightingModule.EmbeddedTriggerWeight import embeddedTriggerWeight_2018 as embeddedTriggerWeight
from Configurations.Weights.EmbeddedReweightingModule.EmbeddedTauIDWeight import embeddedTauIDWeight_2018 as embeddedTauIDWeight

from Configurations.ConfigDefinition import ReweightConfiguration

DYConfiguration = ReweightConfiguration()
DYConfiguration.name = 'Embedded'
DYConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/Embedded.root"
DYConfiguration.listOfWeights = [
    embeddedWeight,
    embeddedTriggerWeight,
    embeddedTauIDWeight,
    ]
