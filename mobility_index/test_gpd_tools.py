import numpy as np
from numpy import testing as npt
import pandas as pd
from mobility_index import gpd_tools
import shapely

def test_conversion():
    # test if the output of the conversion is geopandas dataframe
    d = {'place_id':[1,2,3],'lat':[47.615866, 47.618850, 47.596843],'lng':[-122.309913, -122.325005, -122.326929]}
    # conversion
    d = pd.DataFrame(d)
    res = pandas2geopandas(d)
    assert(isinstance(res, gpd.geodataframe.GeoDataFrame))
