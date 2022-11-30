# Streamlit Custom Toggle

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shru-examples.streamlit.app/Heart_Toggle_Switch)

A custom component to load heart-shaped Toggle Switch widget 🧡

<p align="center">
 <a href="https://pypi.org/project/streamlit-custom-toggle/0.1.1/">
  <img src="https://img.shields.io/pypi/v/streamlit-custom-toggle?color=brightgreen" />
 </a>
 <a href="https://github.com/ShruAgarwal/streamlit-custom-toggle/blob/main/LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-orange.svg" />
 </a>
 <a href="https://pypi.org/project/streamlit-custom-toggle/">
  <img src="https://img.shields.io/pypi/dm/streamlit-custom-toggle?color=pink" />
 </a>
</p>

## Demo 🕹

<p align="center">
  <img src="https://github.com/ShruAgarwal/streamlit-custom-toggle/blob/main/toggle_demo.gif"/>
</p>

## Installation ⬇

```
pip install streamlit-custom-toggle
```

## Usage 🤓

*Here's a simple example 👇*

```python
import streamlit as st
from streamlit_custom_toggle import st_custom_toggle

st.subheader('Music Choices 🎵')
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    # Disabled toggle switch
    calm = st_custom_toggle('Calm', active_track_fill="#EAE4E4", active_thumb_color="#EAE4E4", value="true", key="toggle1")

with col2:
    fun = st_custom_toggle('Fun', active_track_fill="#57FD6E", active_thumb_color="#EAE4E4", key="toggle2")

with col3:
    music_toggle = st_custom_toggle('Rock', active_track_fill="#FF5733", active_thumb_color="#900C3F", key="toggle3")
    music = st.radio(
    "Select your favorite artist",
    ('The Beatles', 'AC/DC', 'Pink Floyd', 'Elvis Presley', 'MÃ¥neskin'), disabled=music_toggle)
    st.markdown(f"You choose {music}")

# Checking the toggle state
st.code(f"Calm = {calm}, Fun = {fun}, Rock = {music_toggle}")
```

## References 🤩

- [React heart-switch](https://github.com/anatoliygatt/heart-switch)
- [Streamlit Components Tutorial by FANILO](https://streamlit-components-tutorial.netlify.app/)
- [Streamlit Component Publish Docs](https://docs.streamlit.io/library/components/publish)
