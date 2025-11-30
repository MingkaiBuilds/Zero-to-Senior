import { useState } from "react";
import { StudyInput } from "./components/StudyInput";
import { StudyList } from "./components/StudyList";

function App() {
  const [sessions, setSessions] = useState<string[]>([]);

  function addSession(name: string) {
    setSessions([...sessions, name]);
  }

  return (
    <div>
      <h1>Study Session Tracker</h1>
      <StudyInput onAdd={addSession} />
      <StudyList sessions={sessions} />
    </div>
  );
}

export default App;