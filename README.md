For OpenX Reporting access using the Python API Client you will need:
(examples come from an Ubuntu machine)

### 1. Your credentials:
- consumer_key,
- consumer_secret,
- email address and password for your user of your OpenX instance.

### 2. install pip and pipenv

Update the package list
<code>$ sudo apt update</code>

Install pip and pipenv
<code>$ sudo apt install python3-pip python3-dev </code> 

<code>$ pip3 install --user pipenv</code>

Add pipenv (and other python scripts) to PATH
<code>$ echo "PATH=$HOME/.local/bin:$PATH" >> ~/.bashrc
$ source ~/.bashrc</code>


### 3. Create your virtual environment with pipenv

Run the following command in your working directory
<code>$ pipenv shell</code>


### 4. Now, being in your virtual environment download the library into your working directory:

<code>$ git clone https://github.com/openx/ox-ods-python-test</code>

### 5. Go to the downloaded repository and install the library:

<code>$ python setup.py install</code>

Now, setup your Python API Client.

### 6. Edit 'my_creds.py' file - add your credentials.

### 7. Edit 'report_config.py' file - place your request body into the 'settings' variable.

The "settings" variable is responsible for the request body, you can place there any specific dates / hours / attributes and metrics that will define your report. In this particular example you will pull "Inv_perf_pub" type report for the 15th of June 2019. For more information visit http://openxcorporate-ui3.openxenterprise.com/data/1.0/ods.html

If you want to find out what is the date range available for the selected report - please make sure you have the same metrics and attributes in the "data_range" variable as you have in the "settings" variable.

### 7a. Edit 'post_config.py' file - place your request body into the 'settings' variable.

The "settings" variable is responsible for the request body, you can place there specific attributes when, e.g. creating an ad unit. For more information visit  https://docs.openx.com/Content/developers/platform_api/api_ref.html

### 8. Run the python script
- 'pull_fields.py' to see all the available fields

<code>$ python pull_fields.py</code>

- 'date_range.py' to check what is the available date range for selected report (earliest possible StartData, closest possible EndDate)

<code>$ python pull_report.py</code>

- 'pull_reports.py' to pull your report

<code>$ python pull_report.py</code>

- 'ox_post.py' to send a request to our legacy endpoint, can be used to, e.g create a site.

<code>$ python ox_post.py</code>
