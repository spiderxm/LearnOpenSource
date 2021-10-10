import React, { useState } from "react";
import data from "./data";
import List from "./List";
function App() {
  const [birthdays, setBirthdays] = useState(data);
  function handleCLick() {
    setBirthdays([]);
  }
  return (
    <main>
      <section className="container">
        <h3>{birthdays.length} Birthdays Today</h3>
        <List birthdays={birthdays} />
        <button onClick={() => handleCLick()}>Clear All</button>
      </section>
    </main>
  );
}

export default App;
