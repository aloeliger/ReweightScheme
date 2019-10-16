import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight
from TauAnalysisTools.TauTriggerSFs.getTauTriggerSFs import getTauTriggerSFs
from Configurations.Weights import localWeightDataPath
import TriggerFunctions2016
import TriggerFunctions2017
import TriggerFunctions2018

triggerWeight_2016 = Weight()
triggerWeight_2016.name = 'TriggerSF'
triggerWeight_2016.TriggerSFFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2016.root")
triggerWeight_2016.tauSFs = getTauTriggerSFs('mutau',2016,'medium','MVAv2')
triggerWeight_2016.CalculateWeight = TriggerFunctions2016.CalculateTriggerWeight2016
triggerWeight_2016.hasUpDownUncertainties = True
triggerWeight_2016.uncertaintyVariationList = [
    "Trigger22_UP",
    "Trigger22_DOWN",
    "Trigger1920_UP",
    "Trigger1920_DOWN"]
triggerWeight_2016.InitUncertaintyVariations()
triggerWeight_2016.uncertaintyVariationFunctions = {
    "Trigger22_UP": TriggerFunctions2016.CalculateTriggerWeight2016_Trigger22_UP,
    "Trigger22_DOWN": TriggerFunctions2016.CalculateTriggerWeight2016_Trigger22_DOWN,
    "Trigger1920_UP": TriggerFunctions2016.CalculateTriggerWeight2016_Trigger1920_UP,
    "Trigger1920_DOWN": TriggerFunctions2016.CalculateTriggerWeight2016_Trigger1920_DOWN,    
    }

triggerWeight_2017 =  Weight()
triggerWeight_2017.name = 'TriggerSF'
triggerWeight_2017.TriggerSFFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2017.root")
triggerWeight_2017.tauSFs = getTauTriggerSFs('mutau',2017,'medium','MVAv2')
triggerWeight_2017.CalculateWeight = TriggerFunctions2017.CalculateTriggerWeight2017
triggerWeight_2017.hasUpDownUncertainties = True
triggerWeight_2017.uncertaintyVariationList = [
    "Trigger24or27_UP",
    "Trigger24or27_DOWN",    
    "Trigger2027_UP",
    "Trigger2027_DOWN"
]
triggerWeight_2017.InitUncertaintyVariations()
triggerWeight_2017.uncertaintyVariationFunctions = {
    "Trigger24or27_UP": TriggerFunctions2017.CalculateTriggerWeight2017_Trigger24or27_UP,
    "Trigger24or27_DOWN": TriggerFunctions2017.CalculateTriggerWeight2017_Trigger24or27_DOWN,    
    "Trigger2027_UP": TriggerFunctions2017.CalculateTriggerWeight2017_Trigger2027_UP,
    "Trigger2027_DOWN": TriggerFunctions2017.CalculateTriggerWeight2017_Trigger2027_DOWN,    
}

triggerWeight_2018 = Weight()
triggerWeight_2018.name = 'TriggerSF'
triggerWeight_2018.TriggerSFFile = ROOT.TFile.Open(localWeightDataPath+"htt_scalefactors_legacy_2018.root")
triggerWeight_2018.tauSFs = getTauTriggerSFs('mutau',2018,'medium','MVAv2')
triggerWeight_2018.CalculateWeight = TriggerFunctions2018.CalculateTriggerWeight2018
triggerWeight_2017.hasUpDownUncertainties = True
triggerWeight_2018.uncertaintyVariationList = [
    "Trigger24or27_UP",
    "Trigger24or27_DOWN",    
    "Trigger2027_UP",
    "Trigger2027_DOWN"    
]
triggerWeight_2018.InitUncertaintyVariations()
triggerWeight_2018.uncertaintyVariationFunctions = {
    "Trigger24or27_UP": TriggerFunctions2018.CalculateTriggerWeight2018_Trigger24or27_UP,
    "Trigger24or27_DOWN": TriggerFunctions2018.CalculateTriggerWeight2018_Trigger24or27_DOWN,
    "Trigger2027_UP": TriggerFunctions2018.CalculateTriggerWeight2018_Trigger2027_UP,
    "Trigger2027_DOWN": TriggerFunctions2018.CalculateTriggerWeight2018_Trigger2027_DOWN,
    }
