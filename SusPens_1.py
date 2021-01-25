#Necessary packages
import streamlit as st
import pandas as pd

#Some information concerning the three "Pijler Pensioenen":
#  Eerste Pijler Pensioen: Basic pension provided by the Dutch government to all Dutch citizens who have reached their retirement age
#  Tweede  Pijler Pensioen: Additional pension build up partly by employer and party by the individual him/herself during their working-life
#  Derde Pijler Pensioen: Extra pension build up by the individual (e.g. savings, stocks)

#Variables
#  SB1       = Lumpsum percentage
#  SB2       = "Derde Pijler Pensioen"
#  SB3       = Years to enjoy "Derde Pijler Pensioen"
#  SB4       = Percentage of last net salary needed as pension
#  SB5       = Life expectancy
#  SB10      = "Tweede Pijler Pensioen"
#  SB100     = Net Pension per Month
#  SB11      = Final net salary
#  SB12      = "Eerste Pijler Pensioen" / AOW
#  SB13/23   = Actual Pension
#  SB14/24   = Actual Percentage
#  SBLink    = external links


#Free background image from pexels.com
page_bg_img = '''
<style>
body {
background-image: url("https://images.pexels.com/photos/3389613/pexels-photo-3389613.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Set header and subheader
st.markdown("<h1 style='text-align: center;'>LumpSum Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Door de stappen in het linker menu te volgen kunt u zien hoe de Drie Pijlers van uw pensioen en het gebruik van de LumpSum van invloed zijn op uw pensioen.</h2>", unsafe_allow_html=True)

#White line
st.write("#")

#Current AOW as indicated by the SVB ("Eerste Pijler Pensioen")
SB12 = 970

#Life expectancy in months (= 23.5 years)
SB5 = 282

#User input: Current or final net salary
st.sidebar.write('Stap 1')
SB11 = st.sidebar.number_input("Uw huidige of laatst genoten netto salaris in EUR", min_value=1280, max_value=12500)

#White line
st.sidebar.write("#")

#User input: Expected Net Pension per Month in EUR - per month + warning
st.sidebar.write('Stap 2')
SB100 = st.sidebar.number_input("Verwachte netto pensioen per maand in EUR", min_value=1, max_value=2500000)

#External link to "https://www.mijnpensioenoverzicht.nl" which provides Dutch citizens with an overview of their pensioen after logging-in with their DigiD (Digital ID)
SBLink1 = '[mijnpensioenoverzicht.nl](https://www.mijnpensioenoverzicht.nl)'
st.sidebar.markdown(f"Op {SBLink1} vindt u hoeveel netto pensioen per maand u ontvangt via uw pensioenuitvoerders en AOW. U kunt dit bedrag hier invullen.", unsafe_allow_html=True)


SB10 = SB100 - SB12

#White line
st.sidebar.write("#")

#User input: Expected "Derde Pijler Pensioen" in EUR - total + the number of years the person wants to make use of this amount
st.sidebar.write('Stap 3')
SB2 = st.sidebar.number_input("Verwachte Derde Pijler Pensioen in EUR - totaal", min_value=0, max_value=2500000, step=1000)
if SB2 > 0:
    # Hoeveel jaar wilt u van uw opgebouwde Derde Pijler Pensioen genieten?
    SB3 = st.sidebar.number_input("Hoeveel jaar wilt u van uw opgebouwde Derde Pijler Pensioen genieten?", min_value=1, max_value=35)
else:
    SB3 = 1

#White line
st.sidebar.write("#")

#User input: Expected pension needed + external link to a calculator provided by Nibud to determine what one might need + warning
st.sidebar.write('Stap 4')
SBLink2 = '[Nibud](https://pensioenschijf.nibud.nl/#/panel/0)'
st.sidebar.markdown(f'Hoeveel procent van uw laatst genoten netto salaris verwacht u tijdens uw pensioen nodig te hebben om in uw levensonderhoud te kunnen blijven voorzien? Het {SBLink2} biedt een tool waar u precies kunt uitrekenen hoeveel u straks nodig heeft.', unsafe_allow_html=True)
SB4 = st.sidebar.slider('', min_value=40, max_value=140, value=60)

if SB4 < 60:
     st.sidebar.warning('Het Nibud geeft als richtlijn 60% van uw laatst genoten netto inkomen aan te houden.')
else:
    pass

#White line
st.sidebar.write("#")

#User input: Percentage of lumpsum a person might want to withdraw from his/her pension
st.sidebar.write('Stap 5')
st.sidebar.write('Door onderstaande slider te gebruiken kunt u zien hoe het opnemen van een Lumpsum effect heeft op uw pensioen.')
st.sidebar.markdown("<h1 style='text-align: center;'>Lumpsum Percentage </h1>", unsafe_allow_html=True)
SB1 = st.sidebar.slider("", min_value=0, max_value=10)

#White line
st.sidebar.write("#")
st.sidebar.write("#")

#First two columns showing Lumpsum percentage and Lumpsum in EUR
info_2, info_3 = st.beta_columns(2)
with info_2:
    st.markdown("<h1 style='text-align: center;'>Lumpsum %</h1>", unsafe_allow_html=True)
    if SB1 == 0:
        st.markdown("<h2 style='text-align: center;'>Geen</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center;'> {str(SB1) + '%'} </h2>", unsafe_allow_html=True)
with info_3:
    st.markdown("<h1 style='text-align: center;'>In (Bruto) Euro</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'> {'€ '}{(SB10*SB5)*SB1/100:.2f} </h2>", unsafe_allow_html=True)

########################################################################################################################
#First part which shows salary, pension and percentage - including "Derde Pijler Pensioen"

#White line
st.write("#")

#Difference between no lumpsum and the different percentages + Pension (up to 10%)
if SB1 == 1:
    SB13 = SB12 + (SB10*0.99) + (SB2/(SB3*12))
elif SB1 == 2:
    SB13 = SB12 + (SB10*0.98) + (SB2/(SB3*12))
elif SB1 == 3:
    SB13 = SB12 + (SB10*0.97) + (SB2/(SB3*12))
elif SB1 == 4:
    SB13 = SB12 + (SB10*0.96) + (SB2/(SB3*12))
elif SB1 == 5:
    SB13 = SB12 + (SB10*0.95) + (SB2/(SB3*12))
elif SB1 == 6:
    SB13 = SB12 + (SB10*0.94) + (SB2/(SB3*12))
elif SB1 == 7:
    SB13 = SB12 + (SB10*0.93) + (SB2/(SB3*12))
elif SB1 == 8:
    SB13 = SB12 + (SB10*0.92) + (SB2/(SB3*12))
elif SB1 == 9:
    SB13 = SB12 + (SB10*0.91) + (SB2/(SB3*12))
elif SB1 == 10:
    SB13 = SB12 + (SB10*0.90) + (SB2/(SB3*12))
else:
    SB13 = SB12 + SB10 + (SB2/(SB3*12))

SB14 = float(SB13 / SB11 * 100)

#Extra row to divide between pension inclusing and excluding "Derde Pijler Pensioen"
if SB2 > 0:
    st.subheader("Pensioen eerste " + str(SB3) + " jaren inclusief 3e pijler")
else:
    pass

info_1, graph_012, graph_013 = st.beta_columns(3)
with info_1:
    st.markdown("<h1 style='text-align: center;'>Salaris</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'> {'€ ' + str(SB11) +'.-'} </h2>", unsafe_allow_html=True)
with graph_012:
    st.markdown("<h1 style='text-align: center;'>Pensioen</h1>", unsafe_allow_html=True)
    if SB13 > 950:
       st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB13:.2f}</h2>", unsafe_allow_html=True)
    else:
        pass
with graph_013:
    st.markdown("<h1 style='text-align: center;'>Percentage</h1>", unsafe_allow_html=True)
    if SB4 < SB14 and 40 < SB14 < 150:
        st.markdown(f"<h2 style='text-align: center;'>{SB14:.1f}{'%'}</h2>", unsafe_allow_html=True)
    elif 40 < SB14 < 150:
        st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB14:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
    else:
        pass


########################################################################################################################
#Second part which shows salary, pension and percentage - excluding "Derde Pijler Pensioen"

#White line
st.write("#")

#Difference between no lumpsum and the different percentages + Pension (up to 10%)
if SB1 == 1:
    SB23 = SB12 + (SB10*0.99)
elif SB1 == 2:
    SB23 = SB12 + (SB10*0.98)
elif SB1 == 3:
    SB23 = SB12 + (SB10*0.97)
elif SB1 == 4:
    SB23 = SB12 + (SB10*0.96)
elif SB1 == 5:
    SB23 = SB12 + (SB10*0.95)
elif SB1 == 6:
    SB23 = SB12 + (SB10*0.94)
elif SB1 == 7:
    SB23 = SB12 + (SB10*0.93)
elif SB1 == 8:
    SB23 = SB12 + (SB10*0.92)
elif SB1 == 9:
    SB23 = SB12 + (SB10*0.91)
elif SB1 == 10:
    SB23 = SB12 + (SB10*0.90)
else:
    SB23 = SB12 + SB10

SB24 = float(SB23 / SB11 * 100)


if SB2 > 0:
    st.subheader("Pensioen na " + str(SB3) + " jaar exclusief 3e pijler")
    info_1, graph_014, graph_015 = st.beta_columns(3)
    with info_1:
        st.markdown("<h1 style='text-align: center;'>Salaris</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'> {'€ ' + str(SB11) + '.-'} </h2>", unsafe_allow_html=True)
    with graph_014:
        st.markdown("<h1 style='text-align: center;'>Pensioen</h1>", unsafe_allow_html=True)
        if SB23 > 950:
            st.markdown(f"<h2 style='text-align: center;'>{'€ '}{SB23:.2f}</h2>", unsafe_allow_html=True)
        else:
            pass
    with graph_015:
        st.markdown("<h1 style='text-align: center;'>Percentage</h1>", unsafe_allow_html=True)
        if SB4 < SB24 and 40 < SB24 < 150:
            st.markdown(f"<h2 style='text-align: center;'>{SB24:.1f}{'%'}</h2>", unsafe_allow_html=True)
        elif 40 < SB24 < 150:
            st.markdown(f"<h2 style='text-align: center;'><font color=#FF0000><b> {SB24:.1f}{'%'} </font> </h2>", unsafe_allow_html=True)
        else:
            pass
else:
    pass
