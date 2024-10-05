import json

# load original data
with open("./near_earth_comets.json", "r+") as f:
    data = json.loads( f.read() )


new_data = {
    "OrbitsData": []
}

for item in data:
    # convert everything
    new_item: dict = {
        "BodyName": item["object_name"],
        "AttractorName": "Solar system barycenter",
        "AttractorMass": 1.9884999721201209e30,                                                     # unsure
        "EC": float(item["e"]),
        "IN": float(item["i_deg"]),
        "OM": float(item["node_deg"]),
        "W": float(item["w_deg"]),
        "MA": 360 * ( ( float(item["epoch_tdb"]) - float(item["tp_tdb"]) ) / float(item["p_yr"]) ), # https://astronomy.stackexchange.com/a/53495
        # "A": ( float(item["q_au_1"]) + float(item["q_au_2"]) ) / 2,                                 # https://astronomy.stackexchange.com/a/38410
        "A": pow( float(item["p_yr"]), 2.0/3.0 ),
        "Diameter": 0.1,                                                                            # unsure
        "RangeMlt": 1.0,
        "Color": {
            "r": 1.0,
            "g": 1.0,
            "b": 1.0,
            "a": 1.0
        }
    }
    # add to new list
    new_data["OrbitsData"].append(new_item)

# load planets data
with open("./JsonTable.json", "r+") as f:
    planets_data = json.loads( f.read() )

planets_data["OrbitsData"] += new_data["OrbitsData"]

# save new data
with open("./formatted_near_earth_comets.json", "w+") as f:
    f.write( json.dumps(planets_data, indent=4) )