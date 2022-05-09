import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
	const [ret, setRet] = useState("");
	function handleClick() {
    fetch('/fun_fact', {
      method: "POST",
      headers: {
        "content_type": "application/json",
      }
    }).then((response) => response.json()).then((data) => {
      console.log(data)
      setRet(data)
    })
  };
	return (
		<div className="App">
			<p>{ret}</p> 
			<button onClick={handleClick}>CLICK ME</button>
		</div>
	);
    }
export default App;