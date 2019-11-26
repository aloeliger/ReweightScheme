import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from Configurations.Weights import localWeightDataPath
from EmbeddedTriggerFunctions import *

#2016
embeddedTriggerWeight_2016 = Weight()
embeddedTriggerWeight_2016.name = 'EmbeddedTriggerWeighting'
embeddedTriggerWeight_2016.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"LegacyCorrectionsWorkspace/output/htt_scalefactors_legacy_2016.root")
embeddedTriggerWeight_2016.CalculateWeight = CalculateEmbeddedTriggerWeight2016
embeddedTriggerWeight_2016.hasUpDownUncertainties = True
embeddedTriggerWeight_2016.uncertaintyVariationList = [
    "Trigger22_UP",
    "Trigger22_DOWN",
    "Trigger1920_UP",
    "Trigger1920_DOWN"]
embeddedTriggerWeight_2016.InitUncertaintyVariations()
embeddedTriggerWeight_2016.uncertaintyVariationFunctions = {
    "Trigger22_UP":CalculateEmbeddedTriggerWeight2016_22UP,
    "Trigger22_DOWN":CalculateEmbeddedTriggerWeight2016_22DOWN,
    "Trigger1920_UP":CalculateEmbeddedTriggerWeight2016_1920UP,
    "Trigger1920_DOWN":CalculateEmbeddedTriggerWeight2016_1920DOWN,
    }

#2017
embeddedTriggerWeight_2017 = Weight()
embeddedTriggerWeight_2017.name = 'EmbeddedTriggerWeighting'
embeddedTriggerWeight_2017.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"LegacyCorrectionsWorkspace/output/htt_scalefactors_legacy_2017.root")
embeddedTriggerWeight_2017.CalculateWeight = CalculateEmbeddedTriggerWeight1718
embeddedTriggerWeight_2017.hasUpDownUncertainties = True
embeddedTriggerWeight_2017.uncertaintyVariationList = [
    "Trigger24or27_UP",
    "Trigger24or27_DOWN",    
    "Trigger2027_UP",
    "Trigger2027_DOWN"]
embeddedTriggerWeight_2017.InitUncertaintyVariations()
embeddedTriggerWeight_2017.uncertaintyVariationFunctions = {
    "Trigger24or27_UP":CalculateEmbeddedTriggerWeight1718_24or27UP,
    "Trigger24or27_DOWN":CalculateEmbeddedTriggerWeight1718_24or27DOWN,  
    "Trigger2027_UP":CalculateEmbeddedTriggerWeight1718_2027UP,
    "Trigger2027_DOWN":CalculateEmbeddedTriggerWeight1718_2027DOWN,
    }

#2018
embeddedTriggerWeight_2018 = Weight()
embeddedTriggerWeight_2018.name = 'EmbeddedTriggerWeighting'
embeddedTriggerWeight_2018.embeddedWorkspace = ROOT.TFile.Open(localWeightDataPath+"LegacyCorrectionsWorkspace/output/htt_scalefactors_legacy_2018.root")
embeddedTriggerWeight_2018.CalculateWeight = CalculateEmbeddedTriggerWeight1718
embeddedTriggerWeight_2018.hasUpDownUncertainties = True
embeddedTriggerWeight_2018.uncertaintyVariationList = [
    "Trigger24or27_UP",
    "Trigger24or27_DOWN",    
    "Trigger2027_UP",
    "Trigger2027_DOWN"]
embeddedTriggerWeight_2018.InitUncertaintyVariations()
embeddedTriggerWeight_2018.uncertaintyVariationFunctions = {
    "Trigger24or27_UP":CalculateEmbeddedTriggerWeight1718_24or27UP,
    "Trigger24or27_DOWN":CalculateEmbeddedTriggerWeight1718_24or27DOWN,  
    "Trigger2027_UP":CalculateEmbeddedTriggerWeight1718_2027UP,
    "Trigger2027_DOWN":CalculateEmbeddedTriggerWeight1718_2027DOWN,
    }
