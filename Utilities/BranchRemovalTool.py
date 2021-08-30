import ROOT
import sys
import argparse
import os

def PruneBranches(theFileName,branchesToPrune):
    pruneFile = ROOT.TFile(theFileName,"UPDATE")
    #theTree = pruneFile.mt_Selected

    alreadyGrabbedItems = []
    for keyObj in pruneFile.GetListOfKeys():
        if keyObj.GetName() not in alreadyGrabbedItems:
            obj = pruneFile.Get(keyObj.GetName())
            if type(obj) == type(ROOT.TTree()):
                for branch in branchesToPrune:
                    try:
                        obj.GetBranch(branch).SetStatus(0)
                    except:
                        print("Didn't find the branch: "+branch+" in: "+obj.GetName())
                obj = obj.CloneTree(-1,"fast")
            obj.Write()
            alreadyGrabbedItems.append(keyObj.GetName())
