# ReweightScheme
My general purpose root ntuple weight branch creation code

## FinalReweight.py
This is the final script called to create weights on on a tree. At the moment it is hard coded to look for a tree called
'mt_Selected'.

This script will create a final weight with all the weights defined on your sample multiplied together, final weights
with individual up/down uncertainties defined on your weights applied, as well as individual weight branches to examine
the shapes of individual weights, and their up/down uncertainties.

### Options
- `--ConfigFiles`: Required, takes any number of arugments, which are just the paths to configuration files to run the tool
- `--RemovalRecipe`: provides a quick recipe for the removal of the branches added by a particular configuration, designed
  to be run on my `PruneBranches.py` script included elsewhere in the SMHTT code (to be ported here soon?)

## Configurations

### ConfigDefinition.py
Where the final ReweightScheme configuration class is defined.

### UserConfigs
Convenient spot for writing your own weighting scheme configurations

### Weights
Where all the weights that can be added to samples are defined.

#### Data
Contains root files with scale factors and other necessary things in them.

#### How do I write a weight to be used in my weighting scheme?
- Open a python file, at the top import the weight definition `from Configurations.Weights.WeightDefinition import Weight as Weight` 
  (and if you need a file in Data, the local data path, `from Configurations.Weights import localWeightDataPath`)
- Define a function that takes two arguments, the Weight itself (`self`) and the tree with the current event loaded (can
  be called whatever, but I find it convenient to label it `theTree`). The end result of this function must be to set 
  `self.value[0]` to the proper value for the weight.
- If this weight has up/down uncertainties, you will need to define additional functions. These functions behave 
  similarly to the nominal but take an additional argument (that I call `uncert`). This is a little bit clunky, but 
  at the end of the day, what this function must do is similar to the abov but instead it will fill `self.uncertaintyVariationArrays[uncert][0]`
- Now to make the weight you declare an instance of the weight class: `MyWeight = Weight()`
- Set it's name with `Weight.name = 'MyWeight'` (This is how it will show up in the tree)
- Oftentimes, if you have something you would like to for the object to use in the function, a scale factor tool or the like
  it is useful to declare it as an instance variable here as well. Strictly optional.
- You need to set the configuration's CalculateWeight variable to your function like so: `MyWeight.CalculateWeight = MyFunction` (no parantheses)
- (optional) if your weight comes with up/down uncertainties, set the `MyWeight.hasUpDownUncertainties` variable to `True`
- (optional) if your weight comes with up/down uncertainties, set the various names of all the related weights in
  the `uncertaintyVariationList` list with `MyWeight.uncertaintyVariationList = ["Weight_error1_UP","Weight_error1_DOWN","Weight_error2_UP",...]`
  (the "UP","DOWN" is not strictly necessary, but recommended for clarity).
- (optional) if your weight comes with up/down uncertainties, a little extra set-up of the histograms is necessary, so now call:
  `MyWeight.InitUncertaintyVariations()`
- (optional) finally, if your weight comes with up/down uncertainties, create a dictionary (`MyWeight.uncertaintyVariationFunctions`) with all the names you provided before as keys, and with
  the functions to calculate the weight up/down as the values like so: `MyWeight.uncertaintyVariationFunctions = {"MyWeight_error1_UP":myFunction_Error1_up,...}`

#### How do I write a configuration to properly weight my final product?
- Open a python file. You will need to import the configuration definition: `Configurations.ConfigDefinition import ReweightConfiguration`
- Also, import all of the instances of weights that you will need to be applied to your final product.
- Create an instance of the reweight configuration: `MyConfiguration = ReweightConfiguration()`
- Set it's name (No defined behavior, but could be used by behavior you write) `MyConfiguration.name = theName`
- Set the path to the input file to get reweighted: `MyConfiguration.inputFile = "/path/to/file.root"`
- (optional) some weights (like ones I  have created for corss section and pileup) will need years and sample names
   given to them at the time of configuration. This is a good spot to do that. See some of my written configurations for 
   examples of what I mean
- The only other required thing is that all defined weights are put in the configuration's `listOfWeights` list like so:
  `MyConfiguration.listOfWeights = [MyWeight, MyOtherWeight,MyThidWeight,...]`


## Utilities

### RecursiveLoader.py
Contains a simple object used to load python modules from absolute directory paths.

## How do I run this and get a weighted ntuple?

Typically, once you have configurations defined, running should be as simple as:
`python FinalReweight.py --ConfigFiles <Path to configuration files. Supports wildcards.>`

I would love to see use of this tool expand beyond just me, so if you have ideas or improvements, please let me know or open a PR.

