import pandas as pd
import numpy as np
from semopy import Model, report

# Professional Synthetic Data Generation (N=600)
def generate_sem_dataset():
    np.random.seed(42)
    n = 600
    
    # Defining Latent Variables (The core constructs)
    # AI-Personalization (AIP) -> Perceived Trust (TRST) -> Financial Decision Quality (FDQ)
    AIP = np.random.normal(0, 1, n)
    TRST = 0.75 * AIP + np.random.normal(0, 0.4, n)
    FDQ = 0.65 * TRST + 0.22 * AIP + np.random.normal(0, 0.3, n)
    
    # Mapping Latent Variables to Observed Indicators (Survey Items)
    data = {
        'aip_1': 0.88 * AIP + np.random.normal(0, 0.4, n),
        'aip_2': 0.82 * AIP + np.random.normal(0, 0.4, n),
        'aip_3': 0.85 * AIP + np.random.normal(0, 0.4, n),
        
        'trst_1': 0.90 * TRST + np.random.normal(0, 0.3, n),
        'trst_2': 0.86 * TRST + np.random.normal(0, 0.3, n),
        'trst_3': 0.84 * TRST + np.random.normal(0, 0.3, n),
        
        'fdq_1': 0.92 * FDQ + np.random.normal(0, 0.2, n),
        'fdq_2': 0.88 * FDQ + np.random.normal(0, 0.2, n),
        'fdq_3': 0.86 * FDQ + np.random.normal(0, 0.2, n)
    }
    
    df = pd.DataFrame(data)
    # Scaling to a 1-7 Likert Scale
    df = ((df - df.min()) / (df.max() - df.min()) * 6) + 1
    return df.round(3)

# Initialize and save
dataset = generate_sem_dataset()
dataset.to_csv('fintech_sem_dataset.csv', index=False)

# Define SEM Model Structure
model_desc = """
    # Measurement Model
    AIP =~ aip_1 + aip_2 + aip_3
    TRST =~ trst_1 + trst_2 + trst_3
    FDQ =~ fdq_1 + fdq_2 + fdq_3
    
    # Structural Model (Path Analysis)
    TRST ~ AIP
    FDQ ~ TRST + AIP
"""

model = Model(model_desc)
model.fit(dataset)
print(model.inspect())
