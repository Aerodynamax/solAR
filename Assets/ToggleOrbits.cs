using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleOrbits : MonoBehaviour
{

    Toggle m_Toggle;
    public GameObject m_camera;
    LineRenderer[] childRenderers;

    void Start()
    {
        m_Toggle = GetComponent<Toggle>();
        m_Toggle.onValueChanged.AddListener(delegate {
            ToggleValueChanged(m_Toggle);
        });
    }

    void ToggleValueChanged(Toggle change)
    {
        childRenderers = m_camera.GetComponentsInChildren<LineRenderer>();
        Debug.Log(childRenderers);
        for (int i = 0; i < childRenderers.Length; i++)
        {
            LineRenderer orbit = childRenderers[i];
            if (m_Toggle.isOn)
            {
                orbit.forceRenderingOff = false;
            }
            else if(!m_Toggle.isOn)
            {
                orbit.forceRenderingOff = true;
            }
        }

      
    }
}
