# machine-learning-practice
Repository for breaking and making machine learning models




### Major Tools Used

Data Ingest (When necessary)
- Airbyte
  - Pre-requisites:
    - Docker
  - Nice to have:
    - Terraform

Data Warehouse 
- Google BigQuery

Data Transformation and Cleaning
- DBT Cloud

Programming Language
- Python

Machine Learning Libraries
- scikit-learn
- pytorch

# Setup
- Create new repository
  - README 
  - License
  - .gitignore
- Create development branch

- Install Google SDK CLI

- Create GCP project
- Create service acc and credentials json for dbt cloud access
  
- Setup dbt subdirectory and project connected to GCP project
- Initialize dbt cloud proj in dev branch

- Create virtual environment
- Activate `source machine-learning-practice/bin/activate`
- Install required libraries `pip3 install -r requirements.txt`