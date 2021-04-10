import React from "react";
import ReactDOM from "react-dom";
import { ConfigProvider } from "antd";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import zhCN from "antd/lib/locale/zh_CN";

import Home from "./pages/Home";
import Manage from "./pages/Manage";
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
          <Route path="/manage" component={Manage} />
          <Route path="/" component={Home} />
        </Switch>
      </BrowserRouter>
    </ConfigProvider>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
