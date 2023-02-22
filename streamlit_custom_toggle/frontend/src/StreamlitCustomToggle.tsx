import React, { useEffect, useState } from "react"
import{ ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { HeartSwitch } from "@anatoliygatt/heart-switch";


interface PythonArgs {
  label: string
  default_value: boolean
  value: boolean
  active_track_fill: string
  active_thumb_color: string
}
  
const StreamlitCustomToggle = (props: ComponentProps) => {
  const { label, default_value, value, active_track_fill, active_thumb_color}: PythonArgs = props.args;
  useEffect(() => Streamlit.setFrameHeight());

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, [event.target.name]: event.target.checked });
    Streamlit.setComponentValue(!event.target.checked );
  };
  const [state, setState] = React.useState({
      checkStatus: default_value
  });
  
  
    return (
      <>
      {label}
      
      
        <HeartSwitch
        size="md"
        disabled={value}
        inactiveTrackFillColor="#cffafe"
        inactiveTrackStrokeColor="#080015"
        activeTrackFillColor={active_track_fill}
        activeTrackStrokeColor="#0891b2"
        inactiveThumbColor="#ecfeff"
        activeThumbColor={active_thumb_color}
        checked={state.checkStatus}
        onChange={handleChange}
        name="checkStatus"
      /> 
      </> 
    );
}

// The function publicly available.
export default withStreamlitConnection(StreamlitCustomToggle);
