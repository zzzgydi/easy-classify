import React, { useEffect } from "react";
import ReactDOM from "react-dom";
import { useAtom } from "jotai";
import { ConfigProvider } from "antd";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import zhCN from "antd/lib/locale/zh_CN";

import HomePage from "@/pages/HomePage";
import DataPage from "@/pages/DataPage";
import ModelPage from "@/pages/ModelPage";
import DatasetPage from "@/pages/DatasetPage";
import BaseHeader from "@/component/custom/BaseHeader";
import { updateDatasetAtom, updateModelAtom } from "@/state";

import "antd/dist/antd.css";
import "@/assets/style/index.css";
import "@/assets/style/page.scss";
import "@/assets/style/component.scss";

function App() {
  const [, updateModel] = useAtom(updateModelAtom);
  const [, updateDataset] = useAtom(updateDatasetAtom);

  useEffect(() => {
    updateModel(false);
    updateDataset(false);
  }, []);

  return (
    <ConfigProvider locale={zhCN}>
      <BrowserRouter>
        <BaseHeader />

        <Switch>
          <Route path="/dataset" component={DatasetPage} exact />
          <Route path="/model" component={ModelPage} exact />
          <Route path="/data" component={DataPage} exact />
          <Route path="/" component={HomePage} exact />
        </Switch>
      </BrowserRouter>
    </ConfigProvider>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
