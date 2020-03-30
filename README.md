Run project in two ways

1. Use docker
2.manual build


Docker build

- Build Dockerfile:
  
- Run Docker image:

- Run project: 
  python main.py
  
- Choose data file 
  stored in data directory inside project 
  example: PATH_TO_PROJECT/computer_systems_reliability_lab1/data/gamma.csv

Manual build

#Go to project directory:

  cd computer_systems_reliability_lab1/

#Activate dev environment:

   source venv/bin/activate
   
#Install dependencies:

  sudo apt-get install -y python3-tk
  pip install -r requirements.txt
  
#Run project: 
  python main.py
  
#Choose data file:

  stored in data directory inside project 
  example: PATH_TO_PROJECT/computer_systems_reliability_lab1/data/gamma.csv
