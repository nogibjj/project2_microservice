install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#conda env create -f environment.yml
	#conda activate hf
	##had to do this as well
	#conda install pytorch torchvision -c pytorch
	#conda install -c conda-forge pyarrow
