from setuptools import setup, find_packages

setup(
    name="omp-predictor",
    version="1.0.0",
    description="Predict regioselectivity in Pd-catalyzed C-H activation using machine learning.",
    author="Ayan Datta, Arko Mohari, Oshiya RA",
    author_email="spad@iacs.res.in",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "omp_predictor": ["*.pkl"],
    },
    install_requires=[
        "numpy>=1.26.4",
        "scikit-learn>=1.6.1",
        "rdkit>=2025.3.2",
        "joblib>=1.4.2",
    ],
    entry_points={
        "console_scripts": [
            "omp=omp_predictor.omp:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
