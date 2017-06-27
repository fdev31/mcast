#####
MCast
#####

The simplest multicast file transfer app on earth ! ;)

How to use it
#############

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

