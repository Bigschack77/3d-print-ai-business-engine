@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  color-scheme: dark;
}

html, body {
  margin: 0;
  min-height: 100%;
  background: #020617;
  color: #e2e8f0;
  font-family: Arial, Helvetica, sans-serif;
}

body {
  min-height: 100vh;
}

.input {
  width: 100%;
  border-radius: 0.75rem;
  border: 1px solid rgba(148, 163, 184, 0.35);
  background: rgba(15, 23, 42, 0.75);
  padding: 0.7rem 0.8rem;
  color: white;
  outline: none;
}

.input:focus {
  border-color: rgba(34, 211, 238, 0.7);
  box-shadow: 0 0 0 2px rgba(34, 211, 238, 0.15);
}

button {
  cursor: pointer;
}
