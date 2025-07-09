import pandas as pd
import folium
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize, to_hex

def generate_map(df, center=[30, 14], zoom=1):
    
    fmap = folium.Map(location=center, zoom_start=zoom)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color='red',
            fill=True,
            fill_opacity=0.7,
            fill_colour='red',
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap


def generate_frp_map(df, center=[30, 14], zoom=1):
    
    fmap = folium.Map(location=center, zoom_start=zoom)

    norm = Normalize(vmin=df['frp'].min(), vmax=df['frp'].max())
    colormap = cm.get_cmap('YlOrRd')

    for _, row in df.iterrows():
        color = to_hex(colormap(norm(row['frp'])))
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap



def generate_frp_map_log(df, center=[30, 14], zoom=1):
    
    fmap = folium.Map(location=center, zoom_start=zoom)

    norm = Normalize(vmin=df['frp_log'].min(), vmax=df['frp_log'].max())
    colormap = cm.get_cmap('YlOrRd')

    for _, row in df.iterrows():
        color = to_hex(colormap(norm(row['frp_log'])))
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=0.5,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"FRP: {row['frp']:.1f}"
        ).add_to(fmap)

    return fmap