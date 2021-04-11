import React from "react";
import { Link } from "react-router-dom";

const BaseHeader: React.FC = () => {
  return (
    <div className="base-header">
      <Link to="/">Home</Link>
      <Link to="/dataset">Dataset</Link>
      <Link to="/manage">Manage</Link>
    </div>
  );
};

export default BaseHeader;
