import './App.css';
import { useState, useEffect, useRef } from 'react';

function App(props) {
  const [reviewscaught, setValue] = useState([]);
  const [inprate, setRate] = useState("");
  useEffect(() => {
    fetch('/revs', {
      method: "POST",
      headers: {
        "content_type": "application/json",
      }
    }).then((response) => response.json()).then((data) => {
      console.log(data)
      setValue(data)
    })
  }, [])
  const d = (r) => {
    const newreviews = [...reviewscaught];
    newreviews.splice(r, 1);
    console.log(newreviews)
    setValue(newreviews);
  }
  async function deleteratings(newreviews) {
    const response = await fetch("/del", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(newreviews),
    })
    if (response.ok) {
      window.alert("Deleted!")
      d(newreviews)
    }
  }
  function updaterate(props) {
    const newvalues = [...reviewscaught]
    const invalues = [...inprate]
    newvalues.splice(reviewscaught, reviewscaught.length)
    console.log(newvalues)
    setRate([...newvalues].concat(invalues))
  }
  function onchandle(e) {
    return setRate(e.target.value)
  }
  async function rett() {
    const rateupdate = inprate;
    const response = await fetch("/update", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(inprate),
    })
    if (response.ok) {
      window.alert("Saved!")
      updaterate(inprate)
      setRate("")
    }
  }
  return (
    <div className="App">
      <h2>Here are all your recent comments: </h2>
      <ul>
        {reviewscaught.map(movrev => {
          return <ul> {"Movieid: " + " " + movrev.rev_id + " Movie rating: " + " " + movrev.rating + " Comment:" + " "}
            <input type="text" name="newchange" value={movrev.reviews} />

            <button name="deleteme" onClick={deleteratings.bind(this, movrev)}> Delete Rating </button>

            <input type="text" name="newchange" value={props.inprate} onChange={onchandle} />
            <input type="hidden" id="custId" name="jsonid" value={movrev.id} />

            <button type="submit" name="mychange" value="addrate" onClick={rett}> Save Me!</button>
          </ul>
        }
        )
        }
      </ul>
    </div >
  );
}
export default App;

