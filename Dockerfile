FROM ubuntu:trusty

#install git, vim, gcc, etc
RUN sudo apt-get update && apt-get install -y gcc curl vim git emacs python3
RUN sudo apt-get install -y python3-pandas python3-matplotlib python3-numpy

WORKDIR /app
ADD . /app

CMD ["python3", "test.py"]
