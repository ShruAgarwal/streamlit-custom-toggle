import React, { useEffect, useState } from "react"
import{ ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { HeartSwitch } from "@anatoliygatt/heart-switch";


interface PythonArgs {
  label: string
  value: boolean
  active_track_fill: string
  active_thumb_color: string
}
  
const StreamlitCustomToggle = (props: ComponentProps) => {
  const { label, value, active_track_fill, active_thumb_color}: PythonArgs = props.args;
  const [checked, setChecked] = useState(false);
  useEffect(() => Streamlit.setFrameHeight());
  
    return (
      <>
      {label}

      
        <HeartSwitch
        size="md"
        inactiveTrackFillColor="#cffafe"
        inactiveTrackStrokeColor="#080015"
        activeTrackFillColor={active_track_fill}
        activeTrackStrokeColor="#0891b2"
        inactiveThumbColor="#ecfeff"
        activeThumbColor={active_thumb_color}
        checked={checked}
        onChange={(event) => {
          setChecked(event.target.checked);
        }}
        aria-disabled={value}
      /> 
      </> 
    );
};

// Make the function publicly available. If you forget this, index.tsx won't find it.
export default withStreamlitConnection(StreamlitCustomToggle);