## MRI-SSB: Automatic segmentation and evulation of skull/scalp/brain from batch T1 MRI datasets
This is the official implementation of the MRI analysis part of the paper:

### [#TO-DO: paper title and link](https://stars.chromeexperiments.com)

[Junhao Zhang](https://junha0zhang.github.io/), [Ruiqing Ni](https://biomed.ee.ethz.ch/institute/People/person-detail.html?persid=225279)

### Contact
If you have any questions, please let us know:
- Junhao Zhang {zhangjunhao957@gmail.com}
- Ruiqing Ni {ni@biomed.ee.ethz.ch}

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
The ADNI dataset consists of around 1000 T1-weighted MRI images of male and female subjects from 51-100 years old, taken in the [Univerisity Hospital Zurich](https://www.usz.ch). For details about the dataset, please ask [Ruiqing Ni](https://biomed.ee.ethz.ch/institute/People/person-detail.html?persid=225279). It is organized as follows:
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

![Example](demo.png?raw=true)

## Citations
If you find this code useful for your project, please consider citing:
```
TO-DO: citation
```

## Acknowledgments
In this project we use (parts of) the following open-source works:
- [BrainSuite](http://brainsuite.org/)
- [Open3D](http://www.open3d.org/)

 We thank the respective authors for their methods. We would also like to thank reviewers for their valuable inputs. 
