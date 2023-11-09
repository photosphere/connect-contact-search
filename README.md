## About Amazon Connect Quick Connects CDK
This solution can be used to create quick connects and associate/disassociate these with queues.

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

