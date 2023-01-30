# Transcriber-Describer

To run the code, you can either run `node index.js` directly in the terminal, or use the `npm start` command if you have specified the `start` script in your `package.json` file.

### Setting up the Google Speech-to-Text API:

1. Go to the Google Cloud Console (https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Go to the API Library and enable the Speech-to-Text API.
4. Go to the Credentials page and create a new Service Account.
5. Give the Service Account a name and role, then download the private key as a JSON file.
6. In your Node.js project, install the `@google-cloud/speech` library using npm: `npm install @google-cloud/speech`
7. Set the path to the private key file as the value of the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in your terminal: `export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"`.

### Setting up your OpenAI API credentials:

1. Sign up for an OpenAI account if you don't already have one.
2. Go to the API Key section of the OpenAI Dashboard.
3. Create a new API Key by clicking the "Generate API Key" button.
4. Store your API Key securely in your application or system.
5. When making API requests, include the API Key as a bearer token in the authorization header.
