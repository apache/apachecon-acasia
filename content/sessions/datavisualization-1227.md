---
title: "Introducing advanced drill-down functionality in Apache Superset using Apache ECharts"
date: "" 
track: "datavisualization"
presenters: "Ville Brofeldt"
stype: "English Session"
---
Currently Apache Superset features dashboard native filters, which make it possible to add interactive filters to dashboards that control what data is being shown on charts. However, until now, only select chart types have offered cross filtering functionality for emitting filters to other charts, limiting limiting user interaction mostly to native filters.

Currently the project is working on introducing a rich set of interactive features to the main visualization types, making it possible to use charts to drill down (e.g. clicking on a country to expose the distribution of cities), drill through (drill into any dimension in the dataset, irrespective of hierarchies), drill through (show row level data on the fly) and drill to dashboard (open a new dashboard with the selected dimensions pre-populated as native filters). This means that users will be able to interact with charts instead of being limited to the current set of native filter types.

In the talk we'll be exploring the details of the feature, new context menus, hooks for extending the functionality and using the feature when building custom visualization plugins and timelines. We'll also show how the feature integrates with Apache ECharts (the main visualization library used by Superset), and plans for future development.
 ### Speakers: 
 <img src="images/speaker/1227.png" width="200" /><br>Ville Brofeldt: Apple, Software Engineer, Ville Brofeldt is a long standing committer and PMC member of the Apache Superset project, with extensive experience in data visualization, data engineering and predictive analytics.

 