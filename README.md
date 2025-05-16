# Machine Learning Predicts Regioselectivity in Pd-Catalyzed Directing Group-Assisted C–H Activation

In palladium-catalyzed C–H activation reactions, regioselectivity — i.e., where the C–H bond is activated — is critical for designing pharmaceuticals, materials, and complex organic frameworks. Traditional methods to predict this selectivity often rely on empirical rules or computationally expensive quantum chemical calculations.
This tool, omp-predictor, uses machine learning to rapidly and accurately predict the directing group-assisted regioselectivity (meta, ortho, para, or non-directing) in aryl substrates involved in Pd-catalyzed C–H activation. Based on models trained from curated reaction datasets, the predictor leverages structural fingerprints (Morgan fingerprints) and pre-trained classifiers (SVM and Logistic Regression) to classify input molecules.
The standard SVM model demonstrated excellent performance with an F1 score of 0.92 and Matthews correlation coefficient (MCC) of 0.93 on held-out test data, indicating strong generalizability. This approach significantly aids in the early-stage design of catalytic strategies for regioselective C–H activation.

![Diagram](https://pubs.acs.org/cms/10.1021/acs.orglett.5c01158/asset/images/medium/ol5c01158_0006.gif)
![Diagram](https://pubs.acs.org/cms/10.1021/acs.orglett.5c01158/asset/images/medium/ol5c01158_0007.gif)

## omp-predictor

A command-line tool to predict regioselectivity in Pd-catalyzed, directing-group-assisted C–H activation using machine learning models.

This package uses molecular fingerprints and pre-trained models (Logistic Regression and SVM) to classify substitution patterns (meta, ortho, para, or non-directing) from `.mol` files.

<pre lang="markdown">
├── omp_predictor/
│   ├── __init__.py
│   ├── omp.py
│   ├── encoder.py
│   ├── fingerprint.py
│   ├── lg_model.pkl
│   ├── svm_model.pkl
│   ├── lf_lg_model.pkl
│   └── lf_svm_model.pkl
├── setup.py
├── README.md
└── .gitignore </pre>

---

## 🚀 Installation

First, clone the repository:

```bash
git clone https://github.com/arko-mohari/omp-predictor.git
cd omp-predictor
pip install .
```

## 🧪 Usage

Place your .mol files in a folder (e.g., mol_files) and run:

```bash
omp ./mol_files
```

Optional flags:

--lf: Use the large fragment encoder (default is Standard Morgan Fingerprint)

--logreg: Use Logistic Regression (default is SVM)

```bash
omp ./mol_files --lf --logreg
omp ./mol_files --logreg
```
If you use this package in your work, please cite:

R. A. Oshiya; Mohari A.; Datta A.* Machine Learning Predicts Regioselectivity in Pd-Catalyzed Directing Group-Assisted C–H Activation. *Org. Lett.* **2025**, *27*, (19), 4909-4914. 

[Link to article](https://pubs.acs.org/doi/10.1021/acs.orglett.5c01158)
