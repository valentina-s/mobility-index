import numpy as np
from numpy import testing as npt
import pandas as pd
from mobility_index import gpd_tools
import shapely

def test_coordinates():
    # testing ArraySum function
    d = {'place_id':[1,2,3],'lat':[47.615866, 47.618850, 47.596843],'lng':[-122.309913, -122.325005, -122.326929]}
    df = pd.DataFrame(d)
    # array2 = np.ones(100)
    assert('lat' in df.columns)
    assert('lng' in df.columns)
    res = gpd_tools.pandas2geopandas(df)
    # npt.assert_equal(res, 3*np.ones(100))
    assert(res.place_id[0] == df.place_id[0])
