
# image and mask variables
imgSize = (300,400)
squareSize = 50

assert imgSize[0]/squareSize == float(imgSize[0])/squareSize, 'image columns not divisible by tiles'
assert imgSize[1]/squareSize == float(imgSize[1])/squareSize, 'image rows not divisible by tiles'

numRow = imgSize[0]/squareSize
numCol = imgSize[1]/squareSize

# timing variables
waitTime = 1000
isi = 100 # inter-stimulus interval


# arrays with stimuli
# structure: stim[identity][expression]

stim = [['img/f_hap_cut.png',
'img/f_sad_cut.png',
'img/f_ang_cut.png',
'img/f_fea_cut.png',
'img/f_dis_cut.png',
'img/f_sup_cut.png',
'img/f_ntr_cut.png'],
['img/m_hap_cut.png',
'img/m_sad_cut.png',
'img/m_ang_cut.png',
'img/m_fea_cut.png',
'img/m_dis_cut.png',
'img/m_sup_cut.png',
'img/m_ntr_cut.png']]
