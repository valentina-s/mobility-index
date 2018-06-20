def pandas2geopandas(df):
    geometries = [shapely.geometry.Point(xy) for xy in zip(df.lng, df.lat)]
    crs = {'init': 'epsg:4326'}
    gf = gpd.GeoDataFrame(df, crs=crs, geometry=geometries)
    return(gf)

def convex_hull_shape(gf):
    point_collection = shapely.geometry.MultiPoint(gf.geometry.tolist())
    polygon = point_collection.convex_hull
    gfShape = gpd.GeoDataFrame(geometry=[polygon], crs = {'init': 'epsg:4326'})
    return(gfShape)
