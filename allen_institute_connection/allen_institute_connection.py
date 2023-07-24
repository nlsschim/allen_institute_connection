from streamlit.connections import ExperimentalBaseConnection
from pathlib import Path
import streamlit as st
import allensdk

class AllenInstituteConnection(ExperimentalBaseConnection):
    
    def _connect(self, output_dir='./', **kwargs):
        conn = None
        if 'CellTypesCache' in kwargs:
            ctc = kwargs['CellTypesCache']
            ctc = allensdk.core.cell_types_cache.CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
            conn = ctc
        else:
            conn = allensdk.core.cell_types_cache.CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
        return conn


    def _get_ephys_data(self, **kwargs):
        cell_specimen_id = 464212183
        data_set = self.get_ephys_data(cell_specimen_id)
        return data_set