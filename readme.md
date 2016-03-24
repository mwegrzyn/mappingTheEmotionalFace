# Mapping the emotional face.
## How individual face parts contribute to successful emotion recognition.

Martin Wegrzyn, Maria Vogt, Berna Kireclioglu, Julia Schneider & Johanna Kissler
in preparation

### Abstract

Which facial features allow human observers to successfully recognize expressions of emotion? While the eyes and mouth have been frequently shown to be of high importance, research on facial action units has made more precise predictions about the areas involved in displaying each emotion. If human observers are able to efficiently decode individual facial signals, their ability should be reflected in a fine-grained pattern of weights across the face, indicating the most diagnostic areas for each expression.
In the present experiment, emotional faces were hidden behind a mask of 48 tiles, which was sequentially uncovered. Participants were instructed to stop the sequence of unmasking as soon as they recognized the facial expression and assign it the correct label. This gave rise to a set of weight patterns across each face, with most variance explained by the eye and mouth regions. Furthermore, the difference in the importance of eyes and mouth allowed to group the expressions in a continuous space, ranging from sadness and fear (reliance on the eyes) to disgust and happiness (mouth). The face parts with highest diagnostic value were typically located in areas corresponding to action units from the facial action coding system.
A similarity analysis of the weights for every expression demonstrated that faces cluster together by the emotion they express. Also, expressions relying more on the eyes or mouth region are in close proximity in the constructed similarity space. We argue that our analyses can help to better understand the way human observers represent expressions of emotion, and can indicate which expressions will be recognized most readily and which ones will most likely be confused.

### About

This is a repository containing the full data and code of our paper about masked facial expressions (work in progress!).  

### Table of Contents


- the code
  - [Data Import](code001_dataImport.ipynb)
  - [Global Metrics for each Face](code002_globalMetrics.ipynb)
  - [Computation of Mask Weights](code003_weighting.ipynb)
  - [Analysis by Action Units and Upper/Lower Face Half](code004_actionUnits_and_upperLower.ipynb)
  - [PCA](code005_principalComponentAnalysis.ipynb)
  - [RSA](code006_representationalSimilarityAnalysis.ipynb)
  - [Interactive Reconstruction of each trial form every participant](code007_interactivePlots.ipynb)
  - [More Complex Action Unit Analysis (Bonus)](code008_actionUnits_interactive.ipynb)
  - [Main Results as Python Slides](mappingTheFaceSlides.ipynb)
- [the whole experiment, to be run in the browser](experiment/)
- [the participant logfiles, published under a public domain license](rawTables/)
- [hand-drawn Action Units](auLabels/)

### Requirements

Data analysis was performed with Python 2.7.11 [www.python.org](http://www.python.org) using mainly NumPy, SciPy, Pandas, scikit-learn, Matplotlib, Seaborn and the Jupyter Notebook, all as provided with Anaconda 2.2.5 (Continuum Analytics; [docs.continuum.io/anaconda](http://docs.continuum.io/anaconda)).

### Contact

For questions or comments please write to [martin.wegrzyn@uni-bielefeld.de](mailto:martin.wegrzyn@uni-bielefeld.de)
