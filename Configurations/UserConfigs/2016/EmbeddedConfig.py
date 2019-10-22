import ROOT

from Configurations.Weights.EmbeddedReweightingModule.EmbeddedWeight import embeddedWeight_2016 as embeddedWeight

from Configurations.ConfigDefinition import ReweightConfiguration

DYConfiguration = ReweightConfiguration()
DYConfiguration.name = 'Embedded'
DYConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2016_Deep/Embedded.root"
DYConfiguration.listOfWeights = [
    embeddedWeight
    ]
