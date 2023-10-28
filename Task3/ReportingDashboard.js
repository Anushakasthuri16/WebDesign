import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ReportingDashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('/api/data'); // Fetch data from your backend API
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      {/* Display data in the reporting dashboard */}
      {data.map((item) => (
        <div key={item.id}>
          <p>{item.column1}</p>
          <p>{item.column2}</p>
          <p>{item.column3}</p>
          {/* Display other columns as needed */}
        </div>
      ))}
    </div>
  );
};

export default ReportingDashboard;