import ROOT
from Configurations.Weights.WeightDefinition import Weight as Weight

#we need to find a way to specify what cross section or what year we want this module to calculate weights 
#for.
#I'm going to go ahead and just assume that the sample has been given to this particular weight as a variable 
#Sample will be 'sample' and the year as 'year', and the total number of events processed will be 'totalEvents'

def CalculateCrossSectionWeight(self,theTree):
    crossSectionWeight = 1.0
    if self.year == "2016":
        LHCLumi = 35.92e15
    elif self.year == "2017":
        LHCLumi = 41.557e15
    elif self.year == "2018":
        LHCLumi = 59.74e15

    if self.year == '2016':
        crossSections = {
            "DY" : 6077.22e-12,
            "TTTo2L2Nu": 88.29e-12,
            "TTToSemiLeptonic": 365.35e-12,
            "TTToHadronic": 377.96e-12,
            "W": 61526.7e-12,
            "ST_tW_antitop": 35.85e-12,
            "ST_tW_top":35.85e-12,
            "ST_t_antitop":26.23e-12,
            "ST_t_top":44.07e-12,
            "ggH": 48.30e-12*0.06208,
            "VBF": 3.770e-12*0.06208,
            "WHPlus": 0.8331e-12 * 0.06208,
            "WHMinus": 0.5272e-12 * 0.06208,
            "ZH": 0.7544e-12*0.06208,
            "GGZHLLTT":0.1223e-12*0.06208*3*0.033658,
            "GGZHNNTT":0.1223e-12*0.06208*0.2000,
            "GGZHQQTT":0.1223e-12*0.06208*0.6991,
            "ZZ": 16.523e-12,
            "WZ":47.13e-12,
            "WW":118.7e-12,
            "EWKZLL": 4.321e-12 * 0.06208,
            "EWKZNuNu":10.66e-12 * 0.06208,
            "TT":831.76e-12,        
            "WZ1L1Nu2Q": 10.71e-12,
            "WZ1L3Nu":3.05e-12,
            "WZ3L1Nu":4.708e-12,
            "WZ2L2Q": 5.595e-12,
            "WW1L1Nu2Q":49.997e-12,
            "WZJLLLNu":4.708e-12,
            "ZZ4L":1.212e-12,
            "ZZ2L2Q":3.22e-12,
            "VV2L2Nu":11.95e-12,
            "GGHWW":48.30e-12 * 0.2203 * 0.3258 * 0.3258,
            "VBFHWW":3.770e-12 * 0.2203 * 0.3258 * 0.3258,
            "WplusHWW":0.8331e-12 * 0.2203,
            "WminusHWW":0.5272e-12 * 0.2203,
            "ZHWW":0.7544e-12 * 0.2203,
            "GGZHWW": 0.1223e-12 * 0.2203,
            "ttHtoTauTau":0.5033e-12*0.06208,
            "ttHtoNonbb":0.5033e-12*(1.0-0.5760),
        }
    else:
        crossSections = {
            "DY" : 6077.22e-12,
            "TTTo2L2Nu": 88.29e-12,
            "TTToSemiLeptonic": 365.35e-12,
            "TTToHadronic": 377.96e-12,
            "W": 61526.7e-12,
            "ST_tW_antitop": 35.85e-12,
            "ST_tW_top":35.85e-12,
            "ST_t_antitop":26.23e-12,
            "ST_t_top":44.07e-12,
            "ggH": 48.30e-12*0.06208,
            "VBF": 3.770e-12*0.06208,
            "WHPlus": 0.8331e-12 * 0.06208,
            "WHMinus": 0.5272e-12 * 0.06208,
            "ZH": 0.7544e-12*0.06208,
            "GGZHLLTT":0.1223e-12*0.06208*3*0.033658,
            "GGZHNNTT":0.1223e-12*0.06208*0.2000,
            "GGZHQQTT":0.1223e-12*0.06208*0.6991,
            "ZZ": 16.523e-12,
            "WZ":47.13e-12,
            "WW":118.7e-12,
            "EWKZLL": 4.321e-12 * 0.06208,
            "EWKZNuNu":10.66e-12 * 0.06208,
            "TT":831.76e-12,        
            "WZ1L1Nu2Q": 10.71e-12,
            "WZ1L3Nu":3.05e-12,
            "WZ3L1Nu":4.43e-12,
            "WZ2L2Q": 5.525e-12,
            "WW1L1Nu2Q":49.997e-12,
            "WZJLLLNu":5.26e-12,
            "ZZ4L":1.26e-12,
            "ZZ2L2Q":3.38e-12,
            "VV2L2Nu":13.84e-12,
            "GGHWW":48.30e-12 * 0.2203 * 0.3258 * 0.3258,
            "VBFHWW":3.770e-12 * 0.2203 * 0.3258 * 0.3258,
            "WplusHWW":0.8331e-12 * 0.2203,
            "WminusHWW":0.5272e-12 * 0.2203,
            "ZHWW":0.7544e-12 * 0.2203,
            "GGZHWW": 0.1223e-12 * 0.2203,
            "ttHtoTauTau":0.5033e-12*0.06208,
            "ttHtoNonbb":0.5033e-12*(1.0-0.5760),
        }
    crossSectionWeighting = crossSections[self.sample] * LHCLumi / self.totalEvents

    #multi sample weights
    if self.year == "2016":
        if self.sample == "DY":
            crossSectionWeighting = 1.49526
            if theTree.numGenJets == 1:
                crossSectionWeighting = 0.43169
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 0.4649
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 0.5373
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 0.7815
        if self.sample == "W":
            crossSectionWeighting = 25.427
            if theTree.numGenJets == 1:
                crossSectionWeighting = 6.832
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 2.0943
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 0.68722
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 0.76513
    if self.year == "2017":
        if self.sample == "DY":
            crossSectionWeighting = 2.582
            if theTree.numGenJets == 1:
                crossSectionWeighting = 0.7105
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 0.92206
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 1.6526
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 0.21987
        if self.sample == "W":
            crossSectionWeighting = 23.722
            if theTree.numGenJets == 1:
                crossSectionWeighting = 3.113
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 3.020
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 2.205
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 2.1513
    if self.year == "2018":
        if self.sample == "DY":
            crossSectionWeighting = 3.6299
            if theTree.numGenJets == 1:
                crossSectionWeighting = 0.6304
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 0.5521
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 0.6008
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 0.8315
        if self.sample == "W":
            crossSectionWeighting = 51.7495
            if theTree.numGenJets == 1:
                crossSectionWeighting = 9.0816
            elif theTree.numGenJets == 2:
                crossSectionWeighting = 4.5107
            elif theTree.numGenJets == 3:
                crossSectionWeighting = 3.0774
            elif theTree.numGenJets == 4:
                crossSectionWeighting = 3.2112
    crossSectionWeighting = crossSectionWeighting * theTree.genweight
    self.value[0] = crossSectionWeighting
        
crossSectionWeight = Weight()
crossSectionWeight.name = 'CrossSectionWeighting'
crossSectionWeight.CalculateWeight = CalculateCrossSectionWeight
