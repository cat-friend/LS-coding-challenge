# [LINK TO DEPLOYED CODING CHALLENGE](https://dpl-loanstreet.herokuapp.com/)



# Local installation

## Prerequisites
 - [Node.js 16.13.1](https://nodejs.org/en/)


## Getting Started

1. Clone the project repository

   SSH:
```
   git clone git@github.com:cat-friend/LS-coding-challenge.git
```
   HTTPS:
```
git clone https://github.com/cat-friend/LS-coding-challenge.git
```
2. Install dependencies
```
   pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
```

3.  Create a local .env file modeled after the .env.example file in the root directory
```
   FLASK_APP=app
   FLASK_ENV=development
   SECRET_KEY=<<YOUR SECRET KEY>>
   DATABASE_URL=postgresql://<<DBUSER>>:<<DBUSER PASSWORD>>@localhost/<<DB NAME>>

```
4. Set up your PostgreSQL user, password, and database. Make sure that these values match your .env file!

5. Access your `pipenv shell`, migrate your database, seed your database, and run your flask app with the following commands:
```
pipenv shell
```
```
flask db upgrade
```
```
flask seed all
```
```
flask run
```

   In the future, if you'd like to unseed and reseed the database, you can run
   ```
   flask seed reset
   ```
   Caution! This will delete _all_ data in your database.

5. To run the React App, `cd` into the `react-app` directory, install `react-app`, and then start React:
 ```
    cd react-app
 ```
  ```
    npm install
 ```
  ```
    npm start
 ```
