import folium
import openrouteservice as ors
from openrouteservice.exceptions import ApiError


def get_route(client, coordinates):
    """
    Request an optimized route from ORS.

    Args:
        client: OpenRouteService client
        coordinates: List of [lon, lat] coordinates

    Returns:
        GeoJSON route object
    """
    try:
        return client.directions(coordinates, profile='driving-car', format='geojson')
    except ApiError as e:
        print(f"OpenRouteService API error: {e}")
        return None


def create_map(route, coordinates, output_file="map.html"):
    """
    Create and save a folium map with the route and markers.

    Args:
        route: GeoJSON route object from ORS
        coordinates: List of [lon, lat] coordinates
        output_file: File name to save the map to
    """
    # Center the map on the first location
    map_center = list(reversed(coordinates[0]))
    m = folium.Map(location=map_center, zoom_start=14, tiles="cartodbpositron")

    # Add the route to the map
    folium.GeoJson(route, name="Route").add_to(m)

    # Add markers for each stop
    for i, coord in enumerate(coordinates):
        folium.Marker(
            location=list(reversed(coord)),
            popup=f"Stop {i+1}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    # Save to file
    m.save(output_file)
    print(f"✅ Map has been saved to '{output_file}'")


def main():
    # Replace with your OpenRouteService API key
    ORS_API_KEY = "your-api-key-here"

    # Coordinates in [longitude, latitude] format
    coordinates = [
        [-87.7898356, 41.8879452],
        [-87.7808524, 41.8906422],
        [-87.7895149, 41.8933762],
        [-87.7552925, 41.8809087],
        [-87.7728134, 41.8804058],
        [-87.7702890, 41.8802231],
        [-87.7787924, 41.8944518],
        [-87.7732345, 41.8770663],
    ]

    # Initialize ORS client
    try:
        client = ors.Client(key=ORS_API_KEY)
    except Exception as e:
        print(f"Error initializing OpenRouteService client: {e}")
        return

    # Get optimized route
    route = get_route(client, coordinates)
    if route:
        create_map(route, coordinates)
    else:
        print("⚠️ Failed to retrieve route.")


if __name__ == "__main__":
    main()
