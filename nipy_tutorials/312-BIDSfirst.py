"""
First level analysis of a complete BIDS dataset from openneuro
===============================================================


Full step-by-step example of fitting a GLM to perform a first level analysis
in an openneuro BIDS dataset. We demonstrate how BIDS derivatives can be
exploited to perform a simple one subject analysis with minimal code.
Details about the BIDS standard are available at http://bids.neuroimaging.io/
We also demonstrate how to download individual groups of files from the
Openneuro s3 bucket.

More specifically:

1. Download an fMRI BIDS dataset with derivatives from openneuro
2. Extract automatically from the BIDS dataset first level model objects
3. Demonstrate Quality assurance of Nistat estimation against available FSL
   estimation in the openneuro dataset
4. Display contrast plot and uncorrected first level statistics table report



To run this example, you must launch IPython via ``ipython
--matplotlib`` in a terminal, or use the Jupyter notebook.

.. contents:: **Contents**
    :local:
    :depth: 1
"""
##############################################################################
# Fetch openneuro BIDS dataset
# -----------------------------
# We download one subject from the stopsignal task in the ds000030 V4 BIDS
# dataset available in openneuro.
# This dataset contains the necessary information to run a statistical analysis
# using Nistats. The dataset also contains statistical results from a previous
# FSL analysis that we can employ for comparison with the Nistats estimation.
from nistats.datasets import (fetch_openneuro_dataset_index,
                              fetch_openneuro_dataset, select_from_index)

_, urls = fetch_openneuro_dataset_index()

exclusion_patterns = ['*group*', '*phenotype*', '*mriqc*',
                      '*parameter_plots*', '*physio_plots*',
                      '*space-fsaverage*', '*space-T1w*',
                      '*dwi*', '*beh*', '*task-bart*',
                      '*task-rest*', '*task-scap*', '*task-task*']
urls = select_from_index(
    urls, exclusion_filters=exclusion_patterns, n_subjects=1)

data_dir, _ = fetch_openneuro_dataset(urls=urls)

##############################################################################
# Obtain automatically FirstLevelModel objects and fit arguments
# ---------------------------------------------------------------
# From the dataset directory we obtain automatically FirstLevelModel objects
# with their subject_id filled from the BIDS dataset. Moreover we obtain
# for each model the list of run imgs and their respective events and
# confounder regressors. Confounders are inferred from the confounds.tsv files
# available in the BIDS dataset.
# To get the first level models we have to specify the dataset directory,
# the task_label and the space_label as specified in the file names.
# We also have to provide the folder with the desired derivatives, that in this
# case were produced by the fmriprep BIDS app.
from nistats.first_level_model import first_level_models_from_bids
task_label = 'stopsignal'
space_label = 'MNI152NLin2009cAsym'
derivatives_folder = 'derivatives/fmriprep'
print(data_dir)
models, models_run_imgs, models_events, models_confounds = \
    first_level_models_from_bids(
        data_dir, task_label, space_label, smoothing_fwhm=5.0,
        derivatives_folder=derivatives_folder)

#############################################################################
# Take model and model arguments of the subject and process events
model, imgs, events, confounds = (
    models[0], models_run_imgs[0], models_events[0], models_confounds[0])
subject = 'sub-' + model.subject_label

import os
from nistats.utils import get_design_from_fslmat
fsl_design_matrix_path = os.path.join(
    data_dir, 'derivatives', 'task', subject, 'stopsignal.feat', 'design.mat')
design_matrix = get_design_from_fslmat(
    fsl_design_matrix_path, column_names=None)

#############################################################################
# We identify the columns of the Go and StopSuccess conditions of the
# design matrix inferred from the fsl file, to use them later for contrast
# definition.
design_columns = ['cond_%02d' % i for i in range(len(design_matrix.columns))]
design_columns[0] = 'Go'
design_columns[4] = 'StopSuccess'
design_matrix.columns = design_columns

############################################################################
# First level model estimation (one subject)
# -------------------------------------------
# We fit the first level model for one subject.
print(design_matrix)
model.fit(imgs, design_matrices=[design_matrix])

#############################################################################
# Then we compute the StopSuccess - Go contrast. We can use the column names
# of the design matrix.
z_map = model.compute_contrast('StopSuccess - Go')

#############################################################################
# We show agreement between the Nistats estimation and the FSL estimation
# available in the dataset
import nibabel as nib
fsl_z_map = nib.load(
    os.path.join(data_dir, 'derivatives', 'task', subject, 'stopsignal.feat',
                 'stats', 'zstat12.nii.gz'))

from nilearn import plotting
import matplotlib.pyplot as plt
from scipy.stats import norm
plotting.plot_glass_brain(z_map, colorbar=True, threshold=norm.isf(0.001),
                          title='Nistats Z map of "StopSuccess - Go" (unc p<0.001)',
                          plot_abs=False, display_mode='ortho')
plotting.plot_glass_brain(fsl_z_map, colorbar=True, threshold=norm.isf(0.001),
                          title='FSL Z map of "StopSuccess - Go" (unc p<0.001)',
                          plot_abs=False, display_mode='ortho')
plt.show()

from nistats.reporting import compare_niimgs
compare_niimgs([z_map], [fsl_z_map], model.masker_,
               ref_label='Nistats', src_label='FSL')
plt.show()

#############################################################################
# Simple statistical report of thresholded contrast
# -----------------------------------------------------
# We display the contrast plot and table with cluster information
from nistats.reporting import plot_contrast_matrix
plot_contrast_matrix('StopSuccess - Go', design_matrix)
plotting.plot_glass_brain(z_map, colorbar=True, threshold=norm.isf(0.001),
                          plot_abs=False, display_mode='z',
                          figure=plt.figure(figsize=(4, 4)))
plt.show()

###############################################################################
# We can get a latex table from a Pandas Dataframe for display and publication
from nistats.reporting import get_clusters_table
print(get_clusters_table(z_map, norm.isf(0.001), 10).to_latex())
