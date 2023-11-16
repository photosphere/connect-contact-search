## About Amazon Connect Contact Search Tool
This solution can be used to search contact with specified attributes in Amazon Connect.

### Installation

Clone the repo

```bash
git clone https://github.com/photosphere/connect-contact-search.git
```

cd into the project root folder

```bash
cd connect-contact-search
```

#### Create virtual environment

##### via python

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment.

On Linux, or OsX 

```bash
source .venv/bin/activate
```
On Windows

```bash
source.bat
```

Then you should install the local requirements

```bash
pip install -r requirements.txt
```
### Build and run the Application Locally

```bash
streamlit run contact_search.py
```
#### Configuration screenshot
<img width="1044" alt="Contact Search" src="https://github.com/photosphere/connect-contact-search/assets/3398595/a4eafc63-8e89-4dcb-87b6-0c88e583a662">
