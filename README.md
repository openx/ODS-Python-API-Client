For OpenX Reporting access using the Python API Client you will need:
(examples come from an Ubuntu machine)

### 1. Your credentials:
- consumer_key,
- consumer_secret,
- email address and password for your user of your OpenX instance.

### 2. install pip and pipenv

 update the package list
<code>$ sudo apt update</code>

Install pip and pipenv
<code>$ sudo apt install python3-pip python3-dev
$ pip3 install --user pipenv</code>

Add pipenv (and other python scripts) to PATH
<code>$ echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
$ source ~/.bashrc</code>


### 3. Create your virtual environment with pipenv

run the following command in your working directory
<code>$ pipenv shell</code>


### 4. Now, being in your virtual environment download the library into your working directory:

<code>$ git clone https://github.com/openx/ODS-Python-API-Client.git</code>

### 5. Go to the downloaded repository and install the library:

<code>$ python setup.py install</code>

Now, setup your Python API Client.

### 5. Create ".ox3rc" (vim .ox3rc) file in the directory where Python-API-Client library is installed. Format the file as present below:

<code>[ox3apiclient]
envs=
    prod

[prod]
email: you@example.com
password: password123
domain: uidomain.com
realm: uidomain_realm
consumer_key: 1fc5c9ae...
consumer_secret: 7c664d68...
api_path: /data/1.0</code>


An example of such a config:

email: myemail@domain.com
password: 123qwe456rty
domain: my2ads-ui3.openxenterprise.com
realm: my2ads
consumer_key: 23fa23fa2fas2adsf1asd2asd2asd1asdf2asd33a
consumer_secret: 123a23aasd2asd33adssd3a2sad2asdsad33asd2
api_path: /data/1.0


### 6. Edit 'report_config.py' file - place your request body into the 'settings' variable.

The settings variable is responsible for the request body, you can place there any specific dates / hours / attributes and metrics that will define your report. In this particular example you will pull "Inv_perf_pub" type report for the 15th of June 2019. For more information visit http://openxcorporate-ui3.openxenterprise.com/data/1.0/ods.html

### 7. Run the python script
- 'pull_fields.py' to see all the available fields

<code>$ python pull_fields.py</code>

- 'pull_reports.py' to pull your report

<code>$ python pull_report.py</code>
