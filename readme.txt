
### 1. Install Miniconda

* Download Miniconda from the official site:
  [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
* Install it and **allow Conda to initialize** during setup.

---

### 2. Open Conda Prompt

* On Windows: open **“Anaconda Prompt (Miniconda)”**
* On macOS/Linux: open **Terminal**

---

### 3. Create a New Conda Environment

conda create -n todo python=3.10

### 4. Activate the Environment

conda activate todo

### 5. Navigate to the Project Directory


cd path/to/your/project



### 6. Install Dependencies from `requirements.txt`


pip install -r requirements.txt

### 7. Verify Installation

pip list


### 8. (Optional) Deactivate Environment


conda deactivate


If `pip` is not available, install it using:
conda install pip
