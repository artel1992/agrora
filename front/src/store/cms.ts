import {defineStore, StateTree, StoreGeneric} from 'pinia'
import axios from "@/plugins/axios";
import {EditableComponent} from "@/core/interfaces";

export interface CMSState extends StateTree {
    edited: boolean
    nowEdit: EditableComponent<any> | null
}


export const useCMSStore = defineStore<'cmsStore', CMSState>('cmsStore', {
    state: (): CMSState => ({
        edited: false,
        nowEdit: null
    }),
    actions: {
        toggleEdit() {
            this.edited = !this.edited
        },
        setNowEdit(component: EditableComponent<any>) {
            this.nowEdit = component
            return 1
        },
        async getPage<T>(path: string): Promise<EditableComponent<T>> {
            return axios.get('components/by_page/', {params: {path}}).then(response => response.data)
        },
        async saveEditableComponent(data: EditableComponent<any>) {
            return axios.patch(`components/${data.id}/`, data).then(response => response.data)
        },
        async deleteEditableComponent(id: EditableComponent<any>['id']) {
            return axios.delete(`components/${id}/`).then(response => response.data)
        }
    }
})