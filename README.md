# Electric Vehicle Population in the USA: Data Visualization Application

This project involves the creation of a data visualization application that displays statistics about the population of electric vehicles (EVs) in the USA by state. The application processes and visualizes large datasets using various Python libraries and frameworks, including interactive maps and custom graphical elements.

## Data Source

The data used in this project was obtained from the open data repository of the U.S. government. It consists of over 60,000 records on electric vehicle populations. For the purposes of this project, we extracted and processed the following attributes:
- **Brand** (`brand`)
- **Model** (`model`)
- **Year of Production** (`year of production`)
- **Type of Electric Vehicle** (`type`)
- **Range** (`range`)

Data Source Links:
- [Electric Vehicle Population Data](https://catalog.data.gov/dataset/electric-vehicle-population-data)
- [Processed CSV File](https://gist.githubusercontent.com/AlbertKozera/6396b4333d1a9222193e11401069ed9a/raw/dca34e16091ba533a53bc447edad12ddb041af2d/Pojazdy%2520elektryczne%2520w%2520USA.csv)

## Technology Stack

- **Programming Languages**: Python 3.8, HTML5
- **Tools and Environments**:
  - Anaconda
  - Spyder
  - Visual Studio Code
  - Ron’s Editor
  - CSVed
- **Libraries**:
  - **pandas**: Facilitates data manipulation and analysis in Python.
  - **plotly.py**: Interactive graphing library for Python, used for creating SVG-based charts and maps.
  - **Dash**: A Python framework for building web applications with data visualization components.

## Key Features

- **Interactive Map**: Utilizes the Plotly Choropleth component to create a color-coded map of the USA. The color intensity of each state is based on the average range of electric vehicles.
- **Statistical Calculations**: Computes statistics such as mean, variance, and standard deviation for attributes like vehicle range, year of production, and type.
- **Chernoff Cars**: Custom graphical elements are generated to represent data attributes visually, such as the size of the car's trunk reflecting the vehicle's age or the wheel size based on the vehicle's range.
- **Hover Interactions**: Displays detailed statistics for each state when the user hovers over it on the map.
- **Dynamic Updates**: Uses Dash callbacks to update visual elements dynamically based on user interaction.

## Application Overview

The application runs on a local server using Dash, with a default port of 8050. The map is rendered in a web browser, and the Plotly components are converted to HTML5.

- **User Interactivity**: Achieved through the use of Dash's `@app.callback` decorators, which allow for dynamic communication between the user and the server using classes `Input` and `Output`.
- **Chernoff Cars**: Generated using custom Python functions that dynamically create and modify images based on data attributes. Different attributes like brand, model, and vehicle type influence the visual representation of the cars.

![image](https://github.com/user-attachments/assets/c4477fc6-42a1-4e15-ae27-1eb2d82e77fc)

![image](https://github.com/user-attachments/assets/d54d5906-47a6-49b3-ae1a-f59b927a69c9)


## Conclusion

Python, with its rich ecosystem of libraries and frameworks, proved to be a great choice for data analysis and visualization. The use of Plotly and Dash made creating interactive visual elements intuitive and straightforward. The "Chernoff cars" provide an innovative way to present data visually, and there is potential for expanding this approach to other types of data in the future.
