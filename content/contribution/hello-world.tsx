import React from 'react';
import ReactDOM from 'react-dom/client';
import HelloWorld from './HelloWorld'; // Adjust path as needed

const App: React.FC = () => {
  return (
    <div className="App">
      <HelloWorld />
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
