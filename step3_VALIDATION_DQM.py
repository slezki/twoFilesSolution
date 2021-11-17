# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic_T15 -s VALIDATION:@trackingOnlyValidation,DQM:@trackingOnlyDQM --datatier DQMIO -n 10 --geometry Extended2026D49 --era Phase2C9 --eventcontent DQM --filein file:step2.root --fileout file:step3.root --no_exec --mc
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('DQM',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Validation.RecoTrack.inputFiles import pu50_reco
from Validation.RecoTrack.inputFiles import pu50
#from Validation.RecoTrack.inputFiles import pu150
#from Validation.RecoTrack.inputFiles import pu200

process.MessageLogger.categories.append('FastReport')
process.MessageLogger.cerr.FastReport = cms.untracked.PSet( limit = cms.untracked.int32( 10000000 ) )

process.ThroughputService = cms.Service('ThroughputService',
    eventRange = cms.untracked.uint32(1000),
    eventResolution = cms.untracked.uint32(10),
    printEventSummary = cms.untracked.bool(True),
    enableDQM = cms.untracked.bool(True),
    dqmPathByProcesses = cms.untracked.bool(False),
    dqmPath = cms.untracked.string('Throughput'),
    timeRange = cms.untracked.double(1000),
    timeResolution = cms.untracked.double(1)
)

process.MessageLogger.categories.append('ThroughputService')
process.MessageLogger.cerr.ThroughputService = cms.untracked.PSet(
    limit = cms.untracked.int32(10000000)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(pu50_reco),
    secondaryFileNames = cms.untracked.vstring(pu50)
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(16),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3_inDQM_pu50.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

#from HLTrigger.Configuration.common import *
# Path and EndPath definitions
#for analyzer in analyzers_by_type(process, "new"):
    #print(analyzer._Labelable__label)
    #process.DQMOfflineTracking.remove(analyzer)

process.trackValidatorsTrackingOnly.remove(process.trackValidatorBuilding)
process.trackValidatorsTrackingOnly.remove(process.trackValidatorBuildingPreSplitting)
process.trackValidatorsTrackingOnly.remove(process.trackValidatorSeedingTrackingOnly)
process.trackValidatorsTrackingOnly.remove(process.trackValidatorSeedingPreSplittingTrackingOnly)
process.trackValidatorsTrackingOnly.remove(process.trackValidatorConversionTrackingOnly)
process.trackValidatorsTrackingOnly.remove(process.trackValidatorBHadronTrackingOnly)
process.DQMOfflineTracking.remove(process.materialDumperAnalyzer)
process.DQMOfflineTracking.remove(process.TrackSeedMonmuonSeededStepOutIn)
process.DQMOfflineTracking.remove(process.TrackSeedMonmuonSeededStepInOut)
process.DQMOfflineTracking.remove(process.TrackSeedMonpixelPairStep)
process.DQMOfflineTracking.remove(process.TrackSeedMondetachedQuadStep)
process.DQMOfflineTracking.remove(process.TrackSeedMonlowPtTripletStep)
process.DQMOfflineTracking.remove(process.TrackSeedMonlowPtQuadStep)
process.DQMOfflineTracking.remove(process.TrackMon_ckf)
process.DQMOfflineTracking.remove(process.TrackSeedMonhighPtTripletStep)
process.DQMOfflineTracking.remove(process.TrackSeedMoninitialStep)

process.prevalidation_step = cms.Path(process.globalPrevalidationTrackingOnly)
process.validation_step = cms.EndPath(process.globalValidationTrackingOnly)
process.dqmoffline_step = cms.EndPath(process.DQMOfflineTracking)
#process.dqmofflineOnPAT_step = cms.EndPath(process.PostDQMOffline)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.DQMoutput_step)
process.schedule = cms.Schedule(process.prevalidation_step,process.validation_step,process.dqmoffline_step,process.DQMoutput_step)
#process.schedule = cms.Schedule(process.prevalidation_step,process.validation_step,process.DQMoutput_step)

# remove any instance of the FastTimerService
if 'FastTimerService' in process.__dict__:
    del process.FastTimerService

# instrument the menu with the FastTimerService
process.load( "HLTrigger.Timer.FastTimerService_cfi" )

process.FastTimerService = cms.Service( "FastTimerService",
    printEventSummary = cms.untracked.bool( False ),
    printRunSummary = cms.untracked.bool( False ),
    printJobSummary = cms.untracked.bool( True ),
    writeJSONSummary = cms.untracked.bool( True ),
    jsonFileName = cms.untracked.string( "twoFileS_pu50.json" ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( True ),
    enableDQMbyPath = cms.untracked.bool( True ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMTransitions = cms.untracked.bool( False ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmMemoryResolution = cms.untracked.double( 5000.0 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathMemoryRange = cms.untracked.double( 1000000.0 ),
    dqmPathMemoryResolution = cms.untracked.double( 5000.0 ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    dqmModuleMemoryRange = cms.untracked.double( 100000.0 ),
    dqmModuleMemoryResolution = cms.untracked.double( 500.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
)

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
