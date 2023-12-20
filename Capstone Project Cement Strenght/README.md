# Concrete Compressive Strength Prediction

## Description of the Problem

### Context

Concrete is the cornerstone of civil engineering, playing a vital role in the construction industry. The compressive strength of concrete is a critical property, influencing the structural integrity and performance of buildings and infrastructure. Predicting concrete compressive strength is a complex task, as it is a highly nonlinear function of various factors, including the age of the concrete and the proportions of different components in the mixture.

### Problem Overview

This project addresses the regression problem of predicting concrete compressive strength based on a dataset containing 1030 instances. The dataset consists of 8 quantitative input variables representing different components in a concrete mixture and 1 quantitative output variable, which is the concrete compressive strength measured in Mega Pascals (MPa). The primary goal is to develop a model that accurately predicts the compressive strength of concrete based on these input variables.

## About the Dataset

### Data Set Information

- **Number of Instances:** 1030
- **Number of Attributes:** 9
- **Attribute Breakdown:** 8 quantitative input variables, and 1 quantitative output variable
- **Missing Attribute Values:** None

### Attribute Information

1. **Cement (component 1):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of cement in the mixture.

2. **Blast Furnace Slag (component 2):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of blast furnace slag in the mixture.

3. **Fly Ash (component 3):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of fly ash in the mixture.

4. **Water (component 4):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of water in the mixture.

5. **Superplasticizer (component 5):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of superplasticizer in the mixture.

6. **Coarse Aggregate (component 6):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of coarse aggregate in the mixture.

7. **Fine Aggregate (component 7):**
   - Data Type: Quantitative
   - Measurement: kg in a m3 mixture
   - Description: Input variable representing the amount of fine aggregate in the mixture.

8. **Age:**
   - Data Type: Quantitative
   - Measurement: Day (1~365)
   - Description: Input variable representing the age of the concrete in days.

9. **Concrete Compressive Strength (TARGET VARIABLE):**
   - Data Type: Quantitative
   - Measurement: MPa
   - Description: Output variable representing the compressive strength of the concrete.

## Instructions on how to run the project

#### System requirements
* Python
* Docker desktop installed

#### Installation and dependency management
Follow the next steps to run the model.
1. Download contents of this repository into your local machine.
2. Setup the environment.  
`pip install pipenv`
`pipenv install`
3. Activate the environment
Activate the virtual environment to work within it:
`pipenv shell`
4. Step 5: Running the Project
Once the environment is activated, follow  instructions provided in the project's documentation or source code to run the project.

#### Containerization
1. Build the docker image
`docker build -t capstone-project .`
2. Run the docker container
`docker run -it --rm -p 9696:9696 capstone-project`
3. Access the application
Run the `predict_test.py` file in order to post a request to the web server where the model is deployed.

#### Video evidence
Go to the `Video Demonstration - Capstone Project` file in this repository for video evidence of the model running as a web service on a docker container.