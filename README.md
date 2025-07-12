# nlp_polarity_analysis

#=====================================
Este proyecto fué realizado en el marco del Verano Delfín 2025 en Bogotá, Colombia.

### Stage 1: Data Importing, Cleaning, and Preprocessing 

This stage loads the raw CSV data and prepares it for analysis by:

1. **Importing Data**  
   Loads the headlines and comments from the specified CSV file.

2. **Cleaning Text**  
   - Removes non-alphanumeric characters.
   - Converts text to lowercase for consistency.
   - Applies these transformations only to text columns starting from a configurable column index.

3. **Saving Cleaned Data**  
   The cleaned data is saved as `cleaned_data.csv` in the catalog directory, ready for further processing in Stage 2.

**Input:** Raw CSV file (e.g., `DATA_PRUEBA.csv`)  
**Output:** `cleaned_data.csv`


### Stage 2: Data Tokenization

This stage processes the cleaned text data by applying two main steps:

1. **Stopwords Removal**  
   Removes common words (stopwords) in the selected language (e.g., English) from each text column starting from a configurable column index. The goal is to reduce noise and focus on meaningful words.

2. **Stemming**  
   Applies stemming to the remaining words to reduce them to their root forms (e.g., "running" → "run"). This helps standardize word variations and improve the quality of text analysis.

The result is saved as a new CSV file where each processed cell contains a list of tokenized, cleaned, and stemmed words, ready for downstream NLP tasks such as classification or topic modeling.

**Input:** `cleaned_data.csv` (output from Stage 1)  
**Output:** `tokenized_data.csv` (each cell contains a list of tokens)


### 3 Stage 

### 4 Stage 


## Repository Structure
```
.
├── catalog/      # Processed data files and outputs (e.g., cleaned and tokenized CSVs).
├── data/         # Original data (.csv).
├── environment/  # Conda environment configuration files.
├── modules/      # Python modules and scripts. Main entry point: run_polarity.py
├── notebooks/    # Jupyter notebooks for testing and experimentation.
├── plots/        # Generated plots and visualizations.
├── .gitignore    # Specifies files and folders to exclude from Git version control.
└── README.md     # Project documentation and usage instructions.

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

The input CSV file should include the following columns:
```

+----+----------------------------------------+-------------------------------+------------------------------+------------------------------+
| ID | Link | Headliner | Comment 1 | Comment 2 |
+----+----------------------------------------+-------------------------------+------------------------------+------------------------------+
| 1 | "https://example.com/article1" | "Breaking News: Event X!" | "Great news!" | "Can't wait for more info." |
| 2 | "https://example.com/article2" | "New Discoveries in Science" | "This is groundbreaking." | "I love this!" |
+----+----------------------------------------+-------------------------------+------------------------------+------------------------------+

```

- **ID**: A unique identifier for each entry.
- **Link**: The URL or reference link to the original article.
- **Headliner**: The text of the news headline.
- **Comment n**: Each additional column represents an individual comment associated with the headline.

---

By following this unified format, the data can be easily loaded, cleaned, and processed for analysis in the pipeline.


## Running the Clustering Script

The `modules/` directory contains the main script **`run_polarity.py`**, which serves as the primary entry point for executing the polarity analysis process. To run the script, simply use the following command in the terminal (with activated conda environment):  

```bash
python run_polarity.py
```

#### Configuring Execution Stages

At the beginning of `run_polarity.py`, there is a specific line that defines which stages of the polarity analysis process will be executed:

```python
stages = [1] will only run Stage 1 (data importing and cleaning).
stages = [2] will only run Stage 2 (tokenization).
stages = [1, 2] will run both stages sequentially.
```
