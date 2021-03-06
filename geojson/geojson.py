import json
from h3 import h3
import geopandas as gpd
import pandas as pd
from pandas.io.json import json_normalize

rio = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "shape": "Line",
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-78.666387, -1.635368],
                [-78.661065, -1.643089],
                [-78.656601, -1.645491],
                [-78.65145, -1.647379],
                [-78.644239, -1.644462],
                [-78.633766, -1.645663],
                [-78.631877, -1.651669],
                [-78.627928, -1.659733],
                [-78.624838, -1.665396],
                [-78.628958, -1.668999],
                [-78.624666, -1.675348],
                [-78.623121, -1.684442],
                [-78.624666, -1.691992],
                [-78.631019, -1.697654],
                [-78.637028, -1.695938],
                [-78.640977, -1.700571],
                [-78.650592, -1.701086],
                [-78.651107, -1.693708],
                [-78.650077, -1.690104],
                [-78.656429, -1.685815],
                [-78.662953, -1.686158],
                [-78.669306, -1.688903],
                [-78.671195, -1.69508],
                [-78.678062, -1.69611],
                [-78.682698, -1.688389],
                [-78.679436, -1.682383],
                [-78.676689, -1.681868],
                [-78.671881, -1.683927],
                [-78.668619, -1.681182],
                [-78.667933, -1.675691],
                [-78.672568, -1.669342],
                [-78.687334, -1.666425],
                [-78.69506, -1.663337],
                [-78.698494, -1.662479],
                [-78.703988, -1.66042],
                [-78.713431, -1.653899],
                [-78.710684, -1.649266],
                [-78.706735, -1.64],
                [-78.699696, -1.642918],
                [-78.696948, -1.640858],
                [-78.691111, -1.638285],
                [-78.695403, -1.62696],
                [-78.688707, -1.621983],
                [-78.682183, -1.618037],
                [-78.678234, -1.625244],
                [-78.673255, -1.627474],
                [-78.667074, -1.628332],
                [-78.666387, -1.635368]
            ]
        },
        "id": "95033b6d-6691-4c22-aeb0-60d70728b415"
    }]
}

df = gpd.read_file('provincias.geojson')
dfc = df[df['dpa_despro'] == 'PASTAZA']


def read_geojson_points(filepath):
    with open(filepath) as f:
        return json.load(f)


df.drop(['objectid', 'first_firs',  'shape_leng', 'shape_area'], axis='columns', inplace=True)
stops_geodata = read_geojson_points('provincias.geojson')
df = pd.DataFrame(pd.json_normalize(stops_geodata['features']))
dfp = df[df['properties.dpa_despro'] == 'PASTAZA']
#print(dfp.columns)

for points in dfp['geometry.coordinates']:
    print(points[0][0])


multipolygon = dfc['geometry']

geoJson = multipolygon.__geo_interface__

points = multipolygon.__geo_interface__['features'][0]['geometry']['coordinates']

#print(multipolygon.__geo_interface__)

