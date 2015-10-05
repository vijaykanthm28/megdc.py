========================================================
 megdc -- Deploy a datacenter with minimal infrastructure
========================================================

``megdc`` is a way to deploy a datacenter. It runs fully on your
workstation, requiring no servers, databases, or anything like that.


This ``README`` provides a brief overview of megdc, for thorough
documentation please go to http://docs.megam.io/v1.0/docs


Installation
============
Depending on what type of usage you are going to have with ``megdc`` you
might want to look into the different ways to install it. Regular users of ``megdc`` would
probably install from the OS packages or from the Python Package Index.

Python Package Index
--------------------
If you are familiar with Python install tools (like ``pip`` and
``easy_install``) you can easily install ``megdc`` like::

    pip install megdc

or::

    easy_install megdc


It should grab all the dependencies for you and install into the current user's
environment.

We highly recommend using ``virtualenv`` and installing dependencies in
a contained way.


developing
----------

To get the source tree ready for use, run this once::

  git clone https://github.com/megamsys/megdc.git

  cd megdc

  virtualenv venv

  python setup.py install

  megdc

Voila! You will see the following help.




FAQ
===

Before anything
---------------
Make sure you have the latest version of ``megdc``. It is actively
developed and releases are coming weekly (on average). The most recent versions
of ``megdc`` will have a ``--version`` flag you can use, otherwise check
with your package manager and update if there is anything new
