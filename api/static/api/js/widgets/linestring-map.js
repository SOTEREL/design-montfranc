function LineStringMapWidget(config) {
  FeatureMapWidget(config, "LineString", {
    edit: true,
    draw: {
      circle: false,
      circlemarker: false,
      marker: false,
      polygon: false,
      polyline: {
        shapeOptions: config.featureStyle || {},
        showLength: true,
        guidelineDistance: 15,
      },
      rectangle: false,
    },
  }).init();
}
