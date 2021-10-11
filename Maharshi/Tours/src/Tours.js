import React from "react";
import Tour from "./Tour";
const Tours = ({ tours, removeTours }) => {
  return (
    <section>
      <div className="title">
        <h2>Our Tours</h2>
        <div className="underline"></div>
      </div>
      <div>
        {tours.map((item) => {
          return <Tour key={item.id} {...item} removeTours={removeTours} />;
        })}
      </div>
    </section>
  );
};

export default Tours;
