# text-to-image (main)

Text-to-image module's implementation on AWS or other servers. 

#### Cloning the Main Repository :
```
git clone -b main https://github.com/usmanghani6080/text-to-image-generator.git
```

#### Navigate to Main Repository :
```
cd text-to-image-generator
```

#### Installing python :
```
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.10 -y
sudo apt install python3.10-venv -y
sudo apt install python3.10-dev -y
```
#### Creating virtual Environment :
```
python3.10 -m venv tti-venv
source tti-venv/bin/activate
```
#### Installing dependencies:
```
pip install --upgrade pip
pip install --upgrade diffusers transformers accelerate peft
pip install fastapi[all]
```

#### Running API Code:
```
uvicorn app:app --host 0.0.0.0 --port <any> --reload
```