import React from "react";
import ReactDOM from "react-dom";
import { ConfigProvider } from "antd";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import zhCN from "antd/lib/locale/zh_CN";

import HomePage from "./pages/HomePage";
import ManagePage from "./pages/ManagePage";
import DatasetPage from "./pages/DatasetPage";
import BaseHeader from "./component/BaseHeader";

import "antd/dist/antd.css";
import "../assets/index.css";
import "./assets/page.scss";
import "./assets/component.scss";

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <BrowserRouter>
        <BaseHeader />

        <Switch>
          <Route path="/dataset" component={DatasetPage} />
          <Route path="/manage" component={ManagePage} />
          <Route path="/" component={HomePage} />
        </Switch>
      </BrowserRouter>
    </ConfigProvider>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
