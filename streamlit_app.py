import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from allen_institute_connection.allen_institute_connection import AllenInstituteConnection
from allen_institute_connection.plot_ephys import plot_waveform_sweeps
from helper_functions.streamlit_buttons import clicked
import numpy as np
import matplotlib.pyplot as plt
from streamlit.connections import ExperimentalBaseConnection
import streamlit as st
import allensdk
from allensdk.core import cell_types_cache
from allensdk.core.cell_types_cache import CellTypesCache

st.set_page_config(
    page_title='Allen Institute Dataset Explorer',
)

"# Allen Institute Dataset Explorer"

"""
This app is a quick prototype of using st.experimental_connection
 access open source Allen Institute data from Streamlit.
"""

st.write("## Example: Electrophysiology Data")

# Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False,2:False}


connection_button = st.button("Connect to Allen Institute Cell Types Cache", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    conn = st.experimental_connection('AllenInstituteConnection', AllenInstituteConnection)
    c = conn.cursor()
    # conn = conn._connect()
    st.write(conn)

    data_set = conn.get_data(464212183)

if st.session_state.clicked[1]:
    sweep_button = st.button("Plot Waveform Sweeps", on_click=clicked, args=[2])
    if st.session_state.clicked[2]:
        fig = plot_waveform_sweeps(data_set, 30)
        st.pyplot(fig)
