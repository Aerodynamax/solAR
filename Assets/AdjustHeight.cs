using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AdjustHeight : MonoBehaviour
{
    public GameObject Target;
    public Slider heightSlider;

    void Update()
    {
        Vector3 pos = Target.transform.position;
        pos.y = heightSlider.value;
        Target.transform.position = pos;
    }
}
