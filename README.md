# nlp_polarity_analysis

#=====================================
Este proyecto fué realizado en el marco del Verano Delfín 2025 en Bogotá, Colombia.

### 1 Stage 

    - This stage is responsible for loading the headline and comment files. After loading, it cleans the alphanumeric characters and converts all text to lowercase for processing.

### 2 Stage 

### 3 Stage 

### 4 Stage 


## Repository Structure
```
.
├── data/         # Original data (.csv).
├── environment/  # Conda environment for python.
├── modules/      # Python scripts for running the program and modules. Main script : run_polarity.py
├── notebooks/    # Python notebooks for testing the program.
├── plots/        # Output plots from the script.
├── .gitignore    # Specifies which files should be ignored by Git (e.g., data and generated outputs).
└── README.md     # Repository documentation

```

## Conda environment setup

Inside directory `environment/` there is a file named `polarity_analysis_env.yml`. This file is used to set up a dedicated Conda environment with all the necessary dependencies for running the code in this repository.

To create the environment, first ensure you have **Anaconda** or **Miniconda** installed on your system. You can download it from [Anaconda's official website](https://www.anaconda.com/download). Then, open a terminal and run the following command:


```bash
conda env create -f polarity_analysis_env.yml
```

This command will create a new Conda environment named `polarity_analysis_env`, installing all required libraries and dependencies automatically.

#### Activating and Deactivating the Environment

Once the installation is complete, you can activate the new environment by running:


```bash
conda activate polarity_analysis_env
```

If you need to switch to another environment or deactivate it, simpy run:

```bash
conda deactivate
```

## File Format for CSV Files

### Headline File (`titulares.csv`):
The headline file should consist of two main columns:

+---------+----------------------------+
| ID | Headline |
+---------+----------------------------+
| 1 | "Breaking News: Event X!" |
| 2 | "New Discoveries in Science"|
+---------+----------------------------+

- **ID**: A unique identifier for each headline.
- **Headline**: The text of the headline.

### Comment File (`commentarios.csv`):
The comment file should include an **ID column** to establish the relationship with the headlines file, followed by multiple columns of comments. Each comment will be placed horizontally, one comment per column:

+---------+------------------------------+----------------------------+----------------------------+
| ID | Comment 1 | Comment 2 | Comment 3 |
+---------+------------------------------+----------------------------+----------------------------+
| 1 | "Great news!" | "Can't wait for more info." | "So interesting!" |
| 2 | "This is groundbreaking." | "I love this!" | "Science is amazing!" |
+---------+------------------------------+----------------------------+----------------------------+

- **ID**: A unique identifier to link comments to the corresponding headline.
- **Comment n**: Each column represents an individual comment related to the headline.

---

By following this format, the data can be easily loaded and processed for further analysis.


## Running the Clustering Script

The `modules/` directory contains the main script **`run_polarity.py`**, which serves as the primary entry point for executing the polarity analysis process. To run the script, simply use the following command in the terminal (with activated conda environment):  

```bash
python run_polarity.py
```

#### Configuring execution stages

At the beginning of `run_polarity.py`, ther is a specific line that defines which stages of the polarity analysis process will be executed:

```python
stages = [1]
```
