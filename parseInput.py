from PyFoam.RunDictionary.ParsedParameterFile import ParsedParameterFile

f=ParsedParameterFile('files/faSolution')
print(f['relaxationFactors'])
# for name, value in f['nOuterCorrectors'].iteritems():
#   print(name)
#   print(value)
  