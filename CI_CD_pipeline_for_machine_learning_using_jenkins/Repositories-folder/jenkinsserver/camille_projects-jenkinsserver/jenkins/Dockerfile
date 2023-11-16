FROM jenkins/jenkins:lts
MAINTAINER cgirabawe@gmail.com
USER root
RUN apt-get update
RUN apt-get -qy install apt-utils curl wget git tree python3-pip && rm -rf /var/lib/apt/lists/*
RUN apt-get update

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda config --add channels defaults 
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda
RUN conda --version

RUN git config --global user.email "jenkins@master.domain" 
RUN git config --global user.email "jenkins master"
