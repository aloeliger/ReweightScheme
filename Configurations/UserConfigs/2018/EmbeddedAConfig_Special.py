import ROOT

from Configurations.Weights.EmbeddedReweightingModule.EmbeddedWeight import embeddedWeight_2018 as embeddedWeight

from Configurations.ConfigDefinition import ReweightConfiguration

DYConfiguration = ReweightConfiguration()
DYConfiguration.name = 'EmbeddedA'
DYConfiguration.inputFile = "/data/aloeliger/SMHTT_Selected_2018_Deep/EmbeddedA.root"
DYConfiguration.listOfWeights = [
    embeddedWeight
    ]
