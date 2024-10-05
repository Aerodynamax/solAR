import csv
import json

counter = 0

new_data = {
    "OrbitsData": []
}

with open("sbdb_query_results_comets_only.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for item in reader:
        # convert everything
        new_item: dict = {
            "BodyName": item["full_name"],
            "AttractorName": "Solar system barycenter",
            "AttractorMass": 1.9884999721201209e30,                                                     # unsure
            "EC": float(item["e"]),
            "IN": float(item["i"]),
            "OM": float(item["om"]),
            "W": float(item["w"]),
            "MA": float(item["ma"]),
            "A": float(item["a"]),
            "Diameter": float(item["diameter"]) if item["diameter"] != "" else 1.0,                                                                            # unsure
            "NEO": True,
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

    for planet in planets_data["OrbitsData"]:
        planet["NEO"] = False

        RingInclination = 0.0
        if planet["BodyName"] == "Saturn":
            RingInclination = 26.7
        elif planet["BodyName"] == "Uranus":
            RingInclination = 97.77
        planet["RingInclination"] = RingInclination

planets_data["OrbitsData"] += new_data["OrbitsData"]

# save new data
with open("./formatted_near_earth_comets_csv.json", "w+") as f:
    f.write( json.dumps(planets_data, indent=4) )