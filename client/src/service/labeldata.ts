import axios from "./index";

export interface LabelDataModel {
  id: number;
  label: string;
  data: string;
}

class LabeldataApi {
  async list(datasetId: number, page: number, pagesize: number): Promise<any> {
    return axios
      .get("/api/data", {
        params: { dataset: datasetId, page, pagesize },
      })
      .then((res: any) => {
        const result: LabelDataModel[] = res.result.map((item: any[]) => ({
          id: item[0],
          label: item[1],
          data: item[2],
        }));
        return { ...res, result };
      });
  }

  async add(datasetId: number, label: string, datalist: string[]) {
    return axios.post("/api/data", { dataset: datasetId, label, datalist });
  }

  async remove(id: number) {
    return axios.delete("/api/data", { params: { id } });
  }

  async labels(datasetId: number) {
    return axios.get("/api/data/label", { params: { dataset: datasetId } });
  }
}

export default new LabeldataApi();
