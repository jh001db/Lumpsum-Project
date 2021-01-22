import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.text('')

st.markdown("<h1 style='text-align: center;'>LumpSum Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Met de knoppen in het menu kunt u kijken hoe verschillende factoren invloed hebben op uw pensioen.</h2>", unsafe_allow_html=True)

st.text('')

SB1 = st.sidebar.slider(
        "Lumpsum percentage:", min_value=0, max_value=10)


#Huidige AOW (Pijler 1 Pensioen)
SB12 = 970

#Uw huidige of laatst genoten netto salaris
SB11 = st.sidebar.number_input("Uw huidige of laatst genoten netto salaris", min_value=1280, max_value=12500)

#Verwachte Tweede Pijler Pensioen in EUR - per maand + warning
SB100 = st.sidebar.number_input("Verwachte Tweede Pijler Pensioen in EUR - totaal", min_value=1, max_value=2500000)

#Verwachte tweede pijler pensioen gedeelt door 283 maanden - dit komt neer op een levensverwachting van pensioenleeftijd + 23,5 jaar
SB10 = SB100/283

#Verwachte Derde Pijler Pensioen in EUR - totaal
SB2 = st.sidebar.number_input("Verwachte Derde Pijler Pensioen in EUR - totaal", min_value=0, max_value=2500000, step=1000)
if SB2 > 0:
    # Hoeveel jaar wilt u van uw opgebouwde Derde Pijler Pensioen genieten?
    SB3 = st.sidebar.number_input("Hoeveel jaar wilt u van uw opgebouwde Derde Pijler Pensioen genieten?", min_value=1, max_value=35)
else:
    SB3 = 1


#Verwachte pensioen nodig te hebben
SB4 = st.sidebar.slider('Hoeveel procent van uw huidige verwacht u tijdens uw pensioen nodig te hebben om in uw levensonderhoud te kunnen blijven voorzien?', min_value=40, max_value=140)

if SB4 < 60:
     st.sidebar.warning('Normaliter heeft iemand een goed pensioen als iemand 60% netto ontvangt van het laatst genoten salaris')
else:
    pass


info_2, info_3 = st.beta_columns(2)
with info_2:
    st.markdown("<h1 style='text-align: center;'>Lumpsum %</h1>", unsafe_allow_html=True)
    if SB1 == 0:
        st.markdown("<h2 style='text-align: center;'>Geen</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center;'> {str(SB1) + '%'} </h2>", unsafe_allow_html=True)
with info_3:
    st.markdown("<h1 style='text-align: center;'>In (Bruto) Euro</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'> {'€ '}{SB100*SB1/100:.2f} </h2>", unsafe_allow_html=True)

########################################################################################################################
st.markdown('')

#Pensioen gebaseerd op de drie pijlers van het pensioen en afhankelijk van hoe lang iemand van zijn/haar derde pijler pensioen wil genieten
SB13_1 = SB12 + (SB10*0.99) + (SB2/(SB3*12))
SB13_2 = SB12 + (SB10*0.98) + (SB2/(SB3*12))
SB13_3 = SB12 + (SB10*0.97) + (SB2/(SB3*12))
SB13_4 = SB12 + (SB10*0.96) + (SB2/(SB3*12))
SB13_5 = SB12 + (SB10*0.95) + (SB2/(SB3*12))
SB13_6 = SB12 + (SB10*0.94) + (SB2/(SB3*12))
SB13_7 = SB12 + (SB10*0.93) + (SB2/(SB3*12))
SB13_8 = SB12 + (SB10*0.92) + (SB2/(SB3*12))
SB13_9 = SB12 + (SB10*0.91) + (SB2/(SB3*12))
SB13_10 = SB12 + (SB10*0.90) + (SB2/(SB3*12))
SB13_0 = float(f"{SB12 + SB10+ (SB2/(SB3*12)):.2f}")

#Percentage pensioen tegenover salaris
SB14_1 = float(SB13_1/SB11*100)
SB14_2 = float(SB13_2/SB11*100)
SB14_3 = float(SB13_3/SB11*100)
SB14_4 = float(SB13_4/SB11*100)
SB14_5 = float(SB13_5/SB11*100)
SB14_6 = float(SB13_6/SB11*100)
SB14_7 = float(SB13_7/SB11*100)
SB14_8 = float(SB13_8/SB11*100)
SB14_9 = float(SB13_9/SB11*100)
SB14_10 = float(SB13_10/SB11*100)
SB14_0 = float(SB13_0/SB11*100)

#Verschil tussen geen lumpsum en de verschillende percentages
if SB1 == 1:
    SB14 = SB14_1
elif SB1 == 2:
    SB14 = SB14_2
elif SB1 == 3:
    SB14 = SB14_3
elif SB1 == 4:
    SB14 = SB14_4
elif SB1 == 5:
    SB14 = SB14_5
elif SB1 == 6:
    SB14 = SB14_6
elif SB1 == 2:
    SB14 = SB17_7
elif SB1 == 2:
    SB14 = SB18_8
elif SB1 == 2:
    SB14 = SB19_9
elif SB1 == 2:
    SB14 = SB10_10
else:
    SB14 = SB14_0

if SB2 > 0:
    st.write("Pensioen eerste " + str(SB3) + " jaren inclusief 3e pijler")
else:
    pass

info_1, graph_012, graph_013 = st.beta_columns(3)
with info_1:
    st.markdown("<h1 style='text-align: center;'>Salaris</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'> {'€ ' + str(SB11) +'.-'} </h2>", unsafe_allow_html=True)
with graph_012:
    st.markdown("<h1 style='text-align: center;'>Pensioen</h1>", unsafe_allow_html=True)
    if SB1 == 1:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_1:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 2:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_2:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 3:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_3:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 4:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_4:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 5:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_5:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 6:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_6:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 7:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_7:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 8:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_8:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 9:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_9:.2f}</h2>", unsafe_allow_html=True)
    elif SB1 == 10:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_10:.2f}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13_0:.2f}</h2>", unsafe_allow_html=True)
with graph_013:
    st.markdown("<h1 style='text-align: center;'>Percentage</h1>", unsafe_allow_html=True)
    if SB1 == 1 and SB4 > SB14_1:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 1 and 0 < SB14_1 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_1:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 2 and SB4 > SB14_2:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_2:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 2 and 0 < SB14_2 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_2:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 3 and SB4 > SB14_3:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_3:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 3 and 0 < SB14_3 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_3:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 4 and SB4 > SB14_4:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_4:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 4 and 0 < SB14_4 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_4:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 5 and SB4 > SB14_5:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_5:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 5 and 0 < SB14_5 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_5:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 6 and SB4 > SB14_6:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_6:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 6 and 0 < SB14_6 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_6:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 7 and SB4 > SB14_7:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_7:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 7 and 0 < SB14_7 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_7:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 8 and SB4 > SB14_8:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_8:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 8 and 0 < SB14_8 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_8:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 9 and SB4 > SB14_9:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_9:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 9 and 0 < SB14_9 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_9:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 10 and SB4 > SB14_10:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_10:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    elif SB1 == 10 and 0 < SB14_10 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_10:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif SB1 == 0 and SB4 > SB14_1:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14_0:.1f}{'%'} </font> </h2>",
                    unsafe_allow_html=True)
    elif SB1 == 0 and 0 < SB14_1 < 110:
        st.markdown(f"<h2 style='text-align: center;'>{SB14_0:.1f}{'%'}</h2>", unsafe_allow_html=True)
    else:
        pass

########################################################################################################################
st.markdown('')

#Pensioen gebaseerd op de drie pijlers van het pensioen en afhankelijk van hoe lang iemand van zijn/haar derde pijler pensioen wil genieten
SB23_1 = SB12 + (SB10*0.99)
SB23_2 = SB12 + (SB10*0.98)
SB23_3 = SB12 + (SB10*0.97)
SB23_4 = SB12 + (SB10*0.96)
SB23_5 = SB12 + (SB10*0.95)
SB23_6 = SB12 + (SB10*0.94)
SB23_7 = SB12 + (SB10*0.93)
SB23_8 = SB12 + (SB10*0.92)
SB23_9 = SB12 + (SB10*0.91)
SB23_10 = SB12 + (SB10*0.90)
SB23_0 = float(f"{SB12 + SB10:.2f}")

#Percentage pensioen tegenover salaris
SB24_1 = float(SB23_1/SB11*100)
SB24_2 = float(SB23_2/SB11*100)
SB24_3 = float(SB23_3/SB11*100)
SB24_4 = float(SB23_4/SB11*100)
SB24_5 = float(SB23_5/SB11*100)
SB24_6 = float(SB23_6/SB11*100)
SB24_7 = float(SB23_7/SB11*100)
SB24_8 = float(SB23_8/SB11*100)
SB24_9 = float(SB23_9/SB11*100)
SB24_10 = float(SB23_10/SB11*100)
SB24_0 = float(SB23_0/SB11*100)

#Verschil tussen geen lumpsum en de verschillende percentages
if SB1 == 1:
    SB24 = SB24_1
elif SB1 == 2:
    SB24 = SB24_2
elif SB1 == 3:
    SB24 = SB24_3
elif SB1 == 4:
    SB24 = SB24_4
elif SB1 == 5:
    SB24 = SB24_5
elif SB1 == 6:
    SB24 = SB24_6
elif SB1 == 2:
    SB24 = SB27_7
elif SB1 == 2:
    SB24 = SB28_8
elif SB1 == 2:
    SB24 = SB29_9
elif SB1 == 2:
    SB24 = SB20_20
else:
    SB24 = SB24_0


if SB2 > 0:
    st.write("Pensioen na " + str(SB3) + " jaar, exclusief 3e pijler")
    info_1, graph_014, graph_015 = st.beta_columns(3)
    with info_1:
        st.markdown("<h1 style='text-align: center;'>Salaris</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'> {'€ ' + str(SB11) + '.-'} </h2>", unsafe_allow_html=True)
    with graph_014:
        st.markdown("<h1 style='text-align: center;'>Pensioen</h1>", unsafe_allow_html=True)
        if SB1 == 1:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_1:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 2:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_2:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 3:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_3:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 4:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_4:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 5:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_5:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 6:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_6:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 7:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_7:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 8:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_8:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 9:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_9:.2f}</h2>", unsafe_allow_html=True)
        elif SB1 == 10:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_10:.2f}</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23_0:.2f}</h2>", unsafe_allow_html=True)
    with graph_015:
        st.markdown("<h1 style='text-align: center;'>Percentage</h1>", unsafe_allow_html=True)
        if SB1 == 1 and SB4 > SB24_1:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_1:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 1 and 0 < SB24_1 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_1:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 2 and SB4 > SB24_2:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_2:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 2 and 0 < SB24_2 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_2:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 3 and SB4 > SB24_3:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_3:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 3 and 0 < SB24_3 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_3:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 4 and SB4 > SB24_4:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_4:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 4 and 0 < SB24_4 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_4:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 5 and SB4 > SB24_5:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_5:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 5 and 0 < SB24_5 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_5:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 6 and SB4 > SB24_6:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_6:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 6 and 0 < SB24_6 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_6:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 7 and SB4 > SB24_7:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_7:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 7 and 0 < SB24_7 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_7:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 8 and SB4 > SB24_8:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_8:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 8 and 0 < SB24_8 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_8:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 9 and SB4 > SB24_9:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_9:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 9 and 0 < SB24_9 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_9:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 10 and SB4 > SB24_10:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_10:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 10 and 0 < SB24_10 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_10:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif SB1 == 0 and SB4 > SB24_1:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24_0:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        elif SB1 == 0 and 0 < SB24_1 < 110:
            st.markdown(f"<h2 style='text-align: center;'>{SB24_0:.1f}{'%'}</h2>", unsafe_allow_html=True)
        else:
            pass
else:
    pass



st.text('')

#st.button('Stuur mij mijn persoonlijke advies')

