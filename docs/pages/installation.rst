Installation
==================

1. Clone the GitHub repository to your local machine (https://github.com/caseypaquola/BigBrainWarp.git)
2. Edit the first three lines of 'BigBrainWarp/scripts/init.sh' file based on the specific paths of your machine
3. Prior to running any scripts, set the necessary global environment variables

.. code-block:: bash

	bash BigBrainWarp/scripts/init.sh
	source BigBrainWarp/scripts/init.sh


Dependencies
**************

We've included some small dependencies in the GitHub repository. In addition, 

* All transformations require `MINC2 <https://github.com/BIC-MNI/minc-toolkit-v2>`_ and `FSL <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki>`_
* Surface-based transformations use python (tested on 2.7), including `numpy <https://numpy.org/>`_, `scipy <https://www.scipy.org/>` and `nibabel <https://nipy.org/nibabel/index.html>`_ packages

These can be located anywhere on your system, just ensure that they are in your PATH and the functions are callable from your command line.


Tips for Getting Started
****************************

* Follow the tutorials to get an understanding of BigBrain-MRI analysis strategies
* Check out the Glossary and FAQ sections
* Use the hyperlinks to find related papers
* Get in touch if you have any questions 🤙


