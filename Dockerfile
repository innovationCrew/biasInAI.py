# Build : docker build -t biasinai .
# Run  : docker run --rm -ti -v $PWD:/project -p 5000:5000 -p 80:80 biasinai
# RunApp : cd web && uwsgi --ini uwsgi.ini

# Use an official python runtime as parent
FROM continuumio/miniconda3

#update Conda
RUN conda update -n base conda
RUN conda config --add channels conda-forge #for uwsgi

#Install numpy and other packages
#RUN conda install numpy
#RUN conda install flask

#install packages
ADD requirements.txt  /tmp/requirements.txt
RUN conda install --yes --file /tmp/requirements.txt

#install uwsgi
#RUN conda install -c conda-forge uwsgi 

#Expose port 80 and 5000 to the world ouside of this container
EXPOSE 80
EXPOSE 5000

WORKDIR /project

#Run the bash shell
CMD ["/bin/bash"]
