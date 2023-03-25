## BrainCalculator: Automatic segmentation and evulation of skull thickness/scalp-to-cortex distance from large T1 MRI datasets
This is the official implementation of the MRI analysis part of the paper:

### [#TO-DO: paper title and link](https://stars.chromeexperiments.com)

[Junhao Zhang](https://junha0zhang.github.io/), [Ruiqing Ni](https://biomed.ee.ethz.ch/institute/People/person-detail.html?persid=225279)

### Contact
If you have any questions, please let us know:
- Junhao Zhang {zhangjunhao957@gmail.com}
- Ruiqing Ni {ni@biomed.ee.ethz.ch}

Copyright (c) 2022-2023 Junhao Zhang et al.

## Instructions
This repository consists of two parts: segmentation of MRI regions and measurements of thicknesses/distances.

### Installing BrainSuite's Nipype interface
This code has been tested on
- Mac Monterey (Windows is not supported unfortunately, for Windows users please use a 64-bit Linux VM like [Oracle VM VirtualBox](https://www.virtualbox.org/))
- Python 3.9
- BrainSuite v.21a

Steps:
1. Download and install [BrainSuite](http://brainsuite.org/).
2. Add BrainSuite's bin directory to your system's path. The default shell of MAC is ZSH, so in the .zshrc file (which is hidden by default) add the following lines in the end: 
    ```
    export PATH=/The/path/to/your/brainsuite/bin:$PATH
    export PATH=/The/path/to/your/brainsuite/svreg/bin:/The/path/to/your/brainsuite/bdp:/The/path/to/your/brainsuite/bin:$PATH
    ```
    Also make sure python is added to your system's path as well.
3. To ensure that this step is completed, open a terminal window and run the command ```bse```. If instruction text shows up, this step has been completed.
4. Next, install Nipype with the following command if your Python was installed with anaconda
    ```
    cd ~/anaconda*/lib/python*/site-packages/
    git clone https://github.com/nipy/nipype.git
    cd nipype
    pip install -r requirements.txt
    python setup.py develop
    ```
    where ```*``` is the version of your anaconda/python. To test it, run ```from nipype.interfaces import brainsuite``` in python. Refer to the [installation guide](http://brainsuite.org/nipype_installation/) for more tutorials.
    
### Batch processing of MRI
Around 400 T1-weighted MRI images of male and female non-demented control subjects from 51-100 years old from the ADNI dataset was used (https://adni.loni.usc.edu/). Data used in preparation of this article were obtained from the Alzheimer's Disease Neuroimaging Initiative (ADNI) database (adni.loni.usc.edu). As such, the investigators within the ADNI contributed to the design and implementation of ADNI and/or provided data but did not participate in analysis or writing of this report. A complete listing of ADNI investigators can be found at: http://adni.loni.usc.edu/wp-content/uploads/how_to_apply/ADNI_Acknowledgement_List.pdf. For details about the dataset, please contact [Ruiqing Ni](https://biomed.ee.ethz.ch/institute/People/person-detail.html?persid=225279). It is organized as follows:
- `ADNI`
    - `***_S_****`
        - `MPRAGE`
            - `date`   
                - `I******`
                    - `***.nii.gz`  
        - `MPRAGE_SENSE2`
            - `date` 
                - `I******` 
                    - `***.nii.gz`
        - `Sagittal_3D_Accelerated_MPRAGE`
            - `date`  
                - `I******`  
                    - `***.nii.gz`
    - ...

Simply run `python MRI_processing.py` to process all the images. It takes about 60 hours to finish this dataset. After, convert all the .wfo files to .obj (3D mesh) and then it's ready for calculation.

**Note**: The code was designed to only sort dataset in this format. Please modify the code if using another dataset with Python depedencies like `os` and `glob`. If the code runs successfully, you'll find a `brainsuite_workflow_cse` folder next to each `***.nii.gz` file. It includes all the outputs from the computation.

### Distance/Volume calculation
I put the code in a jupyter notebook `calculation.ipynb` with explanations. Please look into it for more details. The required libraries are Open3D 0.16.0, pyvista 0.37.0, fnmatch, etc. Pip install other libraries also if needed. However, for Apple silicon platforms, there is some issue with visualization in Open3D up to September 2022, but it's fine on Windows.


## Citations
If you find this code useful for your project, please cite: Automatic analysis of skull thickness, scalp-to-cortex distance and association with age and sex in cognitively normal elderly
Junhao Zhang, Valerie Treyer, Junfeng Sun, Chencheng Zhang, Anton Gietl, Christoph Hock, Daniel Razansky,Roger M. Nitsch, Ruiqing Ni; for ADNI.
Brain Stimulation: Basic, Translational, and Clinical Research in Neuromodulation, DOI:https://doi.org/10.1016/j.brs.2023.03.011


## Acknowledgments
In this project we use (parts of) the following open-source works:
- [BrainSuite](http://brainsuite.org/)
- [Open3D](http://www.open3d.org/)

- Data: Alzheimer's Disease Neuroimaging Initiative (ADNI) database (adni.loni.usc.edu)

