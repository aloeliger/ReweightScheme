import ROOT 

class DESYScaleFactor():
    def __init__(self,theFileName):
        self.scaleFactorFile = ROOT.TFile.Open(theFileName)

        self.etaLt0p9Histo_MC = self.scaleFactorFile.ZMassEtaLt0p9_MC
        self.eta0p9to1p2Histo_MC = self.scaleFactorFile.ZMassEta0p9to1p2_MC
        self.eta1p2to2p1Histo_MC = self.scaleFactorFile.ZMassEta1p2to2p1_MC
        self.etaGt2p1Histo_MC = self.scaleFactorFile.ZMassEtaGt2p1_MC

        self.etaLt0p9Histo_Data = self.scaleFactorFile.ZMassEtaLt0p9_Data
        self.eta0p9to1p2Histo_Data = self.scaleFactorFile.ZMassEta0p9to1p2_Data
        self.eta1p2to2p1Histo_Data = self.scaleFactorFile.ZMassEta1p2to2p1_Data
        self.etaGt2p1Histo_Data = self.scaleFactorFile.ZMassEtaGt2p1_Data

    def GetScaleFactorWithHistos(self,xAxisVar,dataHisto,MCHisto):
        dataEntry = dataHisto.Eval(xAxisVar)
        MCEntry = MCHisto.Eval(xAxisVar)
        return dataEntry/MCEntry

    def GetScaleFactor(self,xAxisVar,eta):
        if abs(eta)< 0.9:
            return self.GetScaleFactorWithHistos(xAxisVar,self.etaLt0p9Histo_Data,self.etaLt0p9Histo_MC)
        elif abs(eta) >= 0.9 and abs(eta) < 1.2:
            return self.GetScaleFactorWithHistos(xAxisVar,self.eta0p9to1p2Histo_Data,self.eta0p9to1p2Histo_MC)
        elif abs(eta) >= 1.2 and abs(eta) < 2.1:
            return self.GetScaleFactorWithHistos(xAxisVar,self.eta1p2to2p1Histo_Data,self.eta1p2to2p1Histo_MC)
        else:
            return self.GetScaleFactorWithHistos(xAxisVar,self.etaGt2p1Histo_Data,self.etaGt2p1Histo_MC)
