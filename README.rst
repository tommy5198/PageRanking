simple pageranking for search engine
====================================

Information
-----------

- Search each txt file in specified directory
- Each text file corresponds to a web page in the Internet.
- There are N hyperlinks in each file, where N>=0.
- Every hyperlink is of the form (http://filename.txt), which represents the connection between web pages.

Environment
-----------

- Written in Python2.7.8
- Require NumPy for matrix calculate

You can use pip to install the NumPy library. Simply:
	
.. code-block:: bash

	$ pip install numpy
	
You may need `Microsoft Visual C++ Compiler for Python 2.7 <http://aka.ms/vcpython27>`_ to build NumPy.

Usage
-----

Give specified directory that contains txt files, and give a string query:

.. code-block:: bash

	$ python IKDDhw4.py <dir> <query>
 
Program will print out file's name and its rank whos content contain given string.
For example:

.. code-block:: bash

	$ python IKDDhw4.py webpage_data_5 知識挖掘與資料工程導論
	rank	filename
	1		page2.txt
	2		page5.txt
	3		page1.txt