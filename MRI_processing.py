from __future__ import unicode_literals, print_function
from builtins import str



#Checking brainsuite executable path
from distutils.spawn import find_executable
if(find_executable('svreg.sh')):
    print('svreg: true')
print('Message to user:')
if(find_executable('bse') and find_executable('svreg.sh') and find_executable('bdp.sh')):
    print('Your system path has been set up correctly. Continue on with the tutorial.')
else:
    print('Your system path has not been set up correctly.')
    print('Please add the above paths to your system path variable and restart the kernel for this tutorial.')
    print('Edit your ~/.bashrc file, and add the following line, replacing your_path with the path to BrainSuite16a1:\n')
    print('export PATH=$PATH:/your_path/BrainSuite16a1/svreg/bin:/your_path/BrainSuite16a1/bdp:/your_path/BrainSuite16a1/bin')
    exit(1)

#Path set properly if reached here
from nipype import config #Set configuration before importing nipype pipeline
cfg = dict(execution={'remove_unnecessary_outputs' : False}) #We do not want nipype to remove unnecessary outputs
config.update_config(cfg)

import nipype.pipeline.engine as pe
import nipype.interfaces.brainsuite as bs
import nipype.interfaces.io as io
import os
from distutils.spawn import find_executable
import fnmatch
from glob import glob1

brainsuite_atlas_directory = find_executable('bse')[:-3] + '../atlas/'

def main(input_path):
    brainsuite_workflow = pe.Workflow(name='brainsuite_workflow_cse')
    brainsuite_workflow.base_dir='./'


    bseObj = pe.Node(interface=bs.Bse(), name='BSE')
    bseObj.inputs.inputMRIFile = input_path
    bfcObj = pe.Node(interface=bs.Bfc(),name='BFC')
    pvcObj = pe.Node(interface=bs.Pvc(), name = 'PVC')
    cerebroObj = pe.Node(interface=bs.Cerebro(), name='CEREBRO')
    #Provided atlas files
    cerebroObj.inputs.inputAtlasMRIFile =(brainsuite_atlas_directory + 'brainsuite.icbm452.lpi.v08a.img')
    cerebroObj.inputs.inputAtlasLabelFile = (brainsuite_atlas_directory + 'brainsuite.icbm452.v15a.label.img')
    cortexObj = pe.Node(interface=bs.Cortex(), name='CORTEX')
    scrubmaskObj = pe.Node(interface=bs.Scrubmask(), name='SCRUBMASK')
    tcaObj = pe.Node(interface=bs.Tca(), name='TCA')
    dewispObj=pe.Node(interface=bs.Dewisp(), name='DEWISP')
    dfsObj=pe.Node(interface=bs.Dfs(),name='DFS')
    pialmeshObj=pe.Node(interface=bs.Pialmesh(),name='PIALMESH')

    brainsuite_workflow.add_nodes([bseObj, bfcObj, pvcObj, cerebroObj, cortexObj, scrubmaskObj, tcaObj, dewispObj, dfsObj, pialmeshObj])

    brainsuite_workflow.connect(bseObj, 'outputMRIVolume', bfcObj, 'inputMRIFile')
    brainsuite_workflow.connect(bfcObj, 'outputMRIVolume', pvcObj, 'inputMRIFile')
    brainsuite_workflow.connect(bfcObj, 'outputMRIVolume', cerebroObj, 'inputMRIFile')
    brainsuite_workflow.connect(cerebroObj, 'outputLabelVolumeFile', cortexObj, 'inputHemisphereLabelFile')
    brainsuite_workflow.connect(pvcObj, 'outputTissueFractionFile', cortexObj, 'inputTissueFractionFile')
    brainsuite_workflow.connect(cortexObj, 'outputCerebrumMask', scrubmaskObj, 'inputMaskFile')
    brainsuite_workflow.connect(cortexObj, 'outputCerebrumMask', tcaObj, 'inputMaskFile')
    brainsuite_workflow.connect(tcaObj, 'outputMaskFile', dewispObj, 'inputMaskFile')
    brainsuite_workflow.connect(dewispObj, 'outputMaskFile', dfsObj, 'inputVolumeFile')
    brainsuite_workflow.connect(dfsObj, 'outputSurfaceFile', pialmeshObj, 'inputSurfaceFile')
    brainsuite_workflow.connect(pvcObj, 'outputTissueFractionFile', pialmeshObj, 'inputTissueFractionFile')
    brainsuite_workflow.connect(cerebroObj, 'outputCerebrumMaskFile', pialmeshObj, 'inputMaskFile')
    #brainsuite_workflow.connect(dfsObj, 'outputSurfaceFile', hemisplitObj, 'inputSurfaceFile')
    #brainsuite_workflow.connect(cerebroObj, 'outputLabelVolumeFile', hemisplitObj, 'inputHemisphereLabelFile')
    #brainsuite_workflow.connect(pialmeshObj, 'outputSurfaceFile', hemisplitObj, 'pialSurfaceFile')

    brainsuite_workflow.run()


from tqdm import tqdm

age_path ='ADNI'

roots = []
ch_dirs = []
n = 0
for root, dirs, files in os.walk(age_path):
    fileCounter = len(glob1(root,"*.nii.gz"))
    if fileCounter == 1 and 'brainsuite_workflow_cse' not in root and 'brainsuite_workflow_cse' not in dirs:
        ch_dirs += [root]
        roots += [os.path.join(root,glob1(root,"*.nii.gz")[0])]
print(len(roots))

oldpwd = os.getcwd()

for i in tqdm(range(len(roots))):   
    try: 
        path = os.path.join('~/Research', roots[i])
        os.chdir(ch_dirs[i])
        main(path)
    except:
        pass 
    os.chdir(oldpwd)
