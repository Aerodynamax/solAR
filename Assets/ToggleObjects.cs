using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ToggleComets : MonoBehaviour
{
    [SerializeField] private string Tag = "NEO";
    [SerializeField] private Toggle toggle;

    private GameObject[] comets;

    // Start is called before the first frame update
    void Start()
    {
        toggle.onValueChanged.AddListener(delegate {
            OnToggle(toggle);
        });
    }

    private void OnToggle(Toggle toggle)
    {
        GameObject[] NEOs = GameObject.FindGameObjectsWithTag(Tag);

        foreach (GameObject NEO in NEOs)
        {
            NEO.GetComponentInChildren<MeshRenderer>().enabled = toggle.isOn;
        }
        
    }
}
