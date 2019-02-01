# THS_Inventory_Count

Before Launch, navigate to program directory and make sure to install requirements:
$ pip install -r requirements.txt


To launch: python shell.py

1. Load data: > load filepath
this will load single csv into database

2. Check length of imported data 
> length product_data
compare this to your input data. Should equal number of rows in csv

3. create the count for each outlet
> create_count Outlet
it will prompt you to name the inventory count. Do so

4. Check the count has been created. you can do this on the vend website. you should also do this in the shell.
> show counts scheduled

5. Start the counts.
> start_counts

6. Check the count has been started. do this on the website. also in shell
website should show "inProgress" next to name
> show counts in_progress

7. Now upload the products to the count. 
> product_count Outlet
It will then prompt you to select yes or no for the count it presents. Note, it will select the first count that matches that outlet, so there can only be one count in progress for each outlet.
Once you have the correct count, select y. 
It will show status bar as it updates products

8. Then proceed to finalize the count on vendhq.com
