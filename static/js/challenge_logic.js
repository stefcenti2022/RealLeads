// Add console.log to check to see if our code is working.
console.log('working');

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY,
  }
);

// We create the second tile layer that will be the background of our map.
let satelliteStreets = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY,
  }
);

// We create the third tile layer that will be the background of our map.
let outdoors = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/tiles/{z}/{x}/{y}?access_token={accessToken}',
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY,
  }
);

// // Create the map object with center, zoom level and default layer.
let map = L.map('mapid', {
  center: [40.7, -94.5],
  zoom: 3,
  layers: [streets],
});

// Create a base layer that holds all three maps.
let baseMaps = {
  'Streets': streets,
  'Satellite': satelliteStreets,
  'Outdoors': outdoors,
};

// Add a layer group for all earthquakes that occurred in the past 7 days.
// Add a 2nd layer group for the tectonic plate data.
// Add a 3rd layer group for the major earthquake data.
// Add a 4th layer group for the orogens data.
let allEarthquakes = new L.LayerGroup();
let tectonicPlates = new L.LayerGroup();
let majorEQ = new L.LayerGroup();
let orogens = new L.LayerGroup();

// Add a reference to each layer group to the overlays object.
let overlays = {
  'Earthquakes': allEarthquakes,
  'Tectonic Plates': tectonicPlates,
  'Major Earthquakes': majorEQ,
  'Orogens': orogens,
};

// Set up data URLs
let allEarthquakesUrl =
  'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
let majorEQUrl =
  'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson';
let tectonicPlateUrl =
  'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json';
let orogensUrl =
  'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_orogens.json';

// Then we add a control to the map that will allow the user to change which
// layers are visible.
L.control.layers(baseMaps, overlays).addTo(map);

//********************************************
// SET UP ALL EARTHQUAKES LAYER
//********************************************
// Retrieve the earthquake GeoJSON data.
d3.json(allEarthquakesUrl).then(function (data) {
  // This function returns the style data for each of the earthquakes we plot on
  // the map. We pass the magnitude of the earthquake into two separate functions
  // to calculate the color and radius.
  function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.mag),
      color: '#000000',
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5,
    };
  }

  // This function determintes the color of the circle based on the magnitude
  // of the earthquake.
  function getColor(magnitude) {
    return magnitude > 5
      ? '#ea2c2c' // 5+
      : magnitude > 4
      ? '#ea822c'
      : magnitude > 3
      ? '#ee9c00'
      : magnitude > 2
      ? '#eecc00'
      : magnitude > 1
      ? '#d4ee00'
      : '#98ee00';
  }

  // This function determines the radius of the earthquake marker based on its magnitude.
  // Earthquakes with a magnitude of 0 will be plotted with a radius of 1.
  function getRadius(magnitude) {
    return magnitude === 0 ? 1 : magnitude * 4;
  }

  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We turn each feature into a circleMarker on the map.
    pointToLayer: function (feature, latlng) {
      console.log(data);
      return L.circleMarker(latlng);
    },
    // We set the style for each circleMarker using our styleInfo function.
    style: styleInfo,
    // We create a popup for each circleMarker to display the magnitude and location of the earthquake
    //  after the marker has been created and styled.
    onEachFeature: function (feature, layer) {
      layer.bindPopup(
        'Magnitude: ' +
          feature.properties.mag +
          '<br>Location: ' +
          feature.properties.place +
          '<br>Time: ' +
          new Date(feature.properties.time)
      );
    },
  }).addTo(allEarthquakes);
});

//********************************************
// SET UP MAJOR EARTHQUAKES LAYER
//********************************************
// Retrieve the major earthquake GeoJSON data >4.5 mag for the week.
d3.json(majorEQUrl).then(function (data) {
  // Use the same style as the earthquake data.
  // This function returns the style data for each of the earthquakes we plot on
  // the map. We pass the magnitude of the earthquake into two separate functions
  // to calculate the color and radius.
  function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.mag),
      color: '#000000',
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5,
    };
  }

  // Color function that uses three colors for the major earthquakes based on the magnitude of the earthquake.
  function getColor(magnitude) {
    return magnitude > 6 ? '#6e0a0a' : magnitude > 5 ? '#ea2c2c' : '#ea822c';
  }

  // This function determines the radius of the earthquake marker based on its magnitude.
  // Earthquakes with a magnitude of 0 will be plotted with a radius of 1.
  function getRadius(magnitude) {
    return magnitude === 0 ? 1 : magnitude * 4;
  }

  // Creating a GeoJSON layer with the retrieved data that adds a circle to the map
  // sets the style of the circle, and displays the magnitude and location of the earthquake
  // after the marker has been created and styled.
  L.geoJson(data, {
    // We turn each feature into a circleMarker on the map.
    pointToLayer: function (feature, latlng) {
      console.log(data);
      return L.circleMarker(latlng);
    },
    // We set the style for each circleMarker using our styleInfo function.
    style: styleInfo,
    // We create a popup for each circleMarker to display the magnitude and location of the earthquake
    //  after the marker has been created and styled.
    onEachFeature: function (feature, layer) {
      layer.bindPopup(
        'Magnitude: ' +
          feature.properties.mag +
          '<br>Location: ' +
          feature.properties.place +
          '<br>Time: ' +
          new Date(feature.properties.time)
      );
    },
  }).addTo(majorEQ);
});

//********************************************
//  SET UP TECTONIC PLATES LAYER
//********************************************
// Use d3.json to make a call to get our Tectonic Plate geoJSON data.
d3.json(tectonicPlateUrl).then(function (data) {
  // This function returns the style data for each of the tectonic plates we plot on
  // the map.
  function styleInfo(feature) {
    return {
      color: 'darkblue',
      weight: 0.5,
    };
  }

  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We set the style for each tectonic play using our styleInfo function.
    style: styleInfo,
  }).addTo(tectonicPlates);
});

//********************************************
//  SET UP OROGENS LAYER
//********************************************
// Use d3.json to make a call to get our Tectonic Plate geoJSON data.
d3.json(orogensUrl).then(function (data) {
  // This function returns the style data for each of the tectonic plates we plot on
  // the map.
  function styleInfo(feature) {
    return {
      color: 'darkblue',
      weight: 0.5,
    };
  }

  // Creating a GeoJSON layer with the retrieved data.
  L.geoJson(data, {
    // We set the style for each tectonic play using our styleInfo function.
    style: styleInfo,
  }).addTo(orogens);

  console.log(data);
});

//********************************************
//  SET UP LEGEND
//********************************************
// Create a legend control object.
let legend = L.control({
  position: 'bottomright',
});

// Use an anonymous function to return a div containing html to hold the legend.
// This function will called when the legend is added to the map.
legend.onAdd = function () {
  let div = L.DomUtil.create('div', 'info legend');

  const magnitudes = [0, 1, 2, 3, 4, 5];
  const colors = [
    '#98ee00',
    '#d4ee00',
    '#eecc00',
    '#ee9c00',
    '#ea822c',
    '#ea2c2c',
  ];

  // Looping through our intervals to generate a label with a colored square for each interval.
  for (var i = 0; i < magnitudes.length; i++) {
    console.log(colors[i]);
    div.innerHTML +=
      "<i style='background: " +
      colors[i] +
      "'></i> " +
      magnitudes[i] +
      (magnitudes[i + 1] ? '&ndash;' + magnitudes[i + 1] + '<br>' : '+');
  }
  return div;
};

// Add each layer to the map.
tectonicPlates.addTo(map);
orogens.addTo(map);
allEarthquakes.addTo(map);
majorEQ.addTo(map);

// Add a legend to the map.
legend.addTo(map);
