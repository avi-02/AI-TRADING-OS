# Local Setup

## Clone

git clone ...

## Create Virtual Environment

python -m venv venv

## Activate

source venv/bin/activate

## Install

pip install -r requirements.txt

## Run

cd backend

uvicorn app.main:app --reload

## Test

pytest