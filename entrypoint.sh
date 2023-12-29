#!/bin/bash

if [ ${DEPLOY_BRANCH} == "dev" ];
then
  git checkout dev
else
  git checkout main
fi

cd src && python3 manage.py runserver 0.0.0.0:8000
