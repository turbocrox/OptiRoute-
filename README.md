# OptiRoute - Vehicle Routing and Visualization

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**OptiRoute** is a Python-based tool for visualizing optimized vehicle routes using **OpenRouteService (ORS)** and **Folium**. It solves a simplified Vehicle Routing Problem (VRP) by computing the best route across a series of coordinates and displaying the result on an interactive map.

## 🚀 Features

- Route optimization via OpenRouteService
- Interactive map generation using Folium
- Easy-to-edit coordinates for custom scenarios
- Output as an HTML file you can open in any browser

## 📁 Project Structure
















🔧 Instructions to Run

    Install dependencies:
```bash
pip install folium openrouteservice
```

Replace the line:
```bash
ORS_API_KEY = "your-api-key-here"

with your actual API key from https://openrouteservice.org/sign-up/
```

Run the script:
```bash

python main.py
```

Open map.html in a browser to view your route!
