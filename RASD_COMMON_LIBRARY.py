######################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR         ENG. CIVIL / PROF (UFCAT)
# ROMES ANTÔNIO BORGES                             MATE / PROF (UFCAT)
# DONIZETTI APARECIDO DE S. JÚNIOR                  ENG. CIVIL (UFCAT)
######################################################################

######################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIO. PRODES DE ALGORITMOS ESTOCÁSTICOS DE CONFIABILIDADE
######################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

################################################################################
# BIBLIOTECAS DESENVOLVEDORES GPEE
def SAMPLING(SETUP):
    """
    THIS FUNCTION GENERATES RANDOM SAMPLES ACCORDING ,
    TO CHOICE SAMPLING METHOD
    
    INPUT:,
    SETUP: STOCHASTIC RANDOM VARIABLES DESCRIPTION (DICTIONARY MIXED)

    OUTPUT:
    RANDOM_SAMPLING: STOCHASTIC RANDOM SAMPLING (NP.ARRAY, FLOAT)
    """

    # START RESERVED SPACE FOR SAMPLING
    N_SAMPLING = SETUP['TOTAL SAMPLING']
    D = SETUP['TOTAL DESIGN VARIABLES']
    MODEL = SETUP['MODEL']
    RANDOM_SAMPLING = np.zeros((N_SAMPLING, D))
    if MODEL == 'MCS':
        for I_COUNT in range(D):
            # SETUP TYPE, MEAN AND STD I VARIABLE
            TYPE = SETUP['VARS'][I_COUNT][0]
            MEAN = SETUP['VARS'][I_COUNT][1]
            STD = SETUP['VARS'][I_COUNT][2]
            # NORMAL AND GAUSSIAN DISTRIBUITION
            if (TYPE == 'GAUSSIAN' or TYPE == 'NORMAL'):
                RANDOM_NUMBERS = np.random.normal(MEAN, STD, N_SAMPLING)
                RANDOM_SAMPLING[:, I_COUNT] = RANDOM_NUMBERS
            # GUMBEL MAXIMUM DISTRIBUITION
            elif TYPE == 'GUMBEL MAX':
                RANDOM_NUMBERS = np.random.gumbel(MEAN, STD, N_SAMPLING)
                RANDOM_SAMPLING[:, I_COUNT] = RANDOM_NUMBERS
            # LOGNORMAL DISTRIBUITION
            elif TYPE == 'LOGNORMAL':
                RANDOM_NUMBERS = np.random.lognormal(MEAN, STD, N_SAMPLING)
                RANDOM_SAMPLING[:, I_COUNT] = RANDOM_NUMBERS
            # GAMMA DISTRIBUITION
            elif TYPE == 'GAMMA':
                RANDOM_NUMBERS = np.random.gamma(MEAN, STD, N_SAMPLING)
                RANDOM_SAMPLING[:, I_COUNT] = RANDOM_NUMBERS
            # DONIZETTI ADD OUTRAS DISTRIBUIÇÕES
            ####
            ####
            ####
            ####
            ####
    elif MODEL == 'LHS':
        pass
        # DONIZETTI ADD O LHS
        #####
        #####
        #####
    return RANDOM_SAMPLING