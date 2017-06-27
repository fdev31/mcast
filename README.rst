#####
MCast
#####

The simplest multicast file transfer app on earth ! ;)
+ pure python netcat (as fallback ?)

Pull data:

    .. code-block:: console

        mcast

Push data:

    .. code-block:: console

        mcast file.ext

Features
########

- transfer files of any size to multiple hosts at a time
- simple to use (even NetCat is more complex !)
- single file app, runs on any platform (pure Python)
- file corruption detected automatically

Limitations
###########

- computers must be on the same network
    - ``nc.py`` tool featured for *traditional* tcp connections
- one file transfer at a time [TODO: fix this] 

How to use it
#############

receive
    call ``mcast`` without argument
send
    call ``mcast`` with file as argument, or "``-``" for stdin

There are two steps:

#. start program on each computer wanting to receive the file or content
#. start the program with the file as parameter on any computer of the network

On computers you want to send the file to
-----------------------------------------

Run this command to receive data and show it on the console:

.. code-block:: console

    mcast

or, more common, saving the content to a file:

.. code-block:: console

    mcast > my_super_file.ext

or, unpack the transmitted tar archive:

.. code-block:: console

    mcast | tar xvf

On the computer owning the file to distribute
---------------------------------------------

.. code-block:: console

    mcast path/to/file.ext

or, if you want to send multiple files using tar

.. code-block:: console

    tar cvf - path/to/send | mcast -


Developers
##########

This app is supported and tested only under Linux, but patches for other OS are accepted.
