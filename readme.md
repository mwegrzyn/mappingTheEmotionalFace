# Mapping the emotional face.
## How individual face parts contribute to successful emotion recognition.

Martin Wegrzyn, Maria Vogt, Berna Kireclioglu, Julia Schneider & Johanna Kissler
Published: May 11, 2017  
[DOI: 10.1371/journal.pone.0177239](http://dx.doi.org/10.1371/journal.pone.0177239)

### Abstract

Which facial features allow human observers to successfully recognize expressions of emotion? While the eyes and mouth have been frequently shown to be of high importance, research on facial action units has made more precise predictions about the areas involved in displaying each emotion. The present research investigated on a fine-grained level, which physical features are most relied on when decoding facial expressions.
In the experiment, individual faces expressing the basic emotions according to Ekman were hidden behind a mask of 48 tiles, which was sequentially uncovered. Participants were instructed to stop the sequence as soon as they recognized the facial expression and assign it the correct label. For each part of the face, its contribution to successful recognition was computed, allowing to visualize the importance of different face areas for each expression. Overall, observers were mostly relying on the eye and mouth regions when successfully recognizing an emotion. Furthermore, the difference in the importance of eyes and mouth allowed to group the expressions in a continuous space, ranging from sadness and fear (reliance on the eyes) to disgust and happiness (mouth). The face parts with highest diagnostic value for expression identification were typically located in areas corresponding to action units from the facial action coding system.
A similarity analysis of the usefulness of different face parts for expression recognition demonstrated that faces cluster according to the emotion they express, rather than by low-level physical features. Also, expressions relying more on the eyes or mouth region were in close proximity in the constructed similarity space. These analyses help to better understand how human observers process expressions of emotion, by delineating the mapping from facial features to psychological representation.

### About

This is a repository containing the full data and code of our paper about masked facial expressions.

### Table of Contents


- the code
  - [Data Import](notebooks/code001_dataImport.ipynb)
  - [Global Metrics for each Face](notebooks/code002_globalMetrics.ipynb)
  - [Computation of Mask Weights](notebooks/code003_weighting.ipynb)
  - [Analysis by Action Units and Upper/Lower Face Half](notebooks/code004_actionUnits_and_upperLower.ipynb)
  - [PCA](notebooks/code005_principalComponentAnalysis.ipynb)
  - [RSA](notebooks/code006_representationalSimilarityAnalysis.ipynb)
  - [Interactive Reconstruction of each trial form every participant](notebooks/code007_interactivePlots.ipynb)
  - [More Complex Action Unit Analysis (Bonus)](notebooks/code008_actionUnits_interactive.ipynb)
- [the whole experiment, to be run in the browser](experiment/)
- [the participant logfiles, published under a public domain license](rawTables/)
- [hand-drawn Action Units](auLabels/)

### Requirements

Data analysis was performed with Python 2.7.11 [www.python.org](http://www.python.org) using mainly NumPy, SciPy, Pandas, scikit-learn, Matplotlib, Seaborn and the Jupyter Notebook, all as provided with Anaconda 2.2.5 (Continuum Analytics; [docs.continuum.io/anaconda](http://docs.continuum.io/anaconda)).

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)
