FROM ubuntu:trusty

ENV PATH="~/.local/bin/:${PATH}"

#install git, vim, gcc, etc and all dependencies to run our analysis
RUN sudo apt-get update && apt-get install -y gcc curl vim git emacs python3
RUN sudo apt-get install -y python3-pandas python3-matplotlib python3-numpy 
RUN sudo apt-get install -y python3-pip ipython3
RUN pip3 install --upgrade pip
RUN pip3 install jupyter

# adds every file in the current working directory on your host machine to the 
# /app container
WORKDIR /app
ADD . /app

#if you want to use a file and test it with python3 in our docker container
CMD ["python3", "test.py"]

#if you want to run build the container and run interactively
#CMD ["/bin/bash"]

