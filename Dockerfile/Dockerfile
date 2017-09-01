#Dockerfile para gerar imagem que roda um server jupyter localmente
#A senha será configurada manualmente no arquivo "jupyter_notebook_config.py"

#Comando para gerar a imagem: "docker build --tag anaconda_jupyter ."
#OBS: O comando deve ser usado no mesmo diretorio do arquivo Dockerfile, caso contrario especificar o PATH e o nome do arquivo.

#Comando para gerar o container: "docker run -it -p 8888:8888 -v "Path_local_notebooks":/opt/notebooks -v "Path_local_config_file":/root/.jupyter --name Jupyter anaconda_jupyter"

#Documentação de como colocar a senha: http://testnb.readthedocs.io/en/stable/examples/Notebook/Configuring%20the%20Notebook%20and%20Server.html

FROM continuumio/anaconda3

MAINTAINER Bruno Scherer<brunoricardojava@gmail.com>

LABEL Description="Essa imagem serve para rodar um notebook Jupyter"

EXPOSE 8888

RUN conda install jupyter -y --quiet
RUN conda install -c conda-forge librosa

RUN mkdir /opt/notebooks
VOLUME /opt/notebooks

RUN mkdir /root/.jupyter
COPY jupyter_notebook_config.py /root/.jupyter
VOLUME /root/.jupyter

CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
