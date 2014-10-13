#!/usr/bin/env python

import os

from sh import (
    git,
    sphinx_build,
)


def clone_repo(repo, target=None):
    """Clone repo to target and return the checkout directory path.

    If target is not specified, clone_repo defaults to ./docsrc

    """

    if target is None:
        target = os.path.join(os.getcwd(), 'docsrc')

    git.clone(repo, target)

    return target


def build_docs(source, builder, outputdir):

    sphinx_build('-b', builder, source, outputdir)
    

if __name__ == '__main__':

    outputdir = '/docs'
    builder = os.environ.get('BUILDER', 'html')
    
    checkout = clone_repo(os.environ['BUILD_REPO'])
    build_docs(checkout, builder, outputdir)
