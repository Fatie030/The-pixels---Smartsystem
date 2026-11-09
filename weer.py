import json

with open("weer.json", "r") as bestand:
    data = json.load(bestand)

print("=== Weergegevens ===")
print("Latitude:", data["latitude"])
print("Longitude:", data["longitude"])
print("Tijdzone:", data["timezone"])
print("Hoogte:", data["elevation"], "meter")