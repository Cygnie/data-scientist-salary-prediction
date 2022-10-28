# Data Scientist Salary Prediction

![image](https://media.istockphoto.com/vectors/data-analysis-concept-vector-banner-illustration-vector-id1321230055?k=20&m=1321230055&s=612x612&w=0&h=4FqbjHF64W7dvKhnpjOszHiAK50XatodvnHYjLoPeEg= )

### The main goal here is to estimate data scientist salaries based on the information provided.
### You can also find the notebook version of this project on [the link](https://github.com/Cygnie/notebooks/tree/main/Data-Scientist-Salaries).

# Software And Tools Requirements

1. [Github Account](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
5. [Docker](https://www.docker.com/)


# Dataset 

* Download the dataset for custom training. You can also find more details about the dataset at this link.

    * https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

# Installation

* You can create a new environment for this project. If you want to make edits to the project and try new models, I recommend creating a new environment.

## Create a new environment

```
conda create -p venv python==3.7 -y
```

## Download the required libraries

```
pip install -r requirements.txt
```

## Run the demo

```
python app.py
```

# To Set up CI/CD pipeline in heroku we need 3 information

1. Open your project repository and go to: Settings > Secrets > Actions
2. Create a new Repository secret
3. Define the specified names one by one and fill them with your own information.

    * HEROKU_API_KEY
    * HEROKU_APP_NAME
    * HEROKU_EMAIL


# I deployed this project with heroku. Enjoy it

https://ds-job-salaries-prediction.herokuapp.com/


# Author
* [Furkan CEYRAN](https://github.com/Cygnie)