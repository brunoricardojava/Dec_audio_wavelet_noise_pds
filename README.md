# Dec_audio_wavelet_noise_pds 
## Trabalho de PDS, envolvendo Discrete Wave Transform (DWT), para tratamento de ruido branco gaussiano aditivo em sinais de áudio.

Este trabalho utilizara a linguagem python, para desenvolvimento dos scripts de foco principal, como a implementação da transformada wavelet e apresentação dos resultados. Usaremos a ferramenta Jupyter para elaboração do relatorio.

Instalando o Jupyter atravez de uma imagem docker da anaconda: "https://www.continuum.io/blog/developer-blog/anaconda-and-docker-better-together-reproducible-data-science"

##### Comando para criar uma imagem do Jupyter usando uma imagem do projeto Anaconda
> $ docker build --tag anaconda_jupyter .

##### Comando para iniciar o container Jupyter
> $ docker run -it -p 8888:8888 --name Jupyter anaconda_jupyter:latest

OBS: Link referente a documentação para criar o arquivo da senha: http://testnb.readthedocs.io/en/stable/examples/Notebook/Configuring%20the%20Notebook%20and%20Server.html


## Metas

- [ ] Implementar blocos de processamento para realizar os estágios de analise e sintese de uma DWT (cascata de banco de filtros)
- [ ] Redigir relatório técnico, comparando o desempenho entre a DWT e filtragem passa-baixas convencional (aproximação de Butterworth, passa-baixa, especificações a determinar, a ser projetado usando uma ferramenta pronta como o fdatool do Matlab)

## Etapas

- [ ] Formar as duplas de trabalho
- [ ] Implementar as funções para cascata de banco de filtros
- [ ] Definir o sinal de áudio a ser usado como referência (sinal original, sem ruído)
- [ ] Determinar três sinais de teste, obtidos por contaminação da referência por ruído AWGN. Os sinais de teste resultantes deverão apresentar as seguintes SNRs:
	-  10  dB
	-  0   dB
	- -10  db
- [ ] Filtrar cada um dos sinais de teste usando:
	- Filtro Butterworth passa-baixas
	- DWT usando SOFT e HARD thresholds
	> A definir: especifiações do filtro Butterworth, wavelet-mãe e número de níveis de decomposição da DWT
- [ ] Avaliação dos resultados:
	- Comparação da SNR do sinal filtrado
	- Avaliação subjetiva informal (opinião de pessoas)

- [ ]  Entrega de relatório técnico (05.09), códigos fonte (05.09), slides da apresentação (05.09) e apresentação em sala (06.09).
	- O relatório técnico deve apresentar um registro preciso do contéudo técnico estudado, e conter Resumo, Introdução, Base téorica, etodologia experimental, Resultados, Conclusões e Referências bibliográficas. Tal relatório não deve exceder 4 páginas.
	- A apresenta¸c˜ao ser´a feita no dia 06.09 no hor´ario de aula, deve ser baseada no relat´orio t´ecnico e ter´a dura¸c˜ao de 10 min. Os crit´erios usados para avaliar as apresenta¸c˜oes incluem: uso de recursos de apresenta¸c˜ao (slides), numera¸c˜ao dos slides, estrutura da
apresenta¸c˜ao (slide de t´ıtulo, agenda da apresenta¸c˜ao, conte´udo, conclus˜oes, referˆencias), corre¸c˜ao ortogr´afica e gramatical, express˜ao oral, corre¸c˜ao das informa¸c˜oes, uso do tempo.
	- Os c´odigos fonte devem estar devidamente comentados (nome dos autores, data, e coment´arios explicativos das fun¸c˜oes e a¸c˜oes no c´odigo)
	- O relat´orio t´ecnico, c´odigos fonte e slides devem ser enviados para o email zampolo@ieee.org at´e o dia 05.09.2017.

## Refêrencia
1. Oppenheim, Schafer. Processamento em tempo discreto de sinais, 3a edi¸c˜ao, Pearson.
2. Diniz, Silva, Netto. Processamento digital de sinais, 2a edi¸c˜ao, Bookman.
3. http://cs.haifa.ac.il/hagit/courses/seminars/wavelets/Presentations/Lecture09 Denoising.pdf
4. http://cdn.intechopen.com/pdfs/34967/InTech-Signal and image denoising using wavelet transform.pdf
5. https://pdfs.semanticscholar.org/3dfd/6b2bd3d6ad3c6eca50747e686d5ad88b4fc1.pdf
6. https://theses.lib.vt.edu/theses/available/etd-12062002-152858/unrestricted/Chapter4.pdf