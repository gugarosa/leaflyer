# Leaflyer: Cannabis Data Scrapper

*This repository holds all the necessary code to run the an automation robot that extracts strain-related information at [Leafly](https://www.leafly.com).*

---

## Package Guidelines

### Installation

Install all the pre-needed requirements using:

```Python
pip install -r requirements.txt
```

### (Optional) Download the Data

We have already dumped all of Leafly's data and made available in both `.json` and `.csv` formats. Note that there might be some missing values as Leafly's database is incomplete for not well-known strains.

* [Leafly Cannabis Data](https://www.recogna.tech/files/datasets/leafly_strain_data.tar.gz)

*The dataset and its additional information is also available at [Kaggle](https://www.kaggle.com/gthrosa/leafly-cannabis-strains-metadata)*.

---

## Usage

### Scrap List of Strains

Initially, one need to scrap/dump the list of strains (URL format) to proceed with the meta-data extraction. To accomplish such a step, one needs to use the following script:

```Python
python scrap_strains_list.py -h
```

*Note that `-h` invokes the script helper, which assists users in employing the appropriate parameters.*

### Scrap Strains Meta-Data

Further, with the strains' list in hands, it is now possible to extract JSON-like information from every URL that has been found. To fulfill this purpose, just use the following script:

```Python
python scrap_strains_data.py -h
```

---

### Bash Script

Instead of invoking every script to conduct the automation, it is also possible to use the provided shell script, as follows:

```Bash
./pipeline.sh
```

Such a script will conduct every step needed to accomplish the automation process. Furthermore, one can change any input argument that is defined in the script.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository or gustavo.rosa@unesp.br.

---
