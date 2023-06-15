RMI Feature Extraction Algorithm

This repository contains an algorithm specifically developed for the extraction of crucial features from Richtmyer-Meshkov Instabilities (RMIs). The algorithm is designed to analyze RMI data and extract four key characteristics: amplitude, span, stream, and neck.

About Richtmyer-Meshkov Instabilities (RMIs)

Richtmyer-Meshkov Instabilities occur when the interface between two fluids of different densities is impulsively accelerated, typically by the passage of a shock wave. These instabilities play a critical role in the fields of fluid mechanics and are essential in various applications including inertial confinement fusion, combustion engines, astrophysics, and supernova research.

Features

The algorithm is designed to extract the following features:

Amplitude: This feature corresponds to the maximum perturbation growth of the RMI.
Span: This represents the breadth of the instability across the cross section of the fluid interface.
Stream: This refers to the fluid element of highest speed in the instability.
Neck: This signifies the narrowest constriction in the fluid flow in the instability.
Algorithm

The feature extraction algorithm is based on a brute force search method. It iterates over the data, conducting exhaustive searches to find the values that represent the four features.

Here's a brief overview of how the algorithm works:

Data Structuring: The algorithm first sorts the data in ascending order of the 'y' value, structuring the data for subsequent processing.
Interface Definition: It then defines the interface based on specific alpha air values.
Feature Calculation: The algorithm conducts exhaustive searches to find the data points representing the amplitude, span, stream, and neck.
Visualization: Finally, it visualizes the current RMI shape and the identified features.
Please refer to the source code for more detailed information about the implementation.

Usage

This algorithm is implemented in Python, leveraging libraries such as numpy, pandas, and matplotlib for data manipulation and visualization. To use the algorithm, ensure that these libraries are installed in your Python environment.

Contributing

This algorithm was developed by the Matar Fluid Group at Imperial College London as part of the PhD. project "Richtmyer-Meshkov Instabilities in Newtonian and non-Newtonian Flows". Contributions are welcomed to improve the algorithm and expand its capabilities.

This README provides a brief overview of your algorithm and its purpose. It could be expanded with sections on installation instructions, usage examples, or more detailed information about the algorithm and RMIs. Also, remember to add your contact information for people who have further questions.
