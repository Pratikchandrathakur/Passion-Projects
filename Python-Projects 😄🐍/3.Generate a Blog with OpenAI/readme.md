# Safely Storing Openai API keys which prevent unnecessary exposing:
## For Windows:
Open Command Prompt and run:
```
setx OPENAI_API_KEY "your-new-api-key"
```
## For macOS/Linux:
Open your terminal and run:
```
export OPENAI_API_KEY="your-new-api-key"
```
## Using .env file:
- In python file copy and paste this:
```
  from dotenv import dotenv_values

  config = dotenv_values(".env")
```

```
openai.api_key = config['API_KEY']
```
