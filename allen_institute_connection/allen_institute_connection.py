from pathlib import Path
import pandas as pd
import streamlit
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import allensdk

class AllenInstituteConnection(ExperimentalBaseConnection):
    """_summary_

    Parameters
    ----------
    ExperimentalBaseConnection : _type_
        _description_
    """
    
    def _connect(self, output_dir='./tmp', **kwargs):
        conn = allensdk.core.cell_types_cache.CellTypesCache(manifest_file=Path(output_dir) / 'manifest.json')
        return conn
    
    def cursor(self, **kwargs):
        return self._instance
    
    def get_data(self, query: int, ttl: int = 3600, **kwargs):
        @cache_data(ttl=ttl)
        def _get_data(query: int, **kwargs):
            cursor = self.cursor()
            cursor.get_ephys_data(query, **kwargs)
            return cursor.get_ephys_data(query, **kwargs)
        return _get_data(query, **kwargs)


    # def _get_ephys_data(self, **kwargs):
    #     cell_specimen_id = 464212183
    #     data_set = self.get_ephys_data(cell_specimen_id)
    #     return data_set