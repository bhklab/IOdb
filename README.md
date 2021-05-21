# PredictIO Webapp

PredictIO is an web application that allows users to explore gene signatures in 19 immunotherapy studies of ICB-treated patients, and to obtain gene signature predictions using molecular data of their own studies of ICB-treated patients.

The latest version can be found at https://predictio.ca/

## Setup Instructions

- Clone the repo
  
```bash
git clone https://github.com/bhklab/PredictIO-webapp.git
cd IOdb
```

- In the project directory, install all the server dependencies using `pip install -r requirements.txt
- To start the server run this command `flask run`
- In the project directory, install all client dependencies `npm i`
- Start the client (development mode) by running `npm start`
- Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Dependencies

- React
- React-Route
- Body-parser

## Dev Dependenices

- Eslint

## Database Generation

- Download raw_data directory from [https://codeocean.com/capsule/6711882/tree](https://codeocean.com/capsule/6711882/tree) capsule
- Run data generation script which would create CSV files for the database tables

```bash
python scripts/generate_seed_files.py
```

- To create tables and seed the database, run the following command:

```bash
flask seed-database
```
This command will run db/seed_database.py with app context. Modify the file if necessary.

## Build Instructions

### `cd client && npm build`

Builds the app for production to the `build` folder.
It correctly bundles React in production mode and optimizes the build for the best performance.

## Server

- To be determined.
