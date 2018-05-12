# DockerHackathon
## About
This is a project from a School Sponsored Docker Hackathon


## Requirements
- Latest version of Docker for your OS


## Installation
1. [Install Docker](https://docs.docker.com/install/)

2. In your terminal in the directory for this repository, run:
`docker-compose up`
- This will output something like this in your terminal:
tarting datascience-notebook-container ... done
Attaching to datascience-notebook-container
```
datascience-notebook-container | /usr/local/bin/start-notebook.sh: ignoring /usr/local/bin/start-notebook.d/*
datascience-notebook-container |
datascience-notebook-container | Container must be run with group root to update passwd file
datascience-notebook-container | Executing the command: jupyter notebook
datascience-notebook-container | [W 00:26:28.432 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
datascience-notebook-container | [I 00:26:28.472 NotebookApp] JupyterLab beta preview extension loaded from /opt/conda/lib/python3.6/site-packages/jupyterlab
datascience-notebook-container | [I 00:26:28.472 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
datascience-notebook-container | [I 00:26:28.481 NotebookApp] Serving notebooks from local directory: /home/jovyan
datascience-notebook-container | [I 00:26:28.482 NotebookApp] 0 active kernels
datascience-notebook-container | [I 00:26:28.482 NotebookApp] The Jupyter Notebook is running at:
datascience-notebook-container | [I 00:26:28.482 NotebookApp] http://[all ip addresses on your system]:8888/?token=dfdfa78ab2a339dd88e4210eaf32050def83f66107b6d8d9
datascience-notebook-container | [I 00:26:28.483 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
datascience-notebook-container | [C 00:26:28.488 NotebookApp]
datascience-notebook-container |
datascience-notebook-container |     Copy/paste this URL into your browser when you connect for the first time,
datascience-notebook-container |     to login with a token:
datascience-notebook-container |         http://localhost:8888/?token=dfdfa78ab2a339dd88e4210eaf32050def83f66107b6d8d9
```

3. Look for the `localhost:8888` with a token value proceeding it
- Click on the link

4. Your `localhost:8888` should display a Jupyter notebook
- Click on the `Hackathon Demo.ipynb` file

5. Read the analysis


## Other files
- `docker-compose.yml` - file that creates the docker container to run Jupyter Notebooks
- `kickstarter_analyze.py` - file that analyzes kickstarter data in the Data folder

## Bugs
No bugs found yet

## Authors
* [Isaiash Becker-Mayer](https://github.com/ibeckermayer)
* [Nickolas Teixeira](https://github.com/nickolasteixeira)
* [Spence Taylor](https://github.com/set808)
