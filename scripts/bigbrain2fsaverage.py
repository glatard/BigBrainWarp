print('importing libraries')
import numpy as np
import nibabel
import scipy.io as io
import sys

print('assigning arguments')
lhData=str(sys.argv[1])
rhData=str(sys.argv[2])
outName=str(sys.argv[3])
bbwDir=str(sys.argv[4])

# load and vectorise surface data
x = lhData.split(".")
ext = x[-1]
if ext == 'annot':
    lhInput = nibabel.freesurfer.io.read_annot(lhData)
    rhInput = nibabel.freesurfer.io.read_annot(rhData)
elif ext == 'txt':
    lhInput = np.loadtxt(lhData)
    rhInput = np.loadtxt(rhData)
elif ext == 'gii':
    lhInput = nibabel.gifti.giftiio.read(lhData)
    rhInput = nibabel.gifti.giftiio.read(rhData)
elif ext == 'mgh':
    lhInput = nibabel.freesurfer.mghformat.read(lhData)
    rhInput = nibabel.freesurfer.mghformat.read(rhData)
else:
    print("incompatible datatype")
    sys.exit()

# check size
compatSizes = np.array(163842)
if lhInput.shape!=rhInput.shape:
    print('hemispheric data not the same size')
    sys.exit()
if lhInput.shape[0] not in compatSizes:
    print("invalid number of vertices")
    sys.exit()

# load indexing
mat = io.loadmat(bbwDir + "/scripts/nn_surface_indexing.mat")
nn_bb_fs = np.array(mat["nn_bb_fs"])

print("reindexing data to fsaverage")
data_bb = np.array(np.concatenate((lhInput, rhInput), axis=0))
data_fs = data_bb[nn_bb_fs[0]]

print("writing out as text file")
np.savetxt(outName+'_fsaverage5.txt', data_fs, delimiter=',')
