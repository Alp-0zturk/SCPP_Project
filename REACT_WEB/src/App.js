import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [make, setMake] = useState('');
  const [model, setModel] = useState('');
  const [year, setYear] = useState('');
  const [price, setPrice] = useState(0);

  const calculatePrice = () => {
    if (make && model && year) {
      const calculatedPrice = 20000 - (2024 - parseInt(year)) * 1000;
      setPrice(calculatedPrice);
    } else {
      setPrice(0);
    }
  };

  return (
    <div className='bgcol'>
      <div className="container">
        <h1>Find Your Car</h1>
        <div className="dropdown">
          <select id="make" value={make} onChange={(e) => setMake(e.target.value)}>
            <option value="">Select Make</option>
            <option value="honda">Honda</option>
            <option value="ford">Ford</option>
          </select>
        </div>
        <div className="dropdown">
          <select id="model" value={model} onChange={(e) => setModel(e.target.value)}>
            <option value="">Select Model</option>
            <option value="ranger">Ranger</option>
            <option value="mustang">Mustang</option>
            <option value="fusion">Fusion</option>
            <option value="f-100">F-100</option>
            <option value="f-800">F-800</option>
            <option value="civic">Civic</option>
            <option value="ridgeline">Ridgeline</option>
            <option value="pilot">Pilot</option>
            <option value="odyssey">Odyssey</option>
            <option value="fit">Fit</option>
          </select>
        </div>
        <div className="dropdown">
          <input
            id="odometer"
            style={{ borderRadius: "4px", minWidth: "95%", padding: "10px", border: "1px solid #ccc" }}
            type="text"
            fontSize="2em"
            placeholder="Type odometer value"
          />
        </div>
        <div className="dropdown">
          <select id="transmission">
            <option value="">Select Transmission</option>
            <option value="automatic">Automatic</option>
            <option value="manual">Manual</option>
          </select>
        </div>
        <div className="dropdown">
          <select id="condition">
            <option value="">Select Condition</option>
            <option value="new">New</option>
            <option value="like new">Like New</option>
            <option value="excellent">Excellent</option>
            <option value="good">Good</option>
            <option value="fair">Fair</option>
            <option value="salvage">Salvage</option>
          </select>
        </div>
        <div className="dropdown">
          <select id="year" value={year} onChange={(e) => setYear(e.target.value)}>
            <option value="">Select Year</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
            <option value="2017">2017</option>
            <option value="2016">2016</option>
            <option value="2015">2015</option>
            <option value="2014">2014</option>
            <option value="2013">2013</option>
            <option value="2012">2012</option>
            <option value="2011">2011</option>
            <option value="2010">2010</option>
            <option value="2009">2009</option>
          </select>
        </div>
        <button className="btn" onClick={calculatePrice}>Get Price</button>
        <div className="result-box" id="price-result">${price}</div>
      </div>
    </div>
  );
};

export default App;
