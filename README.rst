DocBox
======

A Docker Image for Building Sphinx Projects

Why?
----

Because executing shell commands from Python to build user-provided
source is madness.

Building Your Docs
------------------

::

  $ sudo docker run -v /path/to/output:/docs -e
  "BUILD_REPO=http://githost.com/my/repo.git" docbox/latest

DocBox uses the ``html`` builder by default. You can specify a
different builder by setting the ``BUILDER`` environment variable. For
example, to build Hieroglyph slides::

  $ sudo docker run -v /path/to/output:/docs 
  -e "BUILDER=slides"
  -e "BUILD_REPO=http://githost.com/my/repo.git" docbox/latest

If your docs aren't located in the root of the repository, just set
``BUILD_DIR``::

  $ sudo docker run -v /path/to/output:/docs 
  -e "BUILD_DIR=docs"
  -e "BUILD_REPO=http://githost.com/my/repo.git" docbox/latest

Developing
----------

Building the Image
~~~~~~~~~~~~~~~~~~

::

  $ sudo docker build -t docbox/latest .

