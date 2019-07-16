# slack_response
Denne lambdaen skal ta imot en request fra ```slack_command```-lambdaen og lage en response og gi
den til slack sin response_url.

## Virkemåte
Denne funker ved at den først henter ut de 10 neste fagarrangementene til knowit fra knowit sin
kalender, deretter ser den på requesten som kom inn for å finne ut hva slags event som gjorde at
lambdaen ble kjørt, er det noen som skal ha en ny kode til et arrangement eller skal man bare vise
alle uten å lage nye koder? Om noen trykket på ```Få kode```-knappen så må man generere en 
tilfeldig kode og så sjekke om den blir alt brukt eller ikke. Og så er det bare å bygge
json-objektet som skal returnes og vises fram som en Slack interactive block app og sende den 
til ```response_url```-en. 

Når koden blir gitt ut blir det også schedulet en melding fra slack som sier at du må registrere
 arrangementet. Så når arrangementet er ferdig så får du en melding fra slack-botten og du kan 
 da trykke på ```Registrer arrangement``` knappen og fylle inn hvor mange som kom der og hvilken 
 faggruppe som stod for dette arrangementet.

## Setup

For å sette opp denne lambdaen må du først lage en ```creds.json```.
Vi har et eget ```Dataplattform```-prosjekt i Google API console.
Lag en service account på prosjektet og velg json når du lagrer credentialsene.
Lagre som ```creds.json``` i denne mappen før du kjører ```deploy_to_aws.sh``` for å deploye
lambdaen.

HUSK: ```slack_response``` trenger tilgang til en ny tabell i DynamoDB
```dataplattform_event_codes```.

Environment variabler du trenger for denne lambdaen er:
* SLACK_BOT_TOKEN
* DATAPLATTFORM_FAGKALENDER_ID
* DATAPLATTFORM_INGEST_APIKEY
* DATAPLATTFORM_INGEST_URL