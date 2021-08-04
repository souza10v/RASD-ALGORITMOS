"""
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::..::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::...::...:::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::..:!%@&&@%!:..::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::..:!%@###@@###@%!:..:::::::::::::::::::::::::::::::
::::::::::::::::::::::::::..:!%@##&$*::::*$&##@%!:..::::::::::::::::::::::::::::
::::::::::::::::::::::::::!%&##&$*::*$&&$*::*$&##&%!::::::::::::::::::::::::::::
::::::::::::::::::::::::.$##&$*::*@&##@@&@*.:::!$&##$.::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&!.:@####%:..::!$&&@*.:&#@:::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&:.:!%&##&$**$&##&&##::&#@:::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&::$%::!%@####&%!:$#&::&#$:::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&::##@...:!%%!:...$#&!:*:::::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&::&#@.:::....:::.$#&!.*$$:::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&::##&!:..::::..:!@##!:&#@:::::::::::::::::::::::::::
::::::::::::::::::::::::.@#&::$&##@%!:..:!%@##&$::&#@:::::::::::::::::::::::::::
::::::::::::::::::::::::.@##@*::*$&##@$%@##&$*::*@##@:::::::::::::::::::::::::::
::::::::::::::::::::::::::%@##&@*::*$&##&$*::*$&##@%!:::::::::::::::::::::::::::
:::::::::::::::::::::::::..:!%@###@*::!!::*@###@%!:..:::::::::::::::::::::::::::
::::::::::::::::::::::::::::...:*@###@%%@###@%!:..::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::...:*$&##&@*:...:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::...:**:...::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::...:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::........::.......::........:........:::::::::::::::::::::::
:::::::::::::::::::::%$$$$$$*.:%$$$$$%::*$$$$$$*:%$$$$$$*:::::::::::::::::::::::
:::::::::::::::::::::&&****@#:%#%***$#*!#$*****!:&&****@&:::::::::::::::::::::::
:::::::::::::::::::::&&@@@$@$.%#@@@@@#*:@@$@@@@*:&@....$&:::::::::::::::::::::::
:::::::::::::::::::::&@:%&@*!.$#!:::*#*:!*****#@.&@!!!!@#:::::::::::::::::::::::
:::::::::::::::::::::$%..:$@$:*@:...!@!:@@@@@@@!:$@@@@@@%:::::::::::::::::::::::
:::::::::::::::::::::..::....::.:::::.:::.......:.....:..:::::::::::::::::::::::
"""
################################################################################
# UNIVERSIDADE FEDERAL DE CATALÃO (UFCAT)
# WANDERLEI MALAQUIAS PEREIRA JUNIOR                   ENG. CIVIL / PROF (UFCAT)
# ROMES ANTÔNIO BORGES                                       MAT. / PROF (UFCAT)
# DONIZETTI A. DE SOUZA JÚNIOR                                ENG. CIVIL (UFCAT)
################################################################################

################################################################################
# DESCRIÇÃO ALGORITMO:
# BIBLIOTECA GRÁFICA PARA ANÁLISE DE CONFIABILIDADE ESTRUTURAL DESENVOLVIDA 
# PELO GRUPO DE PESQUISAS E ESTUDOS EM ENGENHARIA (GPEE)
################################################################################

################################################################################
# BIBLIOTECAS NATIVAS PYTHON
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

################################################################################
# BIBLIOTECAS DESENVOLVEDORES GPEE 
def CONVERT_SI_TO_INCHES(WIDTH, HEIGHT):
    """ 
    THIS FUNCTION CONVERT FIGURE SIZE SI TO INCHES
    
    INPUT 
    WIDTH: FIGURE WIDTH IN SI UNITS, (FLOAT)
    HEIGHT: FIGURE HEIGHT IN SI UNITS, (FLOAT)
    
    OUTPUT:
    WIDTH: FIGURE WIDTH IN INCHES UNITS, (FLOAT)
    HEIGHT: FIGURE HEIGHT IN INCHES UNITS, (FLOAT)
    """
    WIDTH = WIDTH / 0.0254
    HEIGHT = HEIGHT / 0.0254
    return WIDTH, HEIGHT

# SALVA A FIGURA NA PASTA OU CAMINHO DESEJADO
def SAVE_GRAPHIC(NAME, EXT, DPI):
    """ 
    THIS FUNCTION SAVE GRAPHICS ON A SPECIFIC PATH
    EXTENSIONS OPTIONS : 
    - 'svg'
    - 'png'
    - 'eps'
    - 'pdf'

    INPUT: 
    NAME: PATH + NAME FIGURE (STRING)
    EXT: FILE EXTENSION (STRING)
    DPI: THE RESOLUTION IN DOTS PER INCH (INTEGER)
    """
    plt.savefig(NAME + EXT, dpi = DPI, bbox_inches = 'tight', transparent = True)

# PLOTAGEM 1
def RASD_PLOT_1(DATASET, PLOT_SETUP):
    """
    THIS FUNCTION PLOT BOXPLOT AND HISTOGRAMS IN A SINGLE CHART
    
    INPUT: 
    DATASET: RESULTS ABOUT RASD ALGORITHM (NP.ARRAY[? X ?] FLOAT)
    PLOT_SETUP: CONTAINS THE SPECIFICATION OF EACH MODEL OF CHART
    
    EXTENSION:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    Other Parameters >> format
    AXISES COLOR, LABELS COLOR AND CHART COLOR:
    https://htmlcolorcodes.com/

    OUTPUT:
    N/A

    EXAMPLE:
    # PLOT SETUP
    PLOT_SETUP = {'NAME': 'WANDER',
                    'WIDTH': 0.40, 
                    'HEIGHT': 0.20, 
                    'X AXIS LABEL': '$x_1$ - Dead Load $(kN / m)$',
                    'X AXIS SIZE': 20,
                    'Y AXIS SIZE': 20,
                    'AXISES COLOR': '#000000',
                    'LABELS SIZE': 16,
                    'LABELS COLOR': '#000000',  
                    'CHART COLOR': '#FEB625',
                    'KDE': False,
                    'DPI': 600, 
                    'EXTENSION': '.svg'}
    # RESULTS X_0 VARIABLE
    DATASET = RESULTS_RASD['X_0']            
    # CALL PLOT
    RASD.RASD_PLOT_1(DATASET, PLOT_SETUP)
    """
    # SETUP CHART
    NAME = PLOT_SETUP['NAME']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    CHART_COLOR = PLOT_SETUP['CHART COLOR']
    BINS = PLOT_SETUP['BINS']
    KDE = PLOT_SETUP['KDE']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    sns.set(style = 'ticks')
    # CONVERT UNITS OF SIZE FIGURE
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    # PLOT
    FIG, (AX_BOX, AX_HIST) = plt.subplots(2, figsize = (W, H), sharex = True, gridspec_kw = {'height_ratios': (.15, .85)})
    sns.boxplot(DATASET, ax = AX_BOX, color = CHART_COLOR)
    sns.histplot(DATASET, ax = AX_HIST, kde = KDE, color = CHART_COLOR, bins = BINS)
    AX_BOX.set(yticks = [])
    AX_BOX.set(xlabel='')
    font = {'fontname': 'Arial',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX_HIST.set_xlabel(X_AXIS_LABEL, fontdict = font)
    AX_HIST.set_ylabel('$COUNT$', fontdict = font)
    AX_HIST.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX_HIST.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    sns.despine(ax = AX_HIST)
    sns.despine(ax = AX_BOX, left = True)
    # SAVEFIG
    SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 2
def RASD_PLOT_2(DATASET, PLOT_SETUP):
    """
    THIS FUNCTION PLOT SCATTER CHART X AND Z VARIABLES A FUNCTION OF I VALUE
    
    INPUT: 
    DATASET: RESULTS ABOUT RASD ALGORITHM (NP.ARRAY[? X ?] FLOAT)
    PLOT_SETUP: CONTAINS THE SPECIFICATION OF EACH MODEL OF CHART
    
    LOC LEGEND: 
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
    Other Parameters >> loc
    EXTENSION:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    Other Parameters >> format
    AXISES COLOR AND LABELS COLOR:
    https://htmlcolorcodes.com/

    OUTPUT:
    N/A

    EXAMPLE:
    # PLOT SETUP
    PLOT_SETUP = {'NAME': 'WANDER',
                    'EXTENSION': '.svg',
                    'DPI': 600,
                    'WIDTH': 0.40, 
                    'HEIGHT': 0.20,              
                    'X DATA': 'S_0',
                    'Y DATA': 'R_0',
                    'X AXIS SIZE': 20,
                    'Y AXIS SIZE': 20,
                    'AXISES COLOR': '#000000',
                    'X AXIS LABEL': '$S_0$',
                    'Y AXIS LABEL': '$R_0$',
                    'LABELS SIZE': 16,
                    'LABELS COLOR': '#000000',
                    'LOC LEGEND': 'lower right',
                    'TITLE LEGEND': 'Failure index ($I$):'}
    # RESULTS
    DATASET = RESULTS_RASD
    # CALL PLOT
    RASD.RASD_PLOT_2(DATASET, PLOT_SETUP)
    """
    # SETUP CHART
    NAME = PLOT_SETUP['NAME']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    X_DATA = PLOT_SETUP['X DATA']
    Y_DATA = PLOT_SETUP['Y DATA']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    LOC_LEGEND = PLOT_SETUP['LOC LEGEND']
    TITLE_LEGEND = PLOT_SETUP['TITLE LEGEND']
    sns.set(style = 'ticks')
    # CONVERT UNITS OF SIZE FIGURE
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    # PLOT
    FIG, AX = plt.subplots(figsize = (W, H))
    sns.scatterplot(data = DATASET, x = X_DATA, y = Y_DATA, hue = 'I')
    font = {'fontname': 'Arial',
        'color':  LABELS_COLOR,
        'weight': 'bold',
        'size': LABELS_SIZE}
    AX.set_xlabel(X_AXIS_LABEL, fontdict = font)
    AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
    AX.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    AX.legend(loc = LOC_LEGEND, title = TITLE_LEGEND)
    # SAVEFIG
    SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 3
def RASD_PLOT_3(DATASET, PLOT_SETUP):
    """
    THIS FUNCTION PLOT SCATTER CHART X AND Z VARIABLES A FUNCTION OF G VALUE
    
    INPUT: 
    DATASET: RESULTS ABOUT RASD ALGORITHM (NP.ARRAY[? X ?] FLOAT)
    PLOT_SETUP: CONTAINS THE SPECIFICATION OF EACH MODEL OF CHART
    
    COLOR MAP: 
    https://matplotlib.org/stable/tutorials/colors/colormaps.html
    Other Parameters >> loc
    EXTENSION:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    Other Parameters >> format
    AXISES COLOR AND LABELS COLOR:
    https://htmlcolorcodes.com/

    OUTPUT:
    N/A

    EXAMPLE:
    # PLOT SETUP
    PLOT_SETUP = {'NAME': 'WANDER',
                    'EXTENSION': '.svg',
                    'DPI': 600,
                    'WIDTH': 0.20, 
                    'HEIGHT': 0.10,              
                    'X DATA': 'S_0',
                    'Y DATA': 'R_0',
                    'X AXIS SIZE': 20,
                    'Y AXIS SIZE': 20,
                    'AXISES COLOR': '#000000',
                    'X AXIS LABEL': '$S_0$',
                    'Y AXIS LABEL': '$R_0$',
                    'LABELS SIZE': 16,
                    'LABELS COLOR': '#000000',
                    'C VALUE': 'G_0',
                    'TRANSPARENCY': 0.8,
                    'COLOR MAP': 'viridis'}
    # RESULTS
    DATASET = RESULTS_RASD
    # CALL PLOT
    RASD.RASD_PLOT_3(DATASET, PLOT_SETUP)
    """
    # SETUP CHART
    NAME = PLOT_SETUP['NAME']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    X_DATA = PLOT_SETUP['X DATA']
    Y_DATA = PLOT_SETUP['Y DATA']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    C_VALUE = PLOT_SETUP['C VALUE']
    TRANSPARENCY = PLOT_SETUP['TRANSPARENCY']
    COLOR_MAP = PLOT_SETUP['COLOR MAP']
    # CONVERT UNITS OF SIZE FIGURE
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    # PLOT
    AUX = plt.Normalize(DATASET[C_VALUE].min(), DATASET[C_VALUE].max())
    FIG, AX = plt.subplots(figsize = (W, H))
    plt.scatter(x = DATASET[X_DATA], y = DATASET[Y_DATA], c = DATASET[C_VALUE], cmap = COLOR_MAP, alpha = TRANSPARENCY)
    font = {'fontname': 'Arial',
        'color':  LABELS_COLOR,
        'weight': 'bold',
        'size': LABELS_SIZE}
    AX.set_xlabel(X_AXIS_LABEL, fontdict = font)
    AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
    AX.tick_params(axis= 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX.tick_params(axis= 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    AUX1 =  ScalarMappable(norm = AUX, cmap = COLOR_MAP)
    FIG.colorbar(AUX1, ax = AX)
    # SAVEFIG
    SAVE_GRAPHIC(NAME, EXT, DPI)

# PLOTAGEM 4
def RASD_PLOT_4(DATASET, PLOT_SETUP):
    """
    THIS FUNCTION PLOTS TWO HISTOGRAMS IN A SINGLE ONE CHART

    INPUT:
    DATASET: RESULTS ABOUT RASD ALGORITHM (NP.ARRAY[? X ?] FLOAT)
    PLOT_SETUP: CONTAINS THE SPECIFICATION OF EACH CHART MODEL

    COLOR MAP:
    https://matplotlib.org/stable/tutorials/colors/colormaps.html
    Other Parameters >> loc
    EXTENSION:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    Other Parameters >> format
    AXISES COLOR AND LABELS COLOR:
    https://htmlcolorcodes.com/

    OUTPUT:
    N/A

    EXAMPLE:
    # PLOT SETUP
    PLOT_SETUP = {'NAME': 'WANDER',
                    'EXTENSION': '.svg',
                    'DPI': 600,
                    'WIDTH': 0.20,
                    'HEIGHT': 0.10,
                    'X DATA': 'S_0',
                    'Y DATA': 'R_0',
                    'X AXIS SIZE': 20,
                    'Y AXIS SIZE': 20,
                    'AXISES COLOR': '#000000',
                    'X AXIS LABEL': '$S_0 R_0$',
                    'Y AXIS LABEL': '$SOMATÓRIO$',
                    'LABELS SIZE': 16,
                    'LABELS COLOR': '#000000',
                    'C VALUE': 'G_0',
                    'TRANSPARENCY': 0.8,
                    'COLOR MAP': 'viridis',
                    'BINS': '50',
                    'ALPHA': '0.6'}
    # RESULTS
    DATASET = RESULTS_RASD
    # CALL PLOT
    RASD.RASD_PLOT_4(DATASET, PLOT_SETUP)
    """
    # SETUP CHART
    NAME = PLOT_SETUP['NAME']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    X_DATA = PLOT_SETUP['X DATA']
    Y_DATA = PLOT_SETUP['Y DATA']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    C_VALUE = PLOT_SETUP['C VALUE']
    TRANSPARENCY = PLOT_SETUP['TRANSPARENCY']
    COLOR_MAP = PLOT_SETUP['COLOR MAP']
    BINS = int(PLOT_SETUP['BINS'])
    ALPHA = float(PLOT_SETUP['ALPHA'])
    # CONVERT UNITS OF SIZE FIGURE
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    # PLOT

    plt.subplots(figsize=(W, H))
    plt.hist(DATASET['R_0'], bins=BINS, label='$R_0$', alpha=ALPHA)
    plt.hist(DATASET['S_0'], bins=BINS, label='$S_0$', alpha=ALPHA)
    plt.legend()

    plt.xlabel(X_AXIS_LABEL)
    plt.ylabel(Y_AXIS_LABEL)

    #plt.tick_params(axis='x', labelsize=X_AXIS_SIZE, colors=AXISES_COLOR)
    #plt.tick_params(axis='y', labelsize=Y_AXIS_SIZE, colors=AXISES_COLOR)
    #AUX_1 = ScalarMappable(norm=AUX, cmap=COLOR_MAP)
    #FIG.colorbar(AUX_1)
    # SAVEFIG
    SAVE_GRAPHIC(NAME, EXT, DPI)
    
    
    """
    RESULTS_RASD: RELIABILITY ANALYSIS RESULTS (DATAFRAME [N_POP, D + N_G * 2 + 2], FLOAT)
    N_SAMPLIG: TOTAL SAMPLES
    D: DIMENSION PROBLEM
    N_G: TOTAL STATE LIMIT FUNCTIONS
    +2 : RESISTANCE AND DEMAND COLUMNS IN NP.ARRAY

    STOCHASTIC RASD EXAMPLE:
    >>> # CHARACTERISTICS OF THE VARIABLES 
    >>> V_1 = ['NORMAL', 500, 100]
    >>> V_2 = ['NORMAL', 1000, 1000]
    >>> # DICTIONARY
    >>> SETUP = {'REPETITIONS': 1,
                 'TOTAL SAMPLING': 10,
                 'TOTAL G FUNCTIONS': 1,
                 'TOTAL DESIGN VARIABLES': 2,
                 'VARS': [V_1, V_2],
                 'MODEL': 'MCS'}     
    >>> # MCS - SIMPLE MONTE CARLO SAMPLING
    >>> # LHS - LATIN HYPER CUBE SAMPLING
    >>> # STATE LIMIT FUNCTIONS
    >>> def OF_FUNCTION(X):
            R = []
            S = []
            G = []
            D0 = 3
            Length = 100
            E = 30 * 10**6
            W = 2
        T = 4
        Px = X[0]
        Py = X[1]
        # LIMIT
        R_1 = D0
        # DEMAND                      
        S_1 = (4 * Length ** 3 / (E * W * T)) * (((Py / T ** 2) ** 2  + (Px / W ** 2) ** 2) ** 0.5)
        # STATE LIMIT FUNCTION
        G_1 = R_1 - S_1
        R = [R_1] 
        S = [S_1] 
        G = [G_1]
    return R, S, G
    # CALL RASD
    RESULTS_TEST = RASD.MAIN_STOCHASTIC(SETUP, OF_FUNCTION)
    # RESULTS
    print(RESULTS_TEST)
    ###################################################
    X_1         X_2         R_1     S_1     G_1     I
    4.25e+02    2.10e+02    3.00    2.82    0.18    0
    ...
    ...
    ...
    4.72e+02    3.35e+03    3.00    4.00   -1.00    1
    ###################################################
    """  