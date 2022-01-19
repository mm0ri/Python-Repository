import PySimpleGUI as sg
import math

#                  1                 2                3                4
ATable = [[0.5 , 0.5 , 0], [0.4, 0.3 ,0.3], [0.3, 0.4, 0.3], [0.4, 0.4, 0.2]] 
BTable = [[2,     1,   1], [3,    1,    0], [2,    2,    0], [1,    2,    1]]
My = 0.3

def make_Win_First():
    layout =[[sg.Text('Calculate.')],
            [sg.Text('Enter Variant A')],     
            [sg.Input()],
            [sg.Text('Enter Variant B1')],      
            [sg.Input()],
            [sg.Text('Enter Variant B2')],
            [sg.Input()],      
            [sg.Button('Calculate'),sg.Exit()]]       
    return sg.Window('Window Title', layout, size = (350, 230), finalize=True)

window1, window2 = make_Win_First(), None

def logic():
    VariantA = int(values[0])
    VariantB1 = int(values[1])
    VariantB2 = int(values[2])

    Lamd1 = ATable[VariantA-1][0]
    Lamd2 = ATable[VariantA-1][1]
    Lamd3 = ATable[VariantA-1][2]
    
    Alph1 = Lamd1 / My
    Alph2 = Lamd2 / My
    Alph3 = Lamd3 / My

    H1 = BTable[VariantB1-1][0]
    H2 = BTable[VariantB1-1][1]
    H3 = BTable[VariantB1-1][2]

    HH1 = BTable[VariantB2-1][0]
    HH2 = BTable[VariantB2-1][1]
    HH3 = BTable[VariantB2-1][2]

    def formH3(Alph, Lamd):
        p0 = ( 1 / ( 1 + Alph + (Alph ** 2 / math.factorial(2)) + (Alph ** 3 / math.factorial(3))))
        p1 = p0 * Alph
        p2 = p0 * ( Alph ** 2) / (math.factorial(2))
        p3 = p0 * ( Alph ** 3) / (math.factorial(3))
        a = (1 - p3) * Lamd
        return a

    def formH2(Alph, Lamd):
        p0 = ( 1 / ( 1 + Alph + (Alph ** 2 / math.factorial(2))))
        p1 = p0 * Alph
        p2 = p0 * ((Alph ** 2) / (math.factorial(2)))
        a = (1 - p2) * Lamd
        return a

    def formH1(Alph, Lamd):
        p0 = ( 1 / ( 1 + Alph))
        p1 = p0 * Alph
        a = (1 - p1) * Lamd
        return a

    def formH0(Alph,Lamd):
        a = 0
        return a

    if VariantB1 == 1:
        Res1 = formH2(Alph1, Lamd1)
        Res2 = formH1(Alph2, Lamd2)
        Res3 = formH1(Alph3, Lamd3)
        ResB1 = Res1 + Res2 + Res3
        #print(ResB1)

    elif VariantB1 == 2:
        Res1 = formH3(Alph1, Lamd1)
        Res2 = formH1(Alph2, Lamd2)
        Res3 = formH0(Alph3, Lamd3)
        ResB1 = Res1 + Res2 + Res3
        #print(ResB1)

    elif VariantB1 == 3:
        Res1 = formH2(Alph1, Lamd1)
        Res2 = formH2(Alph2, Lamd2)
        Res3 = formH0(Alph3, Lamd3)
        ResB1 = Res1 + Res2 + Res3
        #print(ResB1)

    elif VariantB1 == 4:
        Res1 = formH1(Alph1, Lamd1)
        Res2 = formH2(Alph2, Lamd2)
        Res3 = formH1(Alph3, Lamd3)
        ResB1 = Res1 + Res2 + Res3
        #print(ResB1)
        
    if VariantB2 == 1:
        Res1 = formH2(Alph1, Lamd1)
        Res2 = formH1(Alph2, Lamd2)
        Res3 = formH1(Alph3, Lamd3)
        ResB2 = Res1 + Res2 + Res3
        #print(ResB2)

    if VariantB2 == 2:
        Res1 = formH3(Alph1, Lamd1)
        Res2 = formH1(Alph2, Lamd2)
        Res3 = formH0(Alph3, Lamd3)
        ResB2 = Res1 + Res2 + Res3
        #print(ResB2)

    elif VariantB2 == 3:
        Res1 = formH2(Alph1, Lamd1)
        Res2 = formH2(Alph2, Lamd2)
        Res3 = formH0(Alph3, Lamd3)
        ResB2 = Res1 + Res2 + Res3
        #print(ResB2)

    elif VariantB2 == 4:
        Res1 = formH1(Alph1, Lamd1)
        Res2 = formH2(Alph2, Lamd2)
        Res3 = formH1(Alph3, Lamd3)
        ResB2 = Res1 + Res2 + Res3
        #print(ResB2)
    return ResB1, ResB2   

def make_Win_Second():
    layout =[[sg.Text('Results of calculation:\n\nVariant B1:\n{0}\n\nVariant B2:\n{1}\n\nFinal results:\n{0} > {1}'.format(res_b1, res_b2))],    
            [sg.Exit()]]       
    return sg.Window('Window Title', layout, size = (350, 200), finalize=True)

def make_Win_Third():
    layout =[[sg.Text('Results of calculation:\n\nVariant B1:\n{0}\n\nVariant B2:\n{1}\n\nFinal results:\n{1} > {0}'.format(res_b1, res_b2))],    
            [sg.Exit()]]       
    return sg.Window('Window Title', layout, size = (350, 200), finalize=True)

while True:

    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        if window == window2:
            window2 = None
        elif window == window1:
            break 
    elif event == 'Calculate':
        window.close()
        res_b1, res_b2 = logic()
        res_b1, res_b2 = round(res_b1, 3), round(res_b2, 3) 
        #window2 = make_Win_Second()
        if res_b1 > res_b2:    
            window2 = make_Win_Second()
            if event == sg.WIN_CLOSED or event == 'Exit':
                #window.close()
                break
        elif res_b2 > res_b1:
            if event == sg.WIN_CLOSED or event == 'Exit':
                #window.close()
                break
            window2 = make_Win_Third()
    window.close()
        