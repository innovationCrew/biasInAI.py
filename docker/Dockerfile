# Use an official python runtime as parent
FROM continuumio/miniconda3

#update Conda
RUN conda update -n base conda

#Install numpy and other packages
RUN conda install numpy
RUN conda install flask
#conda install --yes --file requirements.txt

#Expose port 80 and 5000 to the world ouside of this container
EXPOSE 80
EXPOSE 5000

WORKDIR /project

#Run the bash shell
CMD ["/bin/bash"]