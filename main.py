import folium
import geopandas as gpd
from IPython.display import display
from h3 import h3
from shapely.geometry import Polygon
import os
import webbrowser
filepath = '/home/julio/Escritorio/python'

gangnam = [37.508811, 127.040978]
hongdae = [37.557435, 126.925808]

gangnam_h3 = h3.geo_to_h3(gangnam[0], gangnam[1], 5)
loc = h3.h3_to_geo(gangnam_h3)


def to_polygon(l):
    return Polygon(h3.h3_to_geo_boundary(l, geo_json=True))


df = gpd.GeoDataFrame({'h3': [gangnam_h3]})
df['geometry'] = df['h3'].apply(to_polygon)
df.crs = 'epsg:4269'
print(df['geometry'])
