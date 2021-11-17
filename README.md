# twoFilesSolution

This package is mean to be run Validation using two file solution

* setup: (it has been tested on CMSSW_11_2_4, should run in any of the recent CMSSW releases)

```
scram p -n CMSSW_1124_Validation CMSSW_11_2_4
cd CMSSW_1124_Validation/src
cmsenv
git cms-addpkg Validation/RecoTrack/

cd Validation/RecoTrack/python/
wget https://raw.githubusercontent.com/slezki/twoFilesSolution/master/inputFiles.py

cd ../
scram b -j8

cd Validation/RecoTrack/test/
mkdir twoFileConfig
cd twoFileConfig/
wget https://raw.githubusercontent.com/slezki/twoFilesSolution/master/step3_VALIDATION_DQM.py
```

* Run:

```
voms-proxy-init -rfc -voms cms -valid 192:00
cmsRun step3_VALIDATION_DQM.py
```

* Example cmsDriver command:

```
cmsDriver.py step3 --conditions auto:phase2_realistic_T15 -s VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier DQMIO -n 10 --geometry Extended2026D49 --era Phase2C9 --eventcontent DQM --filein file:step2.root --fileout file:step3.root --no_exec --mc 2>&1
```