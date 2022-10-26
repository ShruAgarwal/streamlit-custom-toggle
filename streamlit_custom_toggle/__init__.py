import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:  # A function that calls the frontend component when run
    _component_func = components.declare_component(
        "streamlit_custom_toggle",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_custom_toggle", path=build_dir)

# Define a public function for the package,which wraps the caller to the frontend code
def st_custom_toggle(label: str, active_track_fill: str, active_thumb_color: str, value="false", key=None):
    """Display a heart-shaped toggle switch.

    Parameters
    ----------
    label: str
        A short label explaining to the user what this toggle switch is for.
    active_track_fill: str
        To fill color of the track when the toggle switch is in an active/on state.
    active_thumb_color: str
        To fill color of the thumb when the toggle switch is in an active/on state.
    value: bool 
        Defaults the toggle switch to activated. If true, then the toggle switch is inactivated.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    bool
        An active or inactive heart-shaped toggle switch.
    """
    component_value = _component_func(label=label, active_track_fill=active_track_fill, active_thumb_color=active_thumb_color, value=value, key=key)
    return component_value
