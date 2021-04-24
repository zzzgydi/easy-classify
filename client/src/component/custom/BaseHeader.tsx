import React from "react";
import { Link } from "react-router-dom";

const BaseHeader: React.FC = () => {
  return (
    <div className="base-header">
      <Link to="/">Home</Link>
      <Link to="/dataset">Dataset</Link>
      <Link to="/data">Data</Link>
      <Link to="/model">Model</Link>
    </div>
  );
};

export default BaseHeader;
