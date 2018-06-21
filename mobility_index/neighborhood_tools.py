def places_per_neighborhood(gfN, gf, neighborhood):
    gfNeighborhood = gfN.query('nhood == @neighborhood')
    nhood_places = gpd.sjoin(gf, gfNeighborhood, how="inner", op='within')
    return(nhood_places)
