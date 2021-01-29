##### UNCLASSIFIED
# Thermograph Tool

## Table of contents
1. [Description](#description)
2. [Getting Started](#getting-started)
    * [Dependencies](#dependencies)
3. [Navigation, Tests, Simulations, and Analysis](#navigation,-tests,-simulations,-and-analysis)
    * [Pages](#pages)
        * [Thermographs](#thermographs)
        * [View Data](#view-data)
        * [Access Data](#access-data)
        * [Documentation](#documentation)
4. [Features and Best Practices](#features-and-best-practices)
4. [Deployment](#Deployment)
5. [Contributing](#contributing)
6. [Next Steps](#next-steps)
7. [Authors](#authors)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Contact Us](#contact)

## Description

This web app is a proof of concept for a potential Thermograph deliverable. It also is an exploration of R shiny's capabilities with a focus on creating best practices for many facets within a Python Dash application.

**Background:** NGA is implementing a large scale effort to track the agency's progress against newly defined and rigourously tangible goals, objectives, and expected accomplishments. 

**Purpose:** This demonstration looks at how to build a dynamic thermograph style capability with R Shiny. The thermographs include a gradient color bar with a quantitative scale (0 to 1 used in this demonstration). Visualization and layout will be generated through highly dynamic algorithms based on the given data.

**Overview of Methodology:** Construct a web application via Python Dash to create impactful dashboards while maintaining dynamic adaption of the given data.

**Metric Status:** Using the plotly package in Python, the thermographs are created using a scatter plot trace as well as a contour trace for the hue background. The black triangle and blue circle represent the previous and current periods respectively. The data contained in the demo Excel file allows for the inclusion of associated data related to the metric such as related objective, the objective owner, the metric owner and changes since last reporting. Metric analysis can also be found under the Metric Analysis box, which gives insight to each metric, its description, and a further look at its progress.

**Objective Status:** Similar to the Metric Status this demonstration included an objective level that includes a weighted scoring of the objective's metrics.

**Web Application:** Creating a web application as the medium for the visualization gives the user a natural flow and feel while navigating the tool. In addition, it allows for unlimited extensibility and customization.

OSO's Data Analytic team aims to build software that allows users the ability to ingest, manipulate, and display data and graphics in a highly efficient and dynamic web application experience that breaks the mold of limited Tableau technology. Walk through this document to get started with this tool and consider its practices and methods for your own upcoming project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Note that much of the code explanation is done via comments within the project files. See 'Deployment' for notes on how to deploy the project on a live system. 

After reading through the README, see the [CONTRIBUTING.md](CONTRIBUTING.md) document under *Pull Request Process* to see how to get the web application up and running on your own machine.

### Dependencies

What things you need to install the software and how to install them
- [Python >= v3.8.2]()     
- [Visual Studio >= v1.49.1]()
- [Pip]() (*Python libraries can be found at the top of app.py. See below for explanation of libraries.*)
    * **shiny:** the base library for r shiny web applications. 
    * **shinydashboard:** allows for simply UI creation (especially for dashboard templates)
    * **shinyWidgets:** used for more dynamic user inputs
    * **shinyBS:** bootstrap functionality and formatting (e.g. bootstrap collapse)
    * **shinyalert:** creates a modal that pops up as an alert to the user
    * **plotly:** a library full of simple code dynamic visualizations
    * **collapsibleTree:** dendrogram graph
    * **networkD3:** r pulls d3's network graph 
    * **d3r:** functions for using d3 in R
    * **sunburstR:** builds a dynamic sunburst graph with helpful legends and paths
    * **igraph:** provides data types and functions for graph algorithm implementation
    * **tidyverse:** a *colection* of r packages designed for data science and data manipulation
    * **readxl:** pulls in excel data into data frame
    * **writexl:** writes data frame to excel file
    * **DT:** r copies js library DataTables (for visualizing tables)
    * **rmarkdown:** helps interpret .rmd files into many output formats
    * **markdown:** helps interpret markdown files into many output formats 
- [Thermograph Tool Code on Gitlab]() (*note for now that the ***dev*** branch will contain the most up to date feautures and ***master*** will be the latest stable build*)

### Stripped Web Application

[Here]() is an older commit that is a more stripped down version of the application. If the latest commit is too much code, you might want to pull this commit on a separate branch.

## Navigation, Tests, Simulations, and Analysis

OSO's tools are designed to have a natural flow to help navigate the user through building an analytic conclusion. The panel on the left side of the web page are responsible for navigation, selecting, controlling, filtering, and setting parameters for each the dashboard. Each tab exhibits a different asset of the web app. Below will outline each tab and its capabilities

### Pages
#### Thermographs
##### The Thermograph Dashboard is broken down into 4 parts
![thermographs](www/img/Thermographs.png)

1. Objective Selection
All data in the dashboard is filtered down to only data pertaining to the selected objective.

2. Thermographs
The top thermograph is the objective status. It is determined by the weighted sum of the metric thermographs.

3. Insight widget
Our widget in the top right features 4 distinct tabs. A description of the project and three powerful graphs.

    * **PoC Overview** - Explains the proof of concept and some of the reasoning behind why the project was created.

    * **Dendrogram** - examines the hierarchy of the goals, objectives, and metrics.

    * **Network** - indicates dependencies within metrics. (dev data)

    * **Sunburst** - visualizes a mix of hierarchy and dependencies for an additional insight to the data. (dev data)

4. Metric Analysis
Select a metric to see just how much progress has been made since the last update.

#### View Data
##### A simple table to view the underlying data
![viewdata](www/img/ViewData.png)

Explore the data in table format with search and filter capabilites.

#### Access Data
##### Add, Edit, or Import Data

This portion is unbuilt. See the R version of this application for functionality.

#### Documentation
##### Get some background on the tool in the User Guide.
![userguide](www/img/UserGuide.png)

Not including in this README.md is the user guide. This is only accessed within the application. It outlines updates, in progress tasks, data origin and structure, usage, and some notes on the project for background.

## Features and Best Practices

The following features that have been extensively researched and carefully integrated to cleverly provide a given function.

* Tabs to Links

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contributing
See the User Guide to view next steps. *If the project and the README.md has not been updated, the User Guide screenshot might provide this information*

## Authors

* **Brett Parsons** - *Founding Developer*
    - [unclassified github]()
    - [gitlab]()
    - [r space]()

See also the list of [members]() who participated in this project.

## License

There is no license yet for this project. However, when there is, one can access it here - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
- T Rex
- OSO-DA colleagues

## Contact

OSO-DA Team  |  Title  |  Email  |  Phone number
--------------  |  --------------  |  --------------  |  --------------
Robert Brett Parsons  |  Computer & Data Scientist  |  bparsons@apogeeintegration.com  |  757-773-6699
Rachel Carrig  |  Lead Data Scientist  |  rcarrig@apogeeintegration.com  |  713-504-6575
> **Note:** You can also contact Brett Parsons at his Apogee Integration Email at bparsons@apogeeintegration.com for any unclassified questions.
