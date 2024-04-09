import App from "./App";

async function loadConfig() {
  const configResponse = await fetch("/config.json");
  const config = await configResponse.json();

  return config;
}

export default loadConfig;
