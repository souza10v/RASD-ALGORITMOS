import RASD_COMMON_LIBRARY as RASD_CL
import numpy as np

def RASD(SETUP, OBJ):
    """
    THIS FUNCTION GENERATES RANDOM SAMPLES ACCORDING ,
    TO CHOICE SAMPLING METHOD
    
    INPUT:,
    SETUP: STOCHASTIC RANDOM VARIABLES DESCRIPTION (DICTIONARY MIXED)

    OUTPUT:
    RANDOM_SAMPLING: STOCHASTIC RANDOM SAMPLING (NP.ARRAY, FLOAT)
    """  
    # CREATING SAMPLES   
    DATASET_X = RASD_CL.SAMPLING(SETUP)
    # SETUP
    N_SAMPLING = SETUP['TOTAL SAMPLING']
    N_G = SETUP['TOTAL G FUNCTIONS']
    D = SETUP['TOTAL DESIGN VARIABLES']
    # CREATING EMPTY RESULTS
    RESULTS_X = np.zeros((N_SAMPLING, D))
    RESULTS_G = np.zeros((N_SAMPLING, N_G))
    RESULTS_I = np.zeros((N_SAMPLING, N_G))
    # LOPPING CHECK STATE LIMITE FUNCTIONS
    for I_COUNT in range(N_SAMPLING):
        SAMPLE = DATASET_X[I_COUNT, :]
        G = OBJ(SAMPLE)
        for J_COUNT in range(D):
            RESULTS_X[I_COUNT, J_COUNT] = DATASET_X[I_COUNT, J_COUNT]
        for K_COUNT in range(N_G):
            RESULTS_G[I_COUNT, K_COUNT] = G[K_COUNT]
            if G[K_COUNT] >= 0: 
                I = 0
                RESULTS_I[I_COUNT, K_COUNT] = I
            elif G[K_COUNT] < 0: 
                I = 1
                RESULTS_I[I_COUNT, K_COUNT] = I 
    RESULTS = np.hstack((RESULTS_X, RESULTS_G, RESULTS_I))               
    return RESULTS