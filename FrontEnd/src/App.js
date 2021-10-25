import { useEffect, useState } from "react";
import Note from "./components/Note";
import axios from "axios";
import "./App.css";
import Formulario from "./components/Formulario";

function App() {

  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);


  console.log(notes);


  return (

    <div className="App">
      <div className="appbar">
        <img src="/logo-getit.png" className="logo" />
        <span className="subtitle">Como o Post-it, mas com outro verbo</span>
      </div>

      <main className="container">

        <Formulario/>

      <ul className="card-container">

        {notes.map((note) => (
          <Note key={`note__${note.id}`} title={note.title}>
            {note.content}
          </Note>
        ))}

      </ul>

    </main>

    </div>
  );
}

export default App;