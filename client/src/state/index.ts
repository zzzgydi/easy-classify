import { atom } from "jotai";
import modelApi from "@/service/model";
import datasetApi from "@/service/dataset";

const modelLockAtom = atom(false);
const datasetLockAtom = atom(false);

export const modelAtom = atom<any[]>([]); // 模型数据列表
export const datasetAtom = atom<any[]>([]); // 数据集

// 更新模型列表
export const updateModelAtom = atom(null, (get, set, force: boolean) => {
  if (get(modelLockAtom)) return;
  if (!force && get(modelAtom).length > 0) return;
  set(modelLockAtom, true);

  const updateModel = async () => {
    const pageSize = 200;
    let page = 1;
    let total = Number.MAX_VALUE;
    let newModels: any[] = [];

    while (newModels.length < total) {
      const { result, count } = await modelApi.list(page, pageSize);
      page += 1;
      total = count;
      newModels = [...newModels, ...result];
      set(modelAtom, newModels);
    }
  };
  updateModel().finally(() => set(modelLockAtom, false));
});

// 更新数据集列表
export const updateDatasetAtom = atom(null, (get, set, force: boolean) => {
  if (get(datasetLockAtom)) return;
  if (!force && get(datasetAtom).length > 0) return;

  set(datasetLockAtom, true);

  const updateDataset = async () => {
    const pageSize = 200;
    let page = 1;
    let total = Number.MAX_VALUE;
    let newDataset: any[] = [];

    while (newDataset.length < total) {
      const { result, count } = await datasetApi.list(page, pageSize);
      page += 1;
      total = count;
      newDataset = [...newDataset, ...result];
      set(datasetAtom, newDataset);
    }
  };
  updateDataset().finally(() => set(datasetLockAtom, false));
});
