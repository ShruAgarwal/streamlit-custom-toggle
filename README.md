

A custom component to load heart-shaped Toggle Switch 🧡

<p align="center">
 <a href="https://pypi.org/project/streamlit-custom-toggle/0.1.1/">
  <img src="https://img.shields.io/pypi/v/streamlit-custom-toggle?color=brightgreen" />
 </a>
 <a href="https://github.com/ShruAgarwal/streamlit-custom-toggle/">
  <img src="https://img.shields.io/github/last-commit/ShruAgarwal/streamlit-custom-toggle?style=flat&logo=git&color=purple" />
 </a>
 <a href="https://github.com/ShruAgarwal/streamlit-custom-toggle/blob/main/LICENSE">
  <img src="https://img.shields.io/badge/License-MIT-orange.svg" />
 </a>
 <a href="https://github.com/ShruAgarwal/streamlit-custom-toggle/">
  <img src="https://img.shields.io/github/languages/code-size/ShruAgarwal/streamlit-custom-toggle?logo=github&style=flat" />
 </a>
 <a href="https://pypi.org/project/streamlit-custom-toggle/">
  <img src="https://img.shields.io/pypi/dm/streamlit-custom-toggle?color=pink" />
 </a>
</p>

## Demo 🕹
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://shru-examples.streamlit.app/Heart_Toggle_Switch)


<p align="center">
  <img src="https://github.com/ShruAgarwal/streamlit-custom-toggle/blob/main/toggle_demo.gif"/>
</p>

## Installation ⬇

First `pip install streamlit`. Don't know how? 👉 [Check here!](https://30days.streamlit.app/?challenge=Day+1)

After that, install this component:

```
pip install streamlit-custom-toggle
```

## How to Use? 🤓

*Here's an example code 👇*

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

## Arguments Config ⚙
It supports the following arguments customization:

| Args                          | Type   | Required | Description                                                                                              |
| ----------------------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------- |
| label                         | string |   YES    | Define the toggle with a short label value
| active_track_fill             | string |   YES    | Changes the color of the track when the toggle is in the active/on state. Default value is: `#ff708f`
| active_thumb_color            | string |   YES    | Changes the color of the thumb when the toggle is in the active/on state. Default value is: `#ffffff`
| value                         | bool   | OPTIONAL | If it's value is set to `true`, then the toggle switch is deactivated. **The toggle is activated by default**
| key                           | string |   YES    | An optional key value that uniquely identifies this component.

## Tech Stack 🧰
<p align="left">
 <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="50" />
 <img src="https://img.icons8.com/plasticine/256/react.png" width="50" alt="React" />
 <img src="https://img.icons8.com/color/256/python.png" width="50" />
 <img src="https://img.icons8.com/color/256/typescript.png" width="50" />
 <img src="https://img.icons8.com/color/256/nodejs.png" width="50" />
 <img src="https://files.anaconda.com/production/resources/open-source/conda-artboard.svg" width="80" />
</p>

## License 📝
This software is open source, licensed under the [MIT License.](https://github.com/ShruAgarwal/streamlit-custom-toggle/blob/main/LICENSE)

## Helpful References 🤩

- [React heart-switch](https://github.com/anatoliygatt/heart-switch)
- [Streamlit Components Tutorial by FANILO](https://streamlit-components-tutorial.netlify.app/)
- [Streamlit Component Publish Docs](https://docs.streamlit.io/library/components/publish)
