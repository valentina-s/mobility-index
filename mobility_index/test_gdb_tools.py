def test_conversion():
    # test the first coordinate of the conversion
    d = {'place_id':[1,2,3],'lat':[47.615866, 47.618850, 47.596843],'lng':[-122.309913, -122.325005, -122.326929]}
    df = pd.DataFrame(d)
    res = gpd_tools.pandas2geopandas(df)
    assert(res.place_id[0] == df.place_id[0])
