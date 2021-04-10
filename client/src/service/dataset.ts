import axios from "./index";

interface LabelData {
  id?: string | number;
  label: string;
  data: string;
  key?: string;
}

// 获取所有数据
export function apiGetData(
  name: string,
  page: number,
  pagesize: number
): Promise<any> {
  return axios
    .get("/api/data", { params: { name, page, pagesize } })
    .then((res: any) => {
      const { code, result, count } = res;
      if (code !== 200) return Promise.reject(code);

      const results = result.map((result: any[]) => {
        const [id, label, data] = result;
        return { id, label, data };
      });
      return { results, count };
    });
}

// 批量添加数据
export function apiAddData(
  name: string,
  label: string,
  datalist: string[]
): Promise<any> {
  return axios.post("/api/data", { name, label, datalist });
}

// 删除数据
export function apiDeleteData(id: string | number): Promise<any> {
  return axios.delete("/api/data", { params: { id } });
}

// 获取所有数据集的名称
export function apiGetDataset(): Promise<any> {
  return axios.get("/api/dataset");
}

// 获取数据集的标签
export function apiGetLabel(name: string): Promise<any> {
  return axios.get("/api/label", { params: { name } });
}

// 获取所有模型
export function apiGetModel(): Promise<any> {
  return axios.get("/api/model");
}
